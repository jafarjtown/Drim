const videoIntersect = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        entry.target.pause();
      }
    });
  },
  {
    threshold: 1,
  }
);
$("#theme-toggler").on("click", () => {
  $("body").toggleClass("dark", "light");
  if ($("body")[0].classList.contains("light")) {
    $("#theme-toggler").innerHTML('<i class="fa fa-moon-o"></i>');
    localStorage.setItem("theme", "light");
  } else {
    $("#theme-toggler").innerHTML('<i class="fa fa-sun-o"></i>');

    localStorage.setItem("theme", "dark");
  }
});
$(document).ready(loadPreference);

function loadPreference() {
  // theme preference
  let theme = localStorage.getItem("theme")
if(theme) qs('body').classList.add(theme)
}
function addEventListener(
  type,
  selector,
  callback,
  options,
  parent = document
) {
  parent.addEventListener(
    type,
    (e) => {
      if (e.target.matches(selector)) callback(e);
    },
    options
  );
}
function qsa(selector, parent = document) {
  return [...parent.querySelectorAll(selector)];
}
function qs(selector, parent = document) {
  return parent.querySelector(selector);
}
function createElement(type, options = {}){
	const element = document.createElement(type)
	Object.entries(options).forEach(([key, value]) => {
		if(key === 'class'){
			element.classList.add(value)
			return
		}
		if(key === 'dataset'){
			Object.entries(value).forEach(([datakey, datavalue]) => {
				element.datasetp[datakey] = datavalue

			})
			return
		}
		if(key === 'text'){
			element.textContent = value
			return
		}
		element.setAttribute(keu, value)
	})
	return element
}

function sleep(duration){
	return new Promise(resolve => {
		setTimeout(resolve, duration)
	})
}

addEventListener('click', '#theme' , e => {
qs('body').classList.toggle('light')
let theme = localStorage.getItem("theme")
if(theme) localStorage.removeItem('theme')
else localStorage.setItem('theme', 'light')
},{}, qs('nav'))

addEventListener('click', '.modal-close', (e)=> {
    qs('.modal-wrapper').style.display = 'none'
}, {}, qs('.modal-wrapper'))

function loading(cb, opt = {}){
	qs('.loading-wrapper').style.display = 'flex'
	if(typeof cb === 'string'){
		qs('.loading-text').innerText = cb
		sleep(2000).then(()=> {qs('.loading-wrapper').style.display = 'none'
		qs('.loading-text').innerText = 'loading... please wait.'})
	}
	if(typeof cb === 'function') cb()
	if('success' in opt){
		if (opt.success) {
			sleep(2500).then(()=>
			qs(opt.target).style.display = 'none'
			)
		}
	}
	
}