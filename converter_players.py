import csv_player_reader

#this function converts nested lists [[], []] to nested tuples ((), ())
def array_to_tuple_converter(list):

#define an empty array into which the sublist of the original list will be appended
    tuple_list = []

    #iterate on the sublists of the list and convert the sublists to tupple from [[], []] to [(),()]
    for sublist in list:
        tuple_list.append(tuple(sublist)) 
    
    #convert the outer original list with tuple sublists to tuple from [(),()] to ((),())
    list = tuple(tuple_list)


    print(list)

    return list

array_to_tuple_converter(csv_player_reader.read_csv_player('lakers_players.csv'))