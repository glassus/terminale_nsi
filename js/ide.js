$('[id^=editor_]').each(function() {
    let number = this.id.split('_').pop();
    //let url_pyfile = $('#'+this.id).text()  // Extracting url from the div before Ace layer
    let url_pyfile = $('#content_'+this.id).text()  // Extracting url from the div before Ace layer

    let id_editor = "editor_" + number
    function createACE(id_editor){
        ace.require("ace/ext/language_tools");
        var editor = ace.edit(id_editor, {
            theme: "ace/theme/tomorrow_night_bright",
            mode: "ace/mode/python",
            autoScrollEditorIntoView: true,
            maxLines: 30,
            minLines: 6,
            tabSize: 4,
            printMargin: false   // hide ugly margins...
        });
        editor.setOptions({
            enableBasicAutocompletion: true,
            enableSnippets: true,
            enableLiveAutocompletion: false
        });
        // Decode the backslashes into newlines for ACE editor from admonitions 
        // (<div> autocloses in an admonition) 
        editor.getSession().setValue(url_pyfile.replace(/backslash_newline/g, "\n"))  
    }
    window.IDE_ready = createACE(id_editor)           // Creating Ace Editor #id_editor

    if (url_pyfile === '') { 
        let editor = ace.edit(id_editor)
        editor.getSession().setValue('\n\n\n\n\n');  // Creates 6 empty lines for UX
    }
});

// Javascript to upload file from customized buttons
$('[id^=input_editor_]').each(function() {
    let number = this.id.split('_').pop();
    let id_editor = "editor_" + number
    document.getElementById('input_'+id_editor).addEventListener('change', function(e) {readFile(e, id_editor)}, false);
});

function readFile (evt, id_editor) {
    var files = evt.target.files;
    var file = files[0];
    var reader = new FileReader();
    var editor = ace.edit(id_editor);
    reader.onload = function(event) {
        editor.getSession().setValue(event.target.result);
    }
    reader.readAsText(file)
};

// turn off copy paste of code... A bit aggressive but necessary
// $(".highlight").bind('copy paste',function(e) { e.preventDefault(); return false; });


// Following blocks paint the IDE according to the mkdocs light/dark mode 
function paintACE(theme) {
    for (var editeur of document.querySelectorAll('div[id^="editor_"]')) {
        let editor = ace.edit(editeur.id);
        editor.setTheme(theme);
        editor.getSession().setMode("ace/mode/python");
    };
}

window.addEventListener('load', () => {
    var p = document.querySelector('label[for="__palette_2"]')
    console.log(p)
    if (p.hidden) {
        paintACE('ace/theme/crimson_editor')
    } else {
        paintACE('ace/theme/tomorrow_night_bright')
    }
});

var p2 = document.querySelector('input[id="__palette_2"]')
p2.addEventListener('click', () => { paintACE('ace/theme/crimson_editor') });

var p1 = document.querySelector('input[id="__palette_1"]')
p1.addEventListener('click', () => { paintACE('ace/theme/tomorrow_night_bright') });