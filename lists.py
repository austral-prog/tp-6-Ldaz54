def remove_elements(list_to_remove_elements):
    lonlist= len(list_to_remove_elements)
    if lonlist >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif lonlist < 6 and lonlist >4:    
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif lonlist <= 4 and lonlist > 0:
        del list_to_remove_elements[0]
    else:
        pass
    return list_to_remove_elements  
print   (remove_elements([]))

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements  # Remove this line and implement

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False 

def check_lists(list_to_compare1, list_to_compare2):
    
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        return  list_to_compare1[2] == list_to_compare2[2]
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    L1= list_of_lists_to_modify[0][:2]
    L2 = list_of_lists_to_modify[1][1:4]
    L3 = list_of_lists_to_modify[2] 
    L3= L3[-2:]
    return [L1, L2, L3]
