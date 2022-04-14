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
    ? localStorage.getItem("theme")
    : "light";
  if (theme !== "light") {
    $("#theme-toggler").innerHTML('<i class="fa fa-sun-o"></i>');
    $("body").toggleClass(theme, "light");
  }
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
			element.classlist.add(value)
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

console.log(qsa('a', qs('nav')))