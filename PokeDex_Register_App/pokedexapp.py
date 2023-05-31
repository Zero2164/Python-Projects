# ---------IMPORTED MODULES---------
import requests
import json
import shutil
import pokebase as pb
import os
import sys
from pathlib import Path

# ---------VARIABLES---------
# pokedex_name = input('\nPlease enter your Pokedex Name: ').capitalize()
pokedex_name = sys.argv[1].capitalize()
choose_a_pokemon = sys.argv[2].lower()


# ---------FUNCTIONS---------

def get_pokemon_types(chosen_pokemon):
    pokemon_types = []
    for type_name in chosen_pokemon.types:
        pokemon_types.append(str(type_name.type).upper())
    return ','.join(pokemon_types)


def get_pokemon_stats(chosen_pokemon):
    pokemon_stats = []
    for stat_name in chosen_pokemon.stats:
        pokemon_stats.append(
            ' '+str(stat_name.stat).capitalize() + ':'+str(stat_name.base_stat))
    return ','.join(pokemon_stats)


def get_pokemon_abilities(chosen_pokemon, type):
    pokemon_abilities = []
    pokemon_hidden_abilities = []
    for stat_name in chosen_pokemon.abilities:
        if stat_name.is_hidden:
            pokemon_hidden_abilities.append(
                str(stat_name.ability).capitalize())
            continue
        pokemon_abilities.append(str(stat_name.ability).capitalize())
    abil_hidden = ','.join(pokemon_hidden_abilities)
    abil_list = ','.join(pokemon_abilities)
    if type == 'ability':
        abilities_str = abil_list
        return abilities_str
    if type == 'hidden':
        if len(pokemon_hidden_abilities) > 0:
            abilities_str = abil_hidden
            return abilities_str
        else:
            return 'N/A'


def register_new_pokemon(registered_pokemon, chosen_pokemon, pokemon_id, pokemon_name, pokemon_img):
    p_img_fname = str(pokemon_name+'.png')
    img_file = Path(f'{pokedex_name}_PokeDex'f'/{pokemon_name}/'+p_img_fname)
    img_file.parent.mkdir(exist_ok=True, parents=True)
    pokemon_folder = str(
        f'{pokedex_name}_Pokedex'f'/{pokemon_name}/'+p_img_fname)
    registered_pokemon['POKEMON'].append({
        'PokeDex_ID': pokemon_id,
        'Name': pokemon_name,
        'Image': pokemon_folder,
        'Types': get_pokemon_types(chosen_pokemon),
        'Height': str(chosen_pokemon.height*10)+'cm',
        'Weight': str(chosen_pokemon.weight/10)+'kg',
        'BaseEXP': str(chosen_pokemon.base_experience)+'exp',
        'Stats': get_pokemon_stats(chosen_pokemon),
        'Abilities': get_pokemon_abilities(chosen_pokemon, 'ability'),
        'HiddenAbilities': get_pokemon_abilities(chosen_pokemon, 'hidden')
    })
    print('\n'+pokemon_name+' Registered to your PokeDex!!')
    print('Check out Pokedex Entry at:', f'{pokemon_folder}\n')
    out_file = Path(f'{pokedex_name}_Pokedex/'+'Registered_Pokemon.json')
    out_file.parent.mkdir(exist_ok=True, parents=True)
    with open(out_file, 'w') as output_fp:
        json.dump(registered_pokemon, output_fp, indent=3)

    res = requests.get(pokemon_img.url, stream=True)
    assert 200 <= res.status_code < 400, 'Failed to POST, error: \n'+res.text
    with open(img_file, 'wb') as out_img:
        shutil.copyfileobj(res.raw, out_img)


def console_output(pokemon_name, registered_pokemon, pokemon_exists, pokemon_index):
    if pokemon_exists:
        print('\nYOU HAVE ALREADY REGISTERED THIS POKEMON.\n')

    print(f'{ pokemon_name+" DETAILS ":-^22}\n')
    print('PokeDex_ID:',
          registered_pokemon['POKEMON'][pokemon_index]['PokeDex_ID'])
    print('Name:', registered_pokemon['POKEMON'][pokemon_index]['Name'])
    print('Types:', registered_pokemon['POKEMON'][pokemon_index]['Types'])
    print('Height:', registered_pokemon['POKEMON'][pokemon_index]['Height'])
    print('Weight:', registered_pokemon['POKEMON'][pokemon_index]['Weight'])
    print('Base EXP:', registered_pokemon['POKEMON'][pokemon_index]['BaseEXP'])
    print('Stats:', registered_pokemon['POKEMON'][pokemon_index]['Stats'])
    print('Abilities:',
          registered_pokemon['POKEMON'][pokemon_index]['Abilities'])
    print('Hidden Abilities:',
          registered_pokemon['POKEMON'][pokemon_index]['HiddenAbilities'])
    print('\n'f'{"":-^20}\n')


def pokedex_registrar(pokmon_name, registered_pokemon):
    chosen_pokemon = pb.pokemon(pokmon_name)
    pokemon_name = str(chosen_pokemon).upper()
    pokemon_id = pb.pokemon(pokmon_name).id
    pokemon_img = pb.SpriteResource('pokemon', pokemon_id)
    pokemon_exists = False
    pokemon_exists_id = 0
    if len(registered_pokemon['POKEMON']) == 0:
        register_new_pokemon(registered_pokemon, chosen_pokemon,
                             pokemon_id, pokemon_name, pokemon_img)
        console_output(pokemon_name, registered_pokemon, pokemon_exists, -1)

    else:
        for i, item in enumerate(registered_pokemon['POKEMON']):
            if pokemon_name == item['Name']:
                pokemon_exists_id = i
                pokemon_exists = True

        if pokemon_exists:
            console_output(pokemon_name, registered_pokemon,
                           pokemon_exists, pokemon_exists_id)

        else:
            register_new_pokemon(
                registered_pokemon, chosen_pokemon, pokemon_id, pokemon_name, pokemon_img)
            console_output(pokemon_name, registered_pokemon,
                           pokemon_exists, -1)


def open_pokedex(pokedex_name):
    selected_pokedex_file = Path(
        f'{pokedex_name}_Pokedex/'+'Registered_Pokemon.json')
    if not os.path.exists(f'{pokedex_name}_Pokedex/'+'Registered_Pokemon.json'):
        selected_pokedex_folder = Path(f'{pokedex_name}_Pokedex')/'test'
        selected_pokedex_folder.parent.mkdir(exist_ok=True, parents=True)
        selected_pokedex_file.touch(exist_ok=True)
        register_pokemon = {}
        register_pokemon['POKEMON'] = []
        with open(selected_pokedex_file, 'w') as output_fp:
            json.dump(register_pokemon, output_fp, indent=3)

    with open(selected_pokedex_file) as f:
        REGISTER = json.load(f)
    registered_pokemon = REGISTER
    pokedex_registrar(choose_a_pokemon, registered_pokemon)


open_pokedex(pokedex_name)
