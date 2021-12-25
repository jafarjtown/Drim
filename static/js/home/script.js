// let nextPage = 'start'
// let allPost = []
// let friends = []
const username = JSON.parse(document.querySelector('#username').textContent)
const photoClick = document.querySelector('#photo-click')
const fileClick = document.querySelector('#photo')
fileClick.addEventListener('change', function (e) {
    photoClick.innerHTML += ' <i class="fa fa-spinner"></i>'
    let t = setTimeout(function () {
        console.log(e.target.files)
        photoClick.innerHTML = `File X ${e.target.files.length}`
    }, 1000)
    
})
photoClick.addEventListener('click', ()=> document.querySelector('#photo').click())
