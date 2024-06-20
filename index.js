// docs: https://pokeapi.co/docs/v2
const url = 'https://pokeapi.co/api/v2/pokemon/';

function get_pokemon() {
    let dataContainer = document.getElementById("dataContainer");
    let card_holder = document.getElementById("card_holder");
    let debug = document.getElementById("debug");

    var text = document.getElementById("search").value;

    // delete old data
   card_holder.innerHTML = "";
    debug.innerHTML = "Debug:"

   // get json data from api!
   fetch(url + text)
        .then(response => {
            return response.json();

          })
          .then(response => {        
            // put data on page
            // first the type
            try {
                if (response.types[0].type.name == 'colorless' || response.types[0].type.name == 'normal' || response.types[0].type.name == 'stellar' || response.types[0].type.name == 'unknown') {
                    var card_type = 'gfx/colorless.png';
                } else if (response.types[0].type.name == 'dark' || response.types[0].type.name == 'ghost') {
                    var card_type = 'gfx/darkness.png';
                } else if (response.types[0].type.name == 'dragon' || response.types[0].type.name == 'flying') {
                    var card_type = 'gfx/dragon.png';
                } else if (response.types[0].type.name == 'fairy') {
                    var card_type = 'gfx/fairy.png';
                } else if (response.types[0].type.name == 'fighting' || response.types[0].type.name == 'ground' || response.types[0].type.name == 'rock') {
                    var card_type = 'gfx/fighting.png';
                } else if (response.types[0].type.name == 'fire'){
                    var card_type = 'gfx/fire.png';
                } else if (response.types[0].type.name == 'grass' || response.types[0].type.name == 'bug') {
                    var card_type = 'gfx/grass.png';
                } else if (response.types[0].type.name == 'lightning' || response.types[0].type.name == 'electric') {
                    var card_type = 'gfx/lightning.png';
                } else if (response.types[0].type.name == 'metal' || response.types[0].type.name == 'steel') {
                    var card_type = 'gfx/metal.png';
                } else if (response.types[0].type.name == 'psychic' || response.types[0].type.name == 'poison') {
                    var card_type = 'gfx/psychic.png';
                } else if (response.types[0].type.name == 'water' || response.types[0].type.name == 'ice') {
                    var card_type = 'gfx/water.png';
                }
            } catch (error) {
                debug.innerHTML = "Debug: " + error;
            }

            debug.innerHTML = card_type;

            let card = document.createElement('img');
            card.src = card_type;
            card_holder.appendChild(card);

            // then the info
            let name = document.createElement('h1');
            name.id = "pokemon_name";
            name.innerText = response['name'];
            card_holder.appendChild(name);

            let img = document.createElement('img');
            img.id = "pokemon_image";
            img.src = response['sprites']['other']['official-artwork']['front_default'];
            card_holder.appendChild(img);

            let hp = document.createElement('h1');
            hp.id = "pokemon_hp";
            hp.innerText = "HP: " + response.stats[0].base_stat;
            card_holder.appendChild(hp);

            let attack = document.createElement('h1');
            attack.id = "pokemon_attack";
            attack.innerText = "ATK: " + response.stats[1].base_stat;
            card_holder.appendChild(attack);
            
            let defense = document.createElement('h1');
            defense.id = "pokemon_defense";
            defense.innerText = "DEF: " + response.stats[2].base_stat;
            card_holder.appendChild(defense);
            
            let weight = document.createElement('h1');
            weight.id = "pokemon_weight";
            weight.innerText = "WT: " + response.weight;
            card_holder.appendChild(weight);
            
            let height = document.createElement('h1');
            height.id = "pokemon_height";
            height.innerText = "HT: " + response.height;
            card_holder.appendChild(height);
            
            let speed = document.createElement('h1');
            speed.id = "pokemon_speed";
            speed.innerText = "SPD: " + response.stats[5].base_stat;
            card_holder.appendChild(speed);
          })
          .catch(error => {
            console.log('Error:', error);
            debug.innerHTML = "Debug: " + error;
          });    
}



var searchbox = document.getElementById("search");

searchbox.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("search_button").click();
    }
});