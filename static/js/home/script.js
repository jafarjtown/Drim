addEventListener('click', 'button', (e)=> {
    qs('.modal-wrapper').style.display = 'flex'
    writeModal(e.target.innerText)
}, {}, qs('#share-btns'))

function writeModal(fo){
    if(String(fo) === 'write' ){
        const modal = qs('.modal')
        
    }
}

addEventListener('click', '#save-post', (e)=> {
    loading()
    const textarea = qs('textarea', qs('.write'))
    console.log(textarea.value)
    sleep(5000).then(()=> 
    loading('Done!', {success: true, target: '.modal-wrapper'})
    // qs('.loading-wrapper').style.display = 'none'
    )
})