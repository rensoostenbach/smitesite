// Create a "close" button and append it to each list item
var myNodelist = document.getElementById("list").getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
	var span = document.createElement("SPAN");
	var txt = document.createTextNode("\u00D7");
	span.className = "close";
	span.appendChild(txt);
	myNodelist[i].appendChild(span);
}
// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
	close[i].onclick = function() {
		var div = this.parentElement;
		div.style.display = "none";
	}
}
// Create a new list item when clicking on the "Add" button
function newElement() {
	var li = document.createElement("li");
	var inputValue = document.getElementById("myInput").value;
	var t = document.createTextNode(inputValue);
	var h = document.createElement("button");
	var i = document.createElement("button");
	h.setAttribute("class", "downButton");
	i.setAttribute("class", "upButton");
	li.setAttribute("class", "liEllipsis");
	var x = document.createTextNode("Down");
	var y = document.createTextNode("Up");
	h.appendChild(x);
	i.appendChild(y);
	h.addEventListener ("click", moveDown);
	i.addEventListener ("click", moveUp);
	li.appendChild(h);
	li.appendChild(i);
	li.appendChild(t);
	if (inputValue === '') {
		alert("You must write something!");
	} else {
		document.getElementById("myUL").appendChild(li);
	}
	document.getElementById("myInput").value = "";
	var span = document.createElement("SPAN");
	var txt = document.createTextNode("\u00D7");
	span.className = "close";
	span.appendChild(txt);
	li.appendChild(span);
	for (i = 0; i < close.length; i++) {
		close[i].onclick = function() {
			var div = this.parentElement;
			div.style.display = "none";
		}
	}
}
// Move up/down for new list items
function moveUp() {
	var hook = $(this).closest('.liEllipsis').prev('.liEllipsis');
	if (hook.length) {
		var elementToMove = $(this).closest('.liEllipsis').detach();
		hook.before(elementToMove);
	}
}

function moveDown() {
	var hook = $(this).closest('.liEllipsis').next('.liEllipsis');
	if (hook.length) {
		var elementToMove = $(this).closest('.liEllipsis').detach();
		hook.after(elementToMove);
	}
}

// Move up/down for existing list items
$('.upButton').on('click', function() {
	var hook = $(this).closest('.liEllipsis').prev('.liEllipsis');
	if (hook.length) {
		var elementToMove = $(this).closest('.liEllipsis').detach();
		hook.before(elementToMove);
	}
});
$('.downButton').on('click', function() {
	var hook = $(this).closest('.liEllipsis').next('.liEllipsis');
	if (hook.length) {
		var elementToMove = $(this).closest('.liEllipsis').detach();
		hook.after(elementToMove);
	}
});
