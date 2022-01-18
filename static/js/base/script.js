const videoIntersect = new IntersectionObserver(entries => {
	entries.forEach(entry => {
		if (!entry.isIntersecting) {
			entry.target.pause()
		}
	})
}, {
	threshold: 1
})
$('#theme-toggler').on('click', () => {
	$('body').toggleClass('dark', 'light')
	if ($('body')[0].classList.contains('light'))
	{
		$('#theme-toggler').innerHTML('<i class="fa fa-moon-o"></i>')
		localStorage.setItem('theme', 'light')
		}
	else {
		$('#theme-toggler').innerHTML('<i class="fa fa-sun-o"></i>')
		
		localStorage.setItem('theme', 'dark')
	}
})
$(document).ready(loadPreference)

function loadPreference() {
	// theme preference
	let theme = localStorage.getItem('theme') ? localStorage.getItem('theme') : 'light'
	if (theme !== 'light') {
		$('#theme-toggler').innerHTML('<i class="fa fa-sun-o"></i>')
		$('body').toggleClass(theme,'light')
	}

}