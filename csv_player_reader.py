import csv
import sys

def read_csv_player(file_name_2):

    player_list = []

    try:
        #open the csv file:
        player_file = open(file_name_2)

        try:
            #player_content will store the content of the csv, the content is read in by the reader() function of csv module
            player_content = csv.reader(player_file)

            #append the csv each row to an array list []
            for row in player_content:
                player_list.append(row)
                
            #delete the header of the list      
            del player_list[0]
            

        finally:
            player_file.close()
           

    except OSError:
        #if the input file name is wrong drops an error message
        sys.exit('Hibás file név!')

    else:        
        return player_list
    
