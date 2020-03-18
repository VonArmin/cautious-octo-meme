import pickle
import sys

pkmn_team = []
try:
    file1 = open('pokemon_list', 'rb')
    dataset = pickle.load(file1)
    file1.close()
    file4 = open('move_types', 'rb')
    move_types = pickle.load(file4)
    file4.close()
    file2 = open('attack_chart', 'rb')
    attack_chart = pickle.load(file2)[0]
    file2.close()
    file3 = open('defend_chart', 'rb')
    defend_chart = pickle.load(file3)[0]
    file3.close()
except FileNotFoundError:
    pass


def main():
    try:
        load_data('last_team')
    except AttributeError:
        pass
    menu()


def menu():
    print("""
    1: create team
    2: teach moves
    3: defensive score
    4: offensive score
    5: super effectives
    6: immunities
    7: other commands
    9: save and exit
    """)
    check = int(input('select 1 : '))
    if check == 1:
        create_team()
    if check == 2:
        teach_moves()
    if check == 3:
        defensive_score()
    if check == 4:
        offensive_score()
    if check == 5:
        super_effectives()
    if check == 7:
        other_commands()
    if check == 9:
        save_data('last_team')


def create_team():
    global pkmn_team
    pkmn_team = []
    slot1 = Pokemon(input('pokemon 1 : '))
    slot2 = Pokemon(input('pokemon 2 : '))
    slot3 = Pokemon(input('pokemon 3 : '))
    slot4 = Pokemon(input('pokemon 4 : '))
    slot5 = Pokemon(input('pokemon 5 : '))
    slot6 = Pokemon(input('pokemon 6 : '))
    pkmn_team.append(slot1)
    pkmn_team.append(slot2)
    pkmn_team.append(slot3)
    pkmn_team.append(slot4)
    pkmn_team.append(slot5)
    pkmn_team.append(slot6)
    for slot in pkmn_team:
        print(slot.info())
    menu()


def teach_moves():
    global pkmn_team
    print("""
    0. menu
    1. teach moves
    2. modify moves
    """)
    check = int(input('make the choice : '))
    print(move_types)
    if check == 0:
        menu()
    if check == 1:
        for i, slot in enumerate(pkmn_team):
            print('teaching moves to {}\t'.format(slot.get_pokemon()))
            slot.set_move1(input('enter type of move 1 : '))
            slot.set_move2(input('enter type of move 2 : '))
            slot.set_move3(input('enter type of move 3 : '))
            slot.set_move4(input('enter type of move 4 : '))
    elif check == 2:
        for i, slot in enumerate(pkmn_team):
            print(i + 1, slot.get_pokemon())
        check = int(input('select pokemon : ')) - 1
        print('you are modifying moves of {}'.format(pkmn_team[check].get_pokemon()))
        pkmn_team[check].set_move1(input('enter type of move 1 : '))
        pkmn_team[check].set_move2(input('enter type of move 2 : '))
        pkmn_team[check].set_move3(input('enter type of move 3 : '))
        pkmn_team[check].set_move4(input('enter type of move 4 : '))
    menu()


def defensive_score():
    menu()


def offensive_score():
    attack_matchup = {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                      'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                      'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0}
    if input('whole team? y/n : ') == 'y':
        for pkmn in pkmn_team:
            attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn.get_move1()])
            attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn.get_move2()])
            attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn.get_move3()])
            attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn.get_move4()])

        print(attack_matchup)
        attack_matchup = {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0,
                          'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0,
                          'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0}
    if input('one pkmn? y/n : ') == 'y':
        print('1. {}, 2. {}, 3. {}, 4. {}, 5. {}, 6. {}'.format(pkmn_team[0].get_pokemon(), pkmn_team[1].get_pokemon(),
                                                                pkmn_team[2].get_pokemon(), pkmn_team[3].get_pokemon(),
                                                                pkmn_team[4].get_pokemon(), pkmn_team[5].get_pokemon()))
        slot = int(input('which slot? : ')) + 1
        attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn_team[slot].get_move1()])
        attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn_team[slot].get_move2()])
        attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn_team[slot].get_move3()])
        attack_matchup = merge_dictionaries(attack_matchup, attack_chart[pkmn_team[slot].get_move4()])
        print(attack_matchup)
    menu()


def super_effectives():
    pass


def other_commands():
    global pkmn_team
    print("""
    0. menu
    1. show ya moves
    2. show ya team
    3. save data
    4. load data
    5. quicksave
    6. input commands
    """)
    check = int(input('make the choice : '))
    if check == 0:
        menu()
    if check == 1:
        for i, slot in enumerate(pkmn_team):
            print('{}: {}'.format(i + 1, slot.moves()))
    if check == 2:
        for i, slot in enumerate(pkmn_team):
            print('slot {}: {}'.format(i + 1, slot.info()))
    if check == 3:
        save_data(input('enter name of your team : '))
    if check == 4:
        load_data(input('enter name of your team : '))
    if check == 5:
        save_data('last_team')
    if check == 6:
        input('enter command : ')
    menu()


def save_data(file_name):
    file = open(file_name, 'wb')
    pickle.dump(pkmn_team, file)
    print('saving successful')
    file.close()


def load_data(file_name):
    global pkmn_team
    try:
        file = open(file_name, 'rb')
        pkmn_team = pickle.load(file)
        print('loading successful')
        file.close()
    except FileNotFoundError:
        pass


def merge_dictionaries(dict1, dict2):
    merged_dictionary = {}

    for key in dict1:
        if key in dict2:
            new_value = dict1[key] + dict2[key]
        else:
            new_value = dict1[key]

        merged_dictionary[key] = new_value

    for key in dict2:
        if key not in merged_dictionary:
            merged_dictionary[key] = dict2[key]

    return merged_dictionary


class Pokemon:
    def __init__(self, i):
        self.pokemon, self.number, self.type1, self.type2 = 'null', 'null', 'null', 'null'
        self.set_move1(1)
        self.set_move2(1)
        self.set_move3(1)
        self.set_move4(1)
        self.dataset = dataset
        if i.isdigit():
            i = int(i)
        self.name_number(i)

    def name_number(self, i):
        for pokemon in dataset:
            if type(i) is int:
                if pokemon['number'] == i:
                    self.set_pokemon(pokemon['name'])
                    self.set_number(pokemon['number'])
                    self.set_type1(pokemon['type1'])
                    self.set_type2(pokemon['type2'])
            elif type(i) is str:
                if pokemon['name'].lower() == i.lower():
                    self.set_pokemon(pokemon['name'])
                    self.set_number(pokemon['number'])
                    self.set_type1(pokemon['type1'])
                    self.set_type2(pokemon['type2'])

    def set_pokemon(self, i):
        self.pokemon = i

    def set_number(self, i):
        self.number = i

    def get_pokemon(self):
        return self.pokemon

    def get_number(self):
        return self.number

    def set_type1(self, type):
        self.type1 = type

    def set_type2(self, type):
        self.type2 = type

    def get_type1(self):
        return self.type1

    def get_type2(self):
        return self.type2

    def set_move1(self, move):
        move = int(move)
        self.move1 = move_types[move]

    def set_move2(self, move):
        move = int(move)
        self.move2 = move_types[move]

    def set_move3(self, move):
        move = int(move)
        self.move3 = move_types[move]

    def set_move4(self, move):
        move = int(move)
        self.move4 = move_types[move]

    def get_move1(self):
        return self.move1

    def get_move2(self):
        return self.move2

    def get_move3(self):
        return self.move3

    def get_move4(self):
        return self.move4

    def info(self):
        return 'Pokemon : {}, number : {}, type : {}/{}'.format(self.pokemon, self.number, self.type1,
                                                                self.type2)

    def moves(self):
        return '{} knows {}, {}, {} and {} type moves'.format(self.pokemon, self.move1, self.move2, self.move3,
                                                              self.move4)


main()
