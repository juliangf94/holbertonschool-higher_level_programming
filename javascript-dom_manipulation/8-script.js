document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElement = document.getElementById('hello');
  fetch(url)
    .then(response => response.json())
    .then((data) => {
      helloElement.textContent = data.hello;
    });
});
