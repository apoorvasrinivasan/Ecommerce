window.onscroll =()->
	console.log 'sssssr'
	if window.scrollY >10 
		document.getElementById('menuBar').classList.add('sticky')
	else
		document.getElementById('menuBar').classList.remove('sticky')