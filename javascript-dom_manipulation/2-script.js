const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', () => {
  header.classList.add('red');
});
