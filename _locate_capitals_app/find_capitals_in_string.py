def capital_indexes(str): # define function called 'capital_indexes' with string param
    result=[] # define result variable to store detected capital letters
    for i, char in enumerate(str): # for loop to iterate over string characters 
        if char.isupper(): result.append(i) # test if the iterated character is equal to uppercase then print output
    return result # print result
capital_indexes("TEsT") # parse string, and call capital_indexes function