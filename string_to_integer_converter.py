import csv_score_reader

def string_to_age_calculator(list):

    #converts the score value from string to integer to calculate with that
    for row in list:
        row[2] = int(row[2])

    print(list)
    return list

string_to_age_calculator(csv_score_reader.read_csv_score('lakers_heats_final.csv'))