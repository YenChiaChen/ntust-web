$(function() {
    var home = $('.home'),
        wrap = $('.wrap'),
        screenWidth = window.innerWidth,
        screenHeight = window.innerHeight,
        wrapWidth = (window.innerHeight / 1) * 2;

    home.height(screenHeight + 'px');
    wrap.width(wrapWidth + 'px');

    window.onresize = function() {

      screenWidth = document.body.clientWidth;
      screenHeight = document.body.clientHeight;
      wrapWidth = (screenHeight / 1) * 2;

      home.height(screenHeight + 'px');
      wrap.width(wrapWidth + 'px');
    }
})


var mobileMenu = document.getElementById("mobilemenu");
document.getElementById("navToggle").onclick = function() {
	myFunction()
};
function myFunction() {   
	mobileMenu.classList.toggle("active");
}
var navLink = document.querySelectorAll(".nav-link");
navLink.forEach(n => n.addEventListener("click", closeMenu));
function closeMenu() {
	mobileMenu.classList.remove("active");
}