import csv
import sys

def read_csv_score(file_name_1):

    score_list = []
  

    try:
        #open the csv file:
        score_file = open(file_name_1)        

        try:
            #score_content will store the content of the csv, the content is read in by the reader() function of csv module
            score_content = csv.reader(score_file)
            
            for row in score_content:
                 #append the csv each row to an array list []
                score_list.append(row)

            #delete the header of the list 
            del score_list[0]

            
        finally:
            score_file.close()
           
    except OSError:
        sys.exit('Hibás file név!')

    else:
        return score_list
    
