'''
Function to get index of any number in list of lists
'''
def get_cart_index(list, quary):
    index = " "
    # check length of list
    length_list = len(list)
    # check if list is not empty
    if length_list > 0:
        for cart in list:
            # check in query is exists more than one time
            if list.count(quary) > 1:
                list_duplicate =[]
                for i in range(length_list):
                    if list[i] == quary:
                        list_duplicate.append(i)
                index = f"{quary} is exists at indexs{list_duplicate}"
                
            elif list.count(quary) == 1:
                if cart == quary:
                    index = list.index(cart) 
            # check of card not found
            else:
                index= f"{quary} not found in this list"    
        return index
    else:
        return("list is empty")
