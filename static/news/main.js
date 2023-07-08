

const navBurger = document.querySelector('.nav-bugger');
const navText = document.querySelector('.nav-text');


navBurger.addEventListener('click', ()=> {
  if (navText.style.display === 'none') {
    navText.style.display = 'block';
  } else {
    navText.style.display = 'none';
  }
})