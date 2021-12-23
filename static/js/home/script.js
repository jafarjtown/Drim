// let nextPage = 'start'
// let allPost = []
// let friends = []
const username = JSON.parse(document.querySelector('#username').textContent)
// async function getAllPost(link) {
//     const postWrapper = document.querySelector("#posts_wrapper");
//     let posts__ldb = localStorage.getItem("posts__ldb");
//     if (posts__ldb !== undefined) allPost = JSON.parse(posts__ldb);
//     const addToDom = () => {
//         postWrapper.innerHTML = "";

//         let posts = []
        
//         allPost &&
//             allPost.forEach((post) => {
//                     posts.push(`<div class="post">
//                     <div class="post_header">
//                         <div class="post_header_user">
//                             ${post.author.avatar ? `<img src='${post.author.avatar}' class='user_avatar' />` : `
//                             <div class='user_avatar'>
                                
//                             </div>
//                             `}
//                             <div class='p'>
//                             <p>${post.author.first_name} ${post.author.last_name}</p>
//                             </div>
//                             ${post.group !== null ?
//                         `<a href="groups/${post.group.id}" class='post_group_link'>${post.group.name}</a>` : ''}
//                         <div class='post_settings'>
//                         ${
//                             username === post.author.username ? `<a href='/'><i class='fa fa-edit'></i></a>
//                         <a href='/'><i class='fa fa-dot-circle-o'></i></a>` : ''
//                         }
//                         </div>
//                         </div>
//                     </div>
        
//                     <div class="post_body">
//                     ${post.files.length > 0 ? ViewFile(post.files, post.id) : " "}
//                         <div class="post_text">
                           
//                             ${post?.status && (post.status)}
//                         </div>
//                     </div>
//                     <div class="post_info">
//                     <button onclick='likePost("${post.id}")'> ${post.likes.length} <i class='fa fa-thumbs-o-up'></i> </button>
//                     <a href="posts/comments/${post.id}">
//                         ${post.comments.length} <i class='fa fa-comments-o'></i> 
//                     </a>
//                     <button onclick="copyLink('posts/comments/${post.id}')"><i class='fa fa-share-square-o'></i> </button>
//                     </div>
//                 </div>
//             `)
//             });
//         let rand = Math.floor(Math.random() * posts.length)
//         posts.splice(rand, 0, friends)
//         posts.flat().forEach(item => postWrapper.innerHTML += item)
//     };
//     addToDom();
//     const fetchPost = async (link) => {
//         const data = await fetch(link, {
//             headers: {
//                 'Authorization': `Token ${token}`
//             }
//         });
//         const result = await data.json();
//         if (result.next !== null) {
//             nextPage = result.next
//         } else {
//             nextPage = 'start'
//         }
//         if (result.results.length > 0) {
//             allPost = []
//             for (post of result.results) {
//                 allPost.push(post)
//             }
//             localStorage.setItem("posts__ldb", JSON.stringify(result.results));

//             addToDom();
//         } else {
//             let loader = document.getElementById('loader')
//             loader.classList.remove('loading_post')
//             loader.classList.add('card')
//             loader.classList.add('m-2')
//             loader.classList.add('text-center')
//             loader.classList.add('p-2')
//             loader.innerHTML = `
//                 <h3>Welcome to sitename</h3>
//                 <p>follow people for busy feed</p>
//             `
//         }
//     }
//     if (link !== undefined || null) {
//         fetchPost(link)
//     } else {
//         fetchPost('posts/posts')
//     }
// }
// async function createNewPost() {
//     const text = document.querySelector("textarea").value;
//     const files = document.querySelector("[name='file']").files;
//     const username = "{{user}}";
//     const formData = new FormData();

//     formData.append("status", text);
//     console.log(files)

//     for (file of files) {

//         formData.append("files", file);
//     }
//     formData.append("author",   `${user}}`);
//     const data = {
//         text,
//         username,
//         files
//     };

//     await fetch("api/post/posts/", {
//         method: "POST",
//         body: formData,
//         headers: {
//             'Authorization': `Token ${token}`,
//         }
//     });
//     document.querySelector("textarea").value = ''
//     document.querySelector("[name='file']").value = null
//     toggles()
//     // getAllPost();
//     allPost = []
// }
// document.querySelector("#create_new_post").addEventListener("click", () => {
//     createNewPost();
// });
// getAllPost();
// const loader = document.querySelector('#loader')
// const toggles = () => {
//     let cp = document.querySelector("#create_new_post_div");
//     let pw = document.querySelector("#posts_wrapper");
//     cp.classList.toggle("d-none");
//     cp.classList.toggle('form-post')
//     pw.classList.toggle("d-none");
//     loader.classList.toggle('d-none')
//     // if (cp.classList.contains("d-none")) {
//     //     addPostBtn.textContent = "new post";
//     // } else addPostBtn.textContent = "close";
// }
// const addPostBtn = document.querySelector("#open_create_post_div");
// addPostBtn.addEventListener("click", () => {
//     toggles()
// });
// const isElementVisible = (elem) => {
//     let style = window.getComputedStyle(elem);
//     if (style.display === 'none') return false
//     if (style.visibility !== 'visible') return false
//     if (style.opacity < 0.1) return false
//     if (elem.offsetWidth + elem.offsetHeight + elem.getBoundingClientRect().height + elem.getBoundingClientRect()
//         .width === 0) return false
//     const elemCenter = {
//         x: elem.getBoundingClientRect().left + elem.offsetWidth / 2,
//         y: elem.getBoundingClientRect().top + elem.offsetHeight / 2
//     }
//     if (elemCenter.x < 0) return false
//     if (elemCenter.x > (document.documentElement.clientWidth || window.innerWidth)) return false
//     if (elemCenter.y < 0) return false
//     if (elemCenter.y > (document.documentElement.clientHeight || window.innerHeight)) return false

//     let pointContainer = document.elementFromPoint(elemCenter.x, elemCenter.y)
//     do {
//         if (pointContainer === elem) return true;
//     } while (pointContainer = pointContainer.parentNode);
//     return false
//     //elem.offsetParent === null
// }
// setInterval(() => {
//     if (isElementVisible(loader)) {
//         if (nextPage !== 'start') getAllPost(nextPage)
//     }
// }, 1000)
// const likePost = async (id) => {
//     const req = await fetch(`posts/likes/${id}`)
//     const res = await req.json()
//     getAllPost()
//     return true
// }

const photoClick = document.querySelector('#photo-click')

photoClick.addEventListener('click', ()=> document.querySelector('#photo').click())