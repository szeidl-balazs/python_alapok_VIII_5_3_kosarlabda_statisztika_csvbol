import csv
import sys

def read_csv_player(file_name_2):

    player_list = []

    try:
        player_file = open(file_name_2)

        try:
            player_content = csv.reader(player_file)

            for row in player_content:
                player_list.append(row)


        finally:
            player_file.close()
           

    except OSError:
        sys.exit('Hibás file név!')

    else:
        print(player_list)
        return player_list
    
read_csv_player('lakers_players.csv')