var dict = {};  // Global dictionnary tracking the number of clicks
const nAttempts = 5;

function sleep(s){
    return new Promise(resolve => setTimeout(resolve, s));
  }
  
async function main() {
    await loadPyodide({ indexURL : 'https://cdn.jsdelivr.net/pyodide/v0.17.0/full/' });
}

let pyodideReadyPromise = main();

async function pyterm(id, height) {
await pyodideReadyPromise;
let namespace = pyodide.globals.get("dict")();

// creates the console
// the variable pyconsole is created here.
pyodide.runPython(`
    import sys
    import js
    from pyodide import console
    import __main__

    class PyConsole(console._InteractiveConsole):
        def __init__(self):
            super().__init__(
                __main__.__dict__,
                persistent_stream_redirection=False,
            )

        def banner(self):
            return f"Welcome to the Pyodide terminal emulator 🐍\\n{super().banner()}"

    
    js.pyconsole = PyConsole()
`, namespace);
namespace.destroy();

await pyodideReadyPromise;

// const url1 = 'https://raw.githubusercontent.com/bouillotvincent/bouillotvincent.github.io/master/js-turtle.py'
// // const url1 = 'https://glcdn.githack.com/bouillotvincent/pyodide-mkdocs/-/raw/main/js-turtle.py'
// const response = await fetch(url1);
// const data = await response.text();
// console.log(data);

// pyodide.runPython(data);
 

// pyodide.registerJsModule("turtle", my_module);
// console.log('ici',pyodide.globals.get("dict")())

let ps1 = '>>> ', ps2 = '... ';

async function lock(){
    let resolve;
    let ready = term.ready;
    term.ready = new Promise(res => resolve = res);
    await ready;
    return resolve;
}

async function interpreter(command) {  /// reads the commands
    let unlock = await lock();
    try {
    term.pause();
    // multiline should be splitted (useful when pasting)
    for( const c of command.split('\n') ) {
        let run_complete = pyconsole.run_complete;   // trying to run the commands
        try {
            const incomplete = pyconsole.push(c);    // wait for completion of a Python command
            term.set_prompt(incomplete ? ps2 : ps1); // set the prompt line
            let r = await run_complete;
            if(pyodide.isPyProxy(r)){
            r.destroy();
            }
        } catch(e){   // the completion of the Python command triggered an error (wrong Python syntax)
            if(e.name !== "PythonError"){
            term.error(e);
            throw e;
            }
        }
        run_complete.destroy();
    }
    } finally {
    term.resume();
    await sleep(10);
    unlock();
    }
}

let term = $(id).terminal(   // creates terminal
    interpreter,      // how to read the input
    {
    greetings: '',    // pyconsole.banner(),
    prompt: ps1,
    completionEscape: false,
    height: height,  // if not specified, css says 200
    completion: function(command, callback) {     // autocompletion
        callback(pyconsole.complete(command).toJs()[0]);
    }
    }
);

window.term = term;
pyconsole.stdout_callback = s => $.terminal.active().echo(s, {newline : false});   // this is thie line to change
    pyconsole.stderr_callback = s => {
        $.terminal.active().error(s.trimEnd());
    }


term.ready = Promise.resolve();
pyodide._module.on_fatal = async (e) => {
    term.error("Pyodide has suffered a fatal error. Please report this to the Pyodide maintainers.");
    term.error("The cause of the fatal error was:");
    term.error(e);
    term.error("Look in the browser console for more details.");
    await term.ready;
    term.pause();
    await sleep(15);
    term.pause();
};
}

// function find_imports

// function myLoadPackagesFromImports(code){
//     pyodide.runPython(`from pyodide import find_imports\nimported_modules = find_imports(${JSON.stringify(code)})`)
    
//     pyodide.loadPackagesFromImports(code)
//     return pyodide.globals.get("my_eval_code")(code, pyodide.globals);
// }

function removeLines(data, moduleName) {
    console.log('137', moduleName)
    return data
      .split('\n')
      .filter(sentence => !(sentence.includes("import " + moduleName) || sentence.includes("from " + moduleName)))
      .join('\n');
}

async function foreignModulesFromImports(code, moduleDict = {}) {
    await pyodideReadyPromise;
    pyodide.runPython(`from pyodide import find_imports\nimported_modules = find_imports(${JSON.stringify(code)})`)
    const importedModules = pyodide.globals.get('imported_modules').toJs();
    var executedCode = code
    for (var moduleName in moduleDict) {
        let moduleURL = moduleDict[moduleName];
      
        if (importedModules.includes(moduleName)) {
            console.log('169', importedModules, moduleName, moduleURL)
            // let url = moduleURL//"https://raw.githubusercontent.com/bouillotvincent/bouillotvincent.github.io/master/js-turtle.py"
            const response = await fetch(moduleURL);
            const module_code = await response.text();
            console.log(module_code)
            pyodide.runPython(module_code);
        }
        console.log('170', 'moduleName', executedCode)
        executedCode = removeLines(executedCode, moduleName)

    };

    return executedCode
}

async function evaluatePythonFromACE(code, id_editor, mode) {
    await pyodideReadyPromise;

    $.terminal.active().clear();   
    pyodide.runPython(`
      import sys as __sys__
      import io as __io__
      __sys__.stdout = __io__.StringIO()
    `);

    // TODO WARNING memory leak : globals() should be cleaned. Code below is too aggressive !!  
    // pyodide.runPython(`
    // variable = 0
    // for variable in list(globals()):
    //     if variable[0:2] != "__":
    //         print('variable globale', globals()[variable])
    //         del globals()[variable]
    // `)
    // console.log(pyodide.globals.dict())

    // resize terminal to the size of editor on interpreting
    if (mode === "v") {
        $.terminal.active().resize($.terminal.active().width(), document.getElementById(id_editor).style.height);
    }

    try {
      // console.log('boubou', code, JSON.stringify(code),JSON.stringify(code.replace(/\n/g, "hello")))
      // JSON.stringify() convert code intro real string with \n \t characters
      // await pyodide.myLoadPackagesFromImports(code)
    //   pyodide.runPython(`from pyodide import find_imports\nimported_modules = find_imports(${JSON.stringify(code)})`)
    //   const importedModules = pyodide.globals.get('imported_modules').toJs();
    //   if (importedModules.includes("turtle")) {
    //       console.log('169', importedModules)
    //       let url = "https://raw.githubusercontent.com/bouillotvincent/bouillotvincent.github.io/master/js-turtle.py"
    //       const response = await fetch(url);
    //       const turtle_module = await response.text();

    //       pyodide.runPython(turtle_module);
    //   }

    //   const removeLines = (data) => {
    //     return data
    //         .split('\n')
    //         .filter(word => word !== "import turtle")
    //         .join('\n');
    //   }

      
    //   let executed_code = removeLines(code)
      let executed_code = await foreignModulesFromImports(code, {'turtle': "https://raw.githubusercontent.com/bouillotvincent/bouillotvincent.github.io/master/js-turtle.py"})
      await pyodide.runPythonAsync("from __future__ import annotations\n"+executed_code);    // Running the code
      var stdout = pyodide.runPython("__sys__.stdout.getvalue()")  // Catching and redirecting the output
      $.terminal.active().echo(">>> Script exécuté !\n"+stdout); 
    } catch(err) {
      $.terminal.active().echo(">>> Script exécuté !\n"+err);
    }
  }

// async function silent_evaluatePythonFromACE(code, id_editor, mode) {
//     await pyodideReadyPromise;

//     $.terminal.active().clear();

//     // if (mode === "vert") {
//     //     $.terminal.active().resize($.terminal.active().width(), document.getElementById(id_editor).style.height);
//     // }

//     try {
//       pyodide.runPython("from __future__ import annotations\n"+code);    // Running the code OUTPUT
//     } catch(err) {
//       $.terminal.active().echo(">>> Code invalide !\n"+err);
//       return err
//     }
//   }


async function interpretACE(id_editor, mode) {
    window.console_ready = await pyterm('#term_'+id_editor, 150);
    $('#term_'+id_editor).terminal().focus(true);   // gives the focus to the corresponding terminal
    var editor = ace.edit(id_editor);
    let stream = await editor.getSession().getValue();
    calcTermSize(stream, mode)
    evaluatePythonFromACE(stream, id_editor, mode);
}

async function silent_interpretACE(id_editor) {
    window.console_ready = await pyterm('#term_'+id_editor, 150);
    $('#term_'+id_editor).terminal().focus(true);   // gives the focus to the corresponding terminal
    var editor = ace.edit(id_editor);
    let stream = await editor.getSession().getValue();
    return stream
}

async function start_term(nom_id) {
    document.getElementById(nom_id).className = "terminal terminal_f";
    document.getElementById('fake_'+nom_id).className = "hide";
    window.console_ready = pyterm('#'+nom_id);
    }

function download_file(id_editor, nom_script) {
    var editor = ace.edit(id_editor);
    let data = editor.getValue();
    let splitDate = new Date().toISOString().split('T')
    let date = splitDate[0] + '-' + splitDate[1].split('.')[0].replace(/:/g, "-"); 
    var script2download = 'script_' + date + '.py';
    if (nom_script !== '') {
        script2download = nom_script+'.py';
    }

    let link = document.createElement('a');
    link.download = script2download;
    let blob = new Blob(['' + data + ''], {
        type: 'text/plain'
    });
    link.href = URL.createObjectURL(blob);
    link.click();
    URL.revokeObjectURL(link.href);
}

function calcTermSize(text, mode) {
    let nlines = (mode === 'v' ? text.split(/\r\n|\r|\n/).length : Math.max(5,Math.min(10, text.split(/\r\n|\r|\n/).length)))
    $.terminal.active().resize($.terminal.active().width(), nlines*30);
    return nlines
  }

function executeTest(id_editor, mode) {    
    executeTestAsync(id_editor, mode)
}

function showCorrection(id_editor) {
    if (document.getElementById("corr_"+id_editor) === null) {
    let wrapperElement = document.getElementById(id_editor);  /* going up the DOM to IDE+buttons */ 
    while (wrapperElement.className !== "ide_classe") {
        wrapperElement = wrapperElement.parentNode
    }
    var txt = document.createElement("div");
    txt.innerHTML='<details class="check"><summary>Solution</summary>\
    <div class="highlight" id="corr_'+id_editor+'"></div></details>'

    let url_pyfile = document.getElementById("corr_content_"+id_editor).textContent

    function createACE(id_editor){
        var editor = ace.edit(id_editor, {
            theme: "ace/theme/tomorrow_night_bright",
            mode: "ace/mode/python",
            autoScrollEditorIntoView: true,
            maxLines: 30,
            minLines: 6,
            tabSize: 4,
            readOnly: true,
            printMargin: false   // hide ugly margins...
        });
        // Decode the backslashes into newlines for ACE editor from admonitions 
        // (<div> autocloses in an admonition) 
        editor.getSession().setValue(url_pyfile.replace(/backslash_newline/g, "\n"))  
    }
    wrapperElement.insertAdjacentElement('afterend', txt)
    window.IDE_ready = createACE('corr_'+id_editor)           // Creating Ace Editor #id_editor
}}

async function executeTestAsync(id_editor, mode) {
    await pyodideReadyPromise;
    let interpret_code = silent_interpretACE("editor_"+id_editor, "")

    let code = await interpret_code;
    $.terminal.active().clear();

    // if (mode === "vert") {
    //     $.terminal.active().resize($.terminal.active().width(), document.getElementById(id_editor).style.height);
    // }

    try {
        pyodide.runPython("from __future__ import annotations\n"+code);    // Running the student code (no output)

        let test_code = document.getElementById("test_term_editor_"+id_editor).textContent.replace(/backslash_newline/g, "\n");
        pyodide.runPython(`
        import sys as __sys__
        import io as __io__
        import js
        __sys__.stdout = __io__.StringIO()

        if 'test_unitaire' not in list(globals()):
            from random import choice

        def test_unitaire(numerous_benchmark):
            global_failed = 0
            success_smb = ['🔥','✨','🌠','✅','🥇','🎖']
            fail_smb = ['🌩','🙈','🙉','⛑','🌋','💣']
            if type(numerous_benchmark[0]) not in [list, tuple]:  # just one function has to be evaluated
                type_bench = 'multiple' 
                numerous_benchmark = (numerous_benchmark, )

            for benchmark in numerous_benchmark:
                failed = 0
                print(f">>> Test de la fonction ** {benchmark[0].split('(')[0].upper()} **")
                
                for k, test in enumerate(benchmark, 1):
                    if eval(test):
                        print(f'Test {k} réussi :  {test} ')
                    else:
                        print(f'Test {k} échoué :  {test} ')
                        failed += 1

                if not failed :
                    print(f"Bravo vous avez réussi tous les tests {choice(success_smb)}")
                else :
                    if failed == 1 : msg = f"{failed} test a échoué. "
                    else : msg = f"{failed} tests ont échoué. "
                    print(msg + f"Reprenez votre code {choice(fail_smb)}")
                    global_failed += 1
            return global_failed
        `);

        let output = await pyodide.runPythonAsync(test_code+"\ntest_unitaire(benchmark)");    // Running the code OUTPUT
        var stdout = pyodide.runPython("__sys__.stdout.getvalue()")  // Catching and redirecting the output
        elementCompteur = document.getElementById("test_term_editor_"+id_editor)
        while (elementCompteur.className !== "compteur") {
            elementCompteur = elementCompteur.nextElementSibling
        }
        if (output === 0) {
            dict[id_editor] = nAttempts
        } else {
            dict[id_editor] = 1 + (id_editor in dict ? dict[id_editor] : 0)
        }
        elementCompteur.textContent = Math.max(0,nAttempts-dict[id_editor])+"/5"

        if (dict[id_editor] === nAttempts) {
        let correctionExists = $('#corr_content_editor_'+id_editor).text()  // Extracting url from the div before Ace layer
        if (correctionExists !== "") {
            showCorrection('editor_'+id_editor);
        };
        }

        nlines = calcTermSize(stdout, mode)
        let editor = ace.edit("editor_"+id_editor);
        let stream = await editor.getSession().getValue();

        if(editor.session.getLength()<=nlines && mode==='v') {
            nslash = editor.session.getLength()- nlines + 3; // +3 takes into account shift and newlines
            for (var i = 0; i < nslash; i++) {
                stream += "\n"
            }
            editor.session.setValue(stream); // set value and reset undo history
        }
        $.terminal.active().echo(stdout); 

    } catch(err) {
        err = err.toString().split("\n").slice(-7).join("\n");
        nlines = calcTermSize(err, mode);
        $.terminal.active().echo(">>> Erreur de syntaxe !\n"+err)//.split("\n").slice(~~(nlines/2)).join("\n"));   // Would be nice to display only the last lines
      }
    } 


/* <div class="admonition info">
    <p class="admonition-title">paf</p>
    <div class="tabbed-set" data-tabs="1:3">
        <input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"></input>
        <label for="__tabbed_1_1">test</label>
        <div class="tabbed-content">blabla</div>

        <input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"></input>
        <label for="__tabbed_1_1">test2</label>
        <div class="tabbed-content">blabla2</div>
    </div>
</div> */

// $(document).ready(function() {
    // auto-load the Terminals but slows down A LOT the global loading of pyodide (not a good idea)
    // $('[id^=cons_]').each(function() {
    //     let number = this.id.split('_').pop();
    //     window.console_ready = pyterm('#cons_'+number);
    // });