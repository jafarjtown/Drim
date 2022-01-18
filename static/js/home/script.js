

class Post extends Component{
    static get observedAttributes() {
        return ['likes']
    }
    get id() {
        return this.getAttribute('id')
    }
    get likes() {
        return this.getAttribute('likes')
    }
    set likes(v) {
        this.setAttribute('likes', v)
    }
    attributeChangedCallback(prop, oldV, newV) {
        if (this.observedAttributes[prop]) this.render()
        let button = this.shadow.querySelector(`#btn${this.id}`)
        button.addEventListener('click', this.like.bind(this))
    }
    
    connectedCallback() {
        this.render()
        let button = this.shadow.querySelector(`#btn${this.id}`)
        button.addEventListener('click', this.like.bind(this))
    }
    async like() {
        let req = await fetch(`posts/likes/${this.id}`)
        let res = await req.json()
        this.likes = res.likes
    }
    render() {
        this.shadow.innerHTML = `
        <style>
        *{
            box-sizing:border-box;
            margin:  0;
        }
        .post{
            width: 95%;
            min-width: 95%;
            box-shadow: 0 0 4px 0px grey;
            border-radius: 5px;
            margin-bottom: 5px;
            background-color: white;
        }
        .files{
            width: 100%;
        }
        .post-header{
            width: 100%;
            padding: 5px 8px;
            display: flex;
            align-items: center;
        }
        .text{
            padding: 0 3px;
            white-space: pre-wrap;
        }
        .footer{
            display: flex;
            justify-content: space-between;
            padding: 2px 10px;
        }
        .footer a, .footer button{
            text-decoration: none;
            background-color: white;
            color: gray;
            border: none;
            outline: none;
            font-size: 20px;
        }
        </style>
        <div class='post'>
            <div class='post-header'>
            <slot name='avatar'></slot>
                <div>
                    <slot name='username'></slot>
                    <slot name='date'></slot>
                </div>
            </div>
           
            <div class'files'><slot class='img' name='files'/></div>
            <p class='text'><slot name='status'/></p>
            <div class='footer'>
            <button id='btn${this.id}' class='fa fa-home'>${this.likes} like</button>
            <a href=''><i class='fa fa-comments-o'></i> comments
            </a>
            <button>Share</button>
            </div>
        </div>
        `
    }
}

customElements.define('my-post', Post)
async function fetchPostData() { 
    const request = await fetch('/api/post/posts')
    const response = await request.json()
    let posts = response.results.map((post, index) => `<my-post id='id_${index}' post='${JSON.stringify(post)}' likes='${post.likes.length}'></my-post>`)
    for (let post of posts) {
        $('#posts')[0].innerHTML += post
    }
    
}

let videos = $('video')
        let vidObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => entry.target.pause())
        }, {
            threshold : 1
        })
        videos.forEach(vid => vidObs.observe(vid))

function playVideo(args) {
    console.log(args)
    let vid = document.getElementById(args)
    const playOrpaused = (vid) => {
        
        if (vid.paused) {
            vid.play()
        }
        else {
            vid.pause()
        }
    }
    playOrpaused(vid)
}
// fetchPostData()