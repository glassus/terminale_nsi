// noinspection SqlNoDataSourceInspection


// Performance measurement functions (also used in the worker's js code)
var tictime;
if (!window.performance || !performance.now) {
    window.performance = { now: Date.now }
}


// Because of navigation.instant usage or not, the class may be already defined (or
// not), so check first:
if(!window.SqlIde){

    function valconcat(vals, tagName) {
        if (vals.length === 0) return '';
        var open = '<' + tagName + '>', close = '</' + tagName + '>';
        return open + vals.join(close + open) + close;
    }

    /**@ide: the html div holding the elements for the current SqlIde.
     * @base: path to the database to use.
     * @init: initial commands to apply at instantiation time.
     * @run: initial commands to run, if any.
     * @espace: the global worker object for the current space, if any.
     * */
    class SqlIde {

        constructor(ide, base = '', init = '', run = '', espace = null) {
            console.log("SqlIde", ide, base, init, run, espace);

            this.execBtn = ide.querySelector("button.execute");
            this.outputElm = ide.querySelector('pre.sqloutput');
            this.errorElm = ide.querySelector('div.sqlerror');
            this.commandsElm = ide.querySelector('textarea.sqlcommands');

            // Start the worker in which sql.js will run
            this.worker = espace;
            let neww;
            if (espace === null) {
                this.worker = new Worker(sqljs_base_path + "/js/worker.sql-wasm.js");
                this.worker.onerror = this.error.bind(this);
                neww = true;
            } else if (this.worker.onerror !== null) {
                this.worker.onerror = this.error.bind(this);
                neww = true;
            } else {
                neww = false;
            }
            // Open a database
            if (neww) this.worker.postMessage({ action: 'open' });

            let promesse = Promise.resolve()
            if (base !== '/') {
                const u = new URL(base)
                promesse = fetch(u).then(res => {
                    return res.arrayBuffer()
                }).then(buf => {
                    try {
                        this.worker.postMessage({ action: 'open', buffer: buf }, [buf]);
                    } catch (exception) {
                        this.worker.postMessage({ action: 'open', buffer: buf });
                    }
                });
            }
            promesse.then(()=>{
                if(init !== '') this.execute(init, true);
                if (run !== '') this.execute(run, false);
            }).catch(console.error)


            this.execBtn.addEventListener("click", this.execEditorContents.bind(this), true);

            // Add syntax highlighting to the textarea
            this.editor = CodeMirror.fromTextArea(this.commandsElm, {
                mode: 'text/x-mysql',
                viewportMargin: Infinity,
                indentWithTabs: true,
                smartIndent: true,
                lineNumbers: true,
                matchBrackets: true,
                autofocus: false,
                extraKeys: {
                    "Ctrl-Enter": this.execEditorContents.bind(this),
                }
            });
        }

        error(e) {
            this.outputElm.innerHTML = ''
            this.errorElm.style.height = '2em';
            this.errorElm.textContent = e.message;
        }

        noerror() {
            this.errorElm.style.height = '0';
            this.errorElm.textContent = ''
        }

        // Run a command in the database
        execute(commands, silent = false) {
            this.tic();
            this.outputElm.textContent = "Fetching results...";
            const ideThis = this
            this.worker.onmessage = function (event) {
                var results = event.data.results;
                ideThis.toc("Executing SQL");
                if (!results) {
                    ideThis.error({ message: event.data.error });
                    return;
                }
                ideThis.showResults(results, silent)
            }
            this.worker.postMessage({ action: 'exec', sql: commands });
        }


        showResults(results, silent){
            this.tic();
            this.outputElm.innerHTML = "";
            for (const element of results) {
                const table = this.tableCreate(element.columns, element.values)
                new Tablesort(table)
                this.outputElm.appendChild(table);
            }
            if (this.outputElm.childElementCount === 0 && !silent) this.outputElm.innerHTML = "<p>Requête exécutée correctement, pas de résultat à afficher.</p>";
            this.toc("Displaying results");
        }


        // Create an HTML table
        tableCreate(columns, values) {

            var tbl = document.createElement('table');
            tbl.className = 'sqltable';
            var html = '<thead>' + valconcat(columns, 'th') + '</thead>';
            var rows = values.map(function (v) {
                return valconcat(v, 'td');
            });
            html += '<tbody>' + valconcat(rows, 'tr') + '</tbody>';
            tbl.innerHTML = html;
            return tbl;
        };

        // Execute the commands when the button is clicked
        execEditorContents() {
            this.noerror()
            this.execute(this.editor.getValue() + ';');
        }

        tic() {
            tictime = performance.now()
        }

        toc(msg) {
            const dt = performance.now() - tictime;
            console.log((msg || 'toc') + ": " + dt + "ms");
        }
    }








    /**Wait for an HTML element to be loaded like `div`, `span`, `img`, etc.
     *
     * ex: `onElementLoaded("div.some_class").then(()=>{}).catch(()=>{})`
     *
     * @param {*} elementToObserve wait for this element to load
     * @param {*} parentStaticElement (optional) if parent element is not passed then `document` is used
     * @return {*} Promise - return promise when `elementToObserve` is loaded
     */
    function onElementLoaded(elementToObserve, parentStaticElement) {
        return new Promise((resolve, reject) => {
            try {
                if (document.querySelector(elementToObserve)) {
                    resolve(true);
                    return;
                }
                const parentElement = parentStaticElement
                    ? document.querySelector(parentStaticElement)
                    : document;

                const observer = new MutationObserver((_mutationList, obsrvr) => {
                    const divToCheck = document.querySelector(elementToObserve);

                    if (divToCheck) {
                        console.log(`element loaded: ${elementToObserve}`);
                        obsrvr.disconnect(); // stop observing
                        resolve(true);
                    }
                });

                // start observing for dynamic div
                observer.observe(parentElement, {
                    childList: true,
                    subtree: true,
                });
            } catch (e) {
                console.log(e);
                reject(Error("some issue... promise rejected"));
            }
        });
    }

    // Assign globally, enlarging the scope:
    window.SqlIde = SqlIde
    window.onElementLoaded = onElementLoaded
}