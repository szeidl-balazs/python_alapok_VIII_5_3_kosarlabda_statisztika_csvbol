

#this function converts string values to integer, only the score has to be converted to math calculations
def string_to_integer_converter(list):

    #converts the score value from string to integer to calculate with that
    for row in list:
        row[1] = int(row[1])
        row[2] = int(row[2])
        row[3] = int(row[3])
        
    return list
 

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

