from PIL import Image, ImageDraw, ImageFont
import requests
from colorthief import ColorThief

url = 'https://pokeapi.co/api/v2/pokemon/'

def getInfo(call):
  r = requests.get(call)
  if r.status_code == 204:
    return {'name': 'Null'}
  return r.json()

def getImage(link):
   data = requests.get(link).content
   f = open('temp/pokepic.png', 'wb')
   f.write(data)
   f.close()

def get_pokemon():
   try:
      pokemon_search = input("Search for a pokemon: ")
      pokemon_info = getInfo(url + pokemon_search)
   except requests.exceptions.JSONDecodeError:
      print('Invalid pokemon')
      get_pokemon()

   if pokemon_info['types'][0]['type']['name'] == 'colorless' or pokemon_info['types'][0]['type']['name'] == 'normal' or pokemon_info['types'][0]['type']['name'] == 'stellar' or pokemon_info['types'][0]['type']['name'] == 'unknown':
      card_type = 'gfx/colorless.png'
   elif pokemon_info['types'][0]['type']['name'] == 'dark' or pokemon_info['types'][0]['type']['name'] == 'ghost':
      card_type = 'gfx/darkness.png'
   elif pokemon_info['types'][0]['type']['name'] == 'dragon' or pokemon_info['types'][0]['type']['name'] == 'flying':
      card_type = 'gfx/dragon.png'
   elif pokemon_info['types'][0]['type']['name'] == 'fairy':
      card_type = 'gfx/fairy.png'
   elif pokemon_info['types'][0]['type']['name'] == 'fighting' or pokemon_info['types'][0]['type']['name'] == 'ground' or pokemon_info['types'][0]['type']['name'] == 'rock':
      card_type = 'gfx/fighting.png'
   elif pokemon_info['types'][0]['type']['name'] == 'fire':
      card_type = 'gfx/fire.png'
   elif pokemon_info['types'][0]['type']['name'] == 'grass' or pokemon_info['types'][0]['type']['name'] == 'bug':
      card_type = 'gfx/grass.png'
   elif pokemon_info['types'][0]['type']['name'] == 'electric':
      card_type = 'gfx/electric.png'
   elif pokemon_info['types'][0]['type']['name'] == 'metal' or pokemon_info['types'][0]['type']['name'] == 'steel':
      card_type = 'gfx/metal.png'
   elif pokemon_info['types'][0]['type']['name'] == 'psychic' or pokemon_info['types'][0]['type']['name'] == 'poison':
      card_type = 'gfx/psychic.png'
   elif pokemon_info['types'][0]['type']['name'] == 'water' or pokemon_info['types'][0]['type']['name'] == 'ice':
      card_type = 'gfx/water.png'
    
   pokemon_name = pokemon_info['name']
   pokemon_image = pokemon_info['sprites']['other']['official-artwork']['front_default']
   pokemon_hp = "HP: " + str(pokemon_info['stats'][0]['base_stat'])
   pokemon_atk = "ATK: " + str(pokemon_info['stats'][1]['base_stat'])
   pokemon_def = "DEF: " + str(pokemon_info['stats'][2]['base_stat'])
   pokemon_wt = "WT: " + str(pokemon_info['weight'])
   pokemon_ht = "HT: " + str(pokemon_info['height'])
   pokemon_spd = "SPD: " + str(pokemon_info['stats'][5]['base_stat'])

   card = Image.open(card_type)
   font = ImageFont.truetype("Gill Sans Bold.otf", size=30)
   draw = ImageDraw.Draw(card)
   
   draw.text(xy=(105,22), text=f'{pokemon_name}', fill = (0,0,0), font = font)
   draw.text(xy=(30,400), text=f'{pokemon_hp}', fill = (0,0,0), font = font)
   draw.text(xy=(30,430), text=f'{pokemon_atk}', fill = (0,0,0), font = font)
   draw.text(xy=(30,460), text=f'{pokemon_def}', fill = (0,0,0), font = font)
   draw.text(xy=(230,400), text=f'{pokemon_wt}', fill = (0,0,0), font = font)
   draw.text(xy=(230,430), text=f'{pokemon_ht}', fill = (0,0,0), font = font)
   draw.text(xy=(230,460), text=f'{pokemon_spd}', fill = (0,0,0), font = font)
    
   getImage(pokemon_image)
   img = Image.open('temp/pokepic.png')
   img = img.resize((226,226))

   # get dominant color of pokepic
   color_thief = ColorThief('temp/pokepic.png')
   dominant_color = color_thief.get_color(quality=1)
   r, g, b = (dominant_color)
   color = Image.new('RGB',(347,230),(r,g,b))
   
   #replace transparent pixels with dominant color
   img = img.convert("RGBA")
   datas = img.getdata()

   newData = []
   for item in datas:
       if item[3] == 0:
           newData.append((r, g, b))
       else:
           newData.append(item)

   img.putdata(newData)
   img.save('temp\pokepic.png')
   
   card.paste(color, (37,61))
   card.paste(img, (90,63))

   card.save('temp/card_final.png')
   card.show()

   get_pokemon()

get_pokemon()