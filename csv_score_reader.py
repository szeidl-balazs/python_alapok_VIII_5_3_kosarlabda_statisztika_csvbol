import csv
import sys

def read_csv_score(file_name_1):

    score_list = []
  

    try:
        score_file = open(file_name_1)        

        try:
            score_content = csv.reader(score_file)
            
            for row in score_content:
                score_list.append(row)

        finally:
            score_file.close()
           
    except OSError:
        sys.exit('Hibás file név!')

    else:
        print(score_list)
        return score_list
    
read_csv_score('lakers_heats_final.csv')