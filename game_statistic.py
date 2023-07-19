import converter_players
import csv_player_reader
import converter_scores
import csv_score_reader


lakers_players = converter_players.array_to_tuple_converter(csv_player_reader.read_csv_player('lakers_players.csv'))

lakers_final_game = converter_scores.array_to_tuple_converter(converter_scores.string_to_integer_calculator(csv_score_reader.read_csv_score('lakers_heats_final.csv')))


player_name = 'D. Green'
quarter = '1'
score_type = '3'

"""Converts name to jersey number:"""

def get_jersey_number(players, name):
    for player in players:
        if name in player:
            return player[2]

jersey_number = get_jersey_number(lakers_players, player_name)

"""Calculates the sum of scoures in a quarter:"""

def get_player_score_in_quarter(scores, quarter, jersey):
    
    sum = 0
    
    for score in scores:
        if quarter == score[1] and jersey == score[3]:
            sum += score[2]

    return sum

player_scores = get_player_score_in_quarter(lakers_final_game, quarter, jersey_number)


"""Counts the score_type in a quarter_"""

def get_score_type_count(scores, quarter, jersey, score_type):
    
    sum_of_count = []
    
    for score in scores:  
        if (quarter == score[1] and score_type == score[2] and jersey == score[3]):
            sum_of_count.append(score[2])
        

    return len(sum_of_count)

score_type_count = get_score_type_count(lakers_final_game, quarter, jersey_number, score_type)




def print_player_stat_in_quarter(name, quarter, player_scores, score_type, score_type_count):

    print(name + ' statisztikája a(z) ' + str(quarter) + '. negyedben:')
    if player_scores != 0:
        print('Elért pontok: ' + str(player_scores))
        print(str(score_type) + ' pontos dobások száma: ' + str(score_type_count))
    else:
        print('Nem ért el pontot a negyedben.')
    

print_player_stat_in_quarter(player_name, quarter, player_scores, score_type, score_type_count)