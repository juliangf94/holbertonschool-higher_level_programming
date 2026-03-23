const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterName = document.getElementById('character');

fetch(url)
  .then(response => response.json())
  .then(data => {
    characterName.textContent = data.name;
  });
