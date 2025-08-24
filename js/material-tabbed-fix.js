/**FIX rendering troubles for sqlides that are in secondary tabs. */
(function(){

  const delayedRefreshFactory = (content) =>()=>{
    setTimeout(()=>{
      const cms = Object.values(content.getElementsByClassName("CodeMirror"))
      for(const elt of cms){
        if(!elt.CodeMirror || !elt.CodeMirror.refresh){
          continue
        }
        elt.CodeMirror.refresh()
      }
    })
  }

  const tabbed = Object.values(document.getElementsByClassName('tabbed-labels'))

  for(const tab of tabbed){
    const labels = Object.values(tab.getElementsByTagName("label"))
    for(const label of labels){
      const iLabel = [...label.parentElement.children].indexOf(label)
      const content = tab.parentElement.getElementsByClassName("tabbed-content")[0].children[iLabel]
      label.addEventListener("click", delayedRefreshFactory(content), {once:true})
    }
  }
})()