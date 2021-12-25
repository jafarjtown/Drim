
const saveFile = (data, srcs, type) => {
	var file = new Blob([data], { type: type });
	let filename = `${new Date().getTime()}.${srcs}`;
	if (window.navigator.msSaverOrOpenBlob) {
		window.navigator.msSaverOrOpenBlob(file, filename);
	} else {
		var a = document.createElement("a"),
			url = URL.createObjectURL(file);
		a.href = url;
		a.download = filename;
		document.body.appendChild(a);
		a.click();
		setTimeout(function () {
			document.body.removeChild(a);
			window.URL.revokeObjectURL(url);
		}, 0);
	}
};
const getDate = (str) => {
	let days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
	let months = [
		"jan",
		"feb",
		"mar",
		"apr",
		"may",
		"jun",
		"jul",
		"aug",
		"sep",
		"oct",
		"nov",
		"dec",
	];
	let s = `${days[new Date(str).getDay()]} ${new Date(str).getDate()}/${
		months[new Date(str).getMonth()]
	}`;
	if (new Date(str).getFullYear() !== new Date().getFullYear()) {
		s = `${days[new Date(str).getDay()]} ${new Date(str).getDate()}/${
			months[new Date(str).getMonth()]
		}/${new Date(str).getFullYear()}`;
	}
	return s;
};
const copyLink = async (link) => {
	await window.navigator.clipboard
		.writeText(location.href + link)
		.then((d) => {
			alert("succesfully copied to clickboard");
		})
		.catch((e) => alert(e));
};
function id(name) {
	return document.getElementById(name)
}
function cl(name) {
	return document.querySelectorAll(`.${name}`)
}
function tg(name) {
	return document.querySelectorAll(name)
}
function nm(name) {
	return document.getElementsByName(`[name:${name}]`)
}

function manipulateVideo() {
	controls_wr = cl('video_controls')
	controls_wr.forEach(wr => {
		let btn = wr.children[0]
		wr.addEventListener('mouseover', function () {
			btn.style.display = 'flex'
		})
		wr.addEventListener('mouseout', function () {
			btn.style.display = 'none'
		})
	})
}
manipulateVideo()

const PlayVideo = (btn, vd) => {
	id(vd).nextElementSibling.style.backgroundColor='transparent'
	btn.style.display = 'none'
	if (id(vd).paused) {
		tg('video').forEach(v => {
			v.pause()
			let btn = v.nextElementSibling.children[0]
			btn.className = 'fa fa-3x fa-play'
			btn.display = 'flex'
		})
		id(vd).play()
		btn.className = 'fa fa-3x fa-pause'
	} else {
		id(vd).pause()
		btn.className = 'fa fa-3x fa-play'
	}
	
}

const seeMores = cl('seemore')

seeMores.forEach(seemore => {
	seemore.addEventListener('click', function (e) {
		let div = e.target.previousElementSibling
		div.classList.toggle('m500')
		console.log(div.classList)
		if (div.classList.contains('m500')) {
			seemore.textContent = 'see more'
		}else seemore.textContent = 'see less'
	})
})

const videos = tg('video')
const videoIntersect = new IntersectionObserver(entries => {
	entries.forEach(entry => {
		if (!entry.isIntersecting) {
			console.log(entry)
			entry.target.pause()
		}
	})
}, {
	threshold: 1
})

videos.forEach(video => {
	videoIntersect.observe(video)
})