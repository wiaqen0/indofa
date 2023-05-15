document.addEventListener('DOMContentLoaded', function() {
/* get the menu toggle button and the menu */
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');

/* add a click event listener to the menu toggle button */
menuToggle.addEventListener('click', () => {
  /* toggle the "active" class on the menu toggle button */
  menuToggle.classList.toggle('active');

  /* toggle the "active" class on the menu */
  menu.classList.toggle('active');
});
});