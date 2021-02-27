function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function responsive(x) {
  var cards = document.getElementsByClassName('card')
  for (i=0; i<cards.length; i++) {
    if (x.matches) { // If media query matches
      cards[i].classList.remove('col-6')
      // card[i].classList.add('col-12')
    } else {
      cards[i].classList.add('col-6')
      // card[i].classList.remove('col-12')
    }
  }
  
}

var x = window.matchMedia("(max-width: 700px)")
responsive(x) // Call listener function at run time
x.addListener(responsive) // Attach listener func