import pickle


def main():
    file = open("pokemon dataset.txt").readlines()
    # read_file(file)
    # attack_chart()
    # defend_chart()
    move_types()

def read_file(file):
    pokemons = []
    for line in file:
        try:
            line = line.split('#')
            line1 = line[0]
            line2 = line[1]
            line1 = line1.split(' ')
            line2 = line2.split(' ')
            pokemons.append(create_entry(line1, line2))
        except IndexError:
            pass
    # print(pokemons[786])
    run_pickle(pokemons, 'pokemon_list')


def find_name(line):
    pokemon = ''
    if line[9].startswith('i'):
        pokemon = line[8][10:]
    if line[10].startswith('i'):
        pokemon = line[8][10:] + line[9]
    elif line[11].startswith('i'):
        pokemon = line[8][10:] + line[9] + line[10]
    return pokemon


def create_entry(line1, line2):
    print(line2)
    pokemon = {'name': find_name(line1), 'number': int(line2[0][:3]), 'type1': line2[3][12:].strip('"'),
               'type2': 'none'}
    if len(line2) == 11:
        pokemon = {'name': find_name(line1), 'number': int(line2[0][:3]), 'type1': line2[3][12:].strip('"'),
                   'type2': line2[8][12:].strip('"')}
    return pokemon


def attack_chart():
    attack_chart = [{'normal': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                                'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': -1, 'ghost': 0,
                                'dragon': 0, 'dark': 0, 'steel': -1, 'fairy': 0},
                     'fire': {'normal': 0, 'fire': -1, 'water': -1, 'grass': 1, 'electric': 0, 'ice': 1, 'fighting': 0,
                              'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 1, 'rock': -1, 'ghost': 0,
                              'dragon': -1, 'dark': 0, 'steel': 1, 'fairy': 0},
                     'water': {'normal': 0, 'fire': 1, 'water': -1, 'grass': -1, 'electric': 0, 'ice': 0, 'fighting': 0,
                               'poison': 0, 'ground': 1, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 1, 'ghost': 0,
                               'dragon': -1, 'dark': 0, 'steel': 0, 'fairy': 0},
                     'grass': {'normal': 0, 'fire': -1, 'water': 1, 'grass': -1, 'electric': 0, 'ice': 0, 'fighting': 0,
                               'poison': -1, 'ground': 1, 'flying': -1, 'psychic': 0, 'bug': -1, 'rock': 1, 'ghost': 0,
                               'dragon': -1, 'dark': 0, 'steel': -1, 'fairy': 0},
                     'electric': {'normal': 0, 'fire': 0, 'water': 1, 'grass': -1, 'electric': -1, 'ice': 0,
                                  'fighting': 0, 'poison': 0, 'ground': 0, 'flying': 1, 'psychic': 0, 'bug': 0,
                                  'rock': 0, 'ghost': 0, 'dragon': -1, 'dark': 0, 'steel': 0, 'fairy': 0},
                     'ice': {'normal': 0, 'fire': -1, 'water': -1, 'grass': 1, 'electric': 0, 'ice': -1, 'fighting': 0,
                             'poison': 0, 'ground': 1, 'flying': 1, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                             'dragon': 1, 'dark': 0, 'steel': 0, 'fairy': 0},
                     'fighting': {'normal': 1, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 1,
                                  'fighting': 0, 'poison': -1, 'ground': 0, 'flying': -1, 'psychic': -1, 'bug': -1,
                                  'rock': 1, 'ghost': 0, 'dragon': 0, 'dark': 1, 'steel': 1, 'fairy': -1},
                     'poison': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 1, 'electric': 0, 'ice': 0, 'fighting': 0,
                                'poison': -1, 'ground': -1, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': -1,
                                'ghost': -1, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 1},
                     'ground': {'normal': 0, 'fire': 1, 'water': 0, 'grass': -1, 'electric': 1, 'ice': 0, 'fighting': 0,
                                'poison': 1, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': -1, 'rock': 1, 'ghost': 0,
                                'dragon': 0, 'dark': 0, 'steel': 1, 'fairy': 0},
                     'flying': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                                'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                                'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
                     'psychic': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 1,
                                 'poison': 1, 'ground': 0, 'flying': 0, 'psychic': -1, 'bug': 0, 'rock': 0, 'ghost': 0,
                                 'dragon': 0, 'dark': 0, 'steel': -1, 'fairy': 0},
                     'bug': {'normal': 0, 'fire': -1, 'water': 0, 'grass': 1, 'electric': 0, 'ice': 0, 'fighting': -1,
                             'poison': -1, 'ground': 0, 'flying': -1, 'psychic': 1, 'bug': 0, 'rock': 0, 'ghost': -1,
                             'dragon': 0, 'dark': 1, 'steel': -1, 'fairy': -1},
                     'rock': {'normal': 0, 'fire': 1, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 1, 'fighting': -1,
                              'poison': 0, 'ground': -1, 'flying': 1, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                              'dragon': 0, 'dark': 0, 'steel': -1, 'fairy': 0},
                     'ghost': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                               'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 1, 'bug': 0, 'rock': 0, 'ghost': 1,
                               'dragon': 0, 'dark': -1, 'steel': -1, 'fairy': 0},
                     'dragon': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                                'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                                'dragon': 1, 'dark': 0, 'steel': -1, 'fairy': 0},
                     'dark': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': -1,
                              'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                              'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
                     'steel': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                               'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 1, 'bug': 0, 'rock': 0, 'ghost': 1,
                               'dragon': 0, 'dark': -1, 'steel': -1, 'fairy': -1},
                     'fairy': {'normal': 0, 'fire': -1, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 1,
                               'poison': -1, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                               'dragon': 1, 'dark': 1, 'steel': -1, 'fairy': 0}
                     }]
    run_pickle(attack_chart, 'attack_chart')


def defend_chart():
    defend_chart = [{'normal': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                                'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'fire': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                              'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                              'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'water': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                               'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                               'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'grass': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                               'poison': 1, 'ground': 1, 'flying': .1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                               'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'electric': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1,
                                  'fighting': 1,
                                  'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                  'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'ice': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                             'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                             'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'fighting': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1,
                                  'fighting': 1,
                                  'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                  'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'poison': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                                'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'ground': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                                'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'flying': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                                'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'psychic': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                                 'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                 'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'bug': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                             'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                             'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'rock': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                              'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                              'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'ghost': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                               'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                               'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'dragon': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                                'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                                'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'dark': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                              'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                              'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'steel': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                               'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                               'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1},
                     'fairy': {'normal': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'fighting': 1,
                               'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                               'dragon': 1, 'dark': 1, 'steel': 1, 'fairy': 1}
                     }]
    run_pickle(defend_chart, 'defend_chart')

def move_types():
    move_chart = {1: 'normal', 2: 'fire', 3: 'water', 4: 'grass', 5: 'electric', 6: 'ice', 7: 'fighting', 8: 'poison',
                  9: 'ground', 10: 'flying', 11: 'psychic', 12: 'bug', 13: 'rock', 14: 'ghost', 15: 'dragon', 16: 'dark',
                  17: 'steel', 18: 'fairy'}
    run_pickle(move_chart, 'move_types')

def run_pickle(list, file_name):
    file = open(file_name, 'wb')
    pickle.dump(list, file)
    file.close()


main()
