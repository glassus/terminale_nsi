// noinspection SqlNoDataSourceInspection

function load(ide, base = '', init = '', run='', espace='') {
    var execBtn = ide.querySelector("button.execute");
    var outputElm = ide.querySelector('pre.sqloutput');
    var errorElm = ide.querySelector('div.sqlerror');
    var commandsElm = ide.querySelector('textarea.sqlcommands');

    // Start the worker in which sql.js will run
    var worker = espace;
    var neww;
    if (espace === '') {
        worker = new Worker(path + "/js/worker.sql-wasm.js");
        worker.onerror = error;
        neww = true;
    } else {
        if (worker.onerror !== null) {
            worker.onerror = error;
            neww = true;
        } else {
            neww = false;
        }

    }
// Open a database
    if (neww) worker.postMessage({action: 'open'});
    if (base !== '/') {
        const u = new URL(base)
        fetch(u).then(res => {
            return res.arrayBuffer()
        }).then(buf => {
            try {
                worker.postMessage({action: 'open', buffer: buf}, [buf]);
            } catch (exception) {
                worker.postMessage({action: 'open', buffer: buf});
            }
            if (run !== '') {execute(run, false);}
        });
    }
    else if (init !== '') {
        execute(init, true);
        if (run !=='') execute(run, false);
    }

    function error(e) {
        outputElm.innerHTML = ''
        errorElm.style.height = '2em';
        errorElm.textContent = e.message;
    }

    function noerror() {
        errorElm.style.height = '0';
        errorElm.textContent = ''
    }

// Run a command in the database
    function execute(commands, silent = false) {
        tic();
        worker.onmessage = function (event) {
            var results = event.data.results;
            toc("Executing SQL");
            if (!results) {
                error({message: event.data.error});
                return;
            }

            tic();
            outputElm.innerHTML = "";
            for (const element of results) {
                outputElm.appendChild(tableCreate(element.columns, element.values));
            }
            if (outputElm.childElementCount === 0 && !silent) outputElm.innerHTML = "<p>Requête exécutée correctement, pas de résultat à afficher.</p>";
            toc("Displaying results");
        }
        worker.postMessage({action: 'exec', sql: commands});
        outputElm.textContent = "Fetching results...";
    }

// Create an HTML table
    var tableCreate = function () {
        function valconcat(vals, tagName) {
            if (vals.length === 0) return '';
            var open = '<' + tagName + '>', close = '</' + tagName + '>';
            return open + vals.join(close + open) + close;
        }

        return function (columns, values) {
            var tbl = document.createElement('table');
            tbl.className = 'sqltable';
            var html = '<thead>' + valconcat(columns, 'th') + '</thead>';
            var rows = values.map(function (v) {
                return valconcat(v, 'td');
            });
            html += '<tbody>' + valconcat(rows, 'tr') + '</tbody>';
            tbl.innerHTML = html;
            return tbl;
        }
    }();

// Execute the commands when the button is clicked
    function execEditorContents() {
        noerror()
        execute(editor.getValue() + ';');
    }

    execBtn.addEventListener("click", execEditorContents, true);

// Performance measurement functions
    var tictime;
    if (!window.performance || !performance.now) {
        window.performance = {now: Date.now}
    }

    function tic() {
        tictime = performance.now()
    }

    function toc(msg) {
        var dt = performance.now() - tictime;
        console.log((msg || 'toc') + ": " + dt + "ms");
    }

// Add syntax highlihjting to the textarea
    var editor = CodeMirror.fromTextArea(commandsElm, {
        mode: 'text/x-mysql',
        viewportMargin: Infinity,
        indentWithTabs: true,
        smartIndent: true,
        lineNumbers: true,
        matchBrackets: true,
        autofocus: false,
        extraKeys: {
            "Ctrl-Enter": execEditorContents,
        }
    });
}


/**
 *
 * Wait for an HTML element to be loaded like `div`, `span`, `img`, etc.
 * ex: `onElementLoaded("div.some_class").then(()=>{}).catch(()=>{})`
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




