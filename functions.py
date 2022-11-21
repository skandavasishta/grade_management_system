def print_main_menu(menu):
    '''this function prints out the list with options for the program'''
    print(menu)
    
def get_list_avg(main_list):
    '''this function creates a new list from the list that it takes in from
    the parameter, making each element an average of each sublist from the
    original main list'''
    new_list = []
    if len(main_list) == 0:
        return new_list
    for sub_list in main_list:       
        if len(sub_list) == 0:
            avg = 0
        else:
            avg = sum(sub_list)/len(sub_list)
        new_list.append(avg)
    return new_list

def get_grades(info_list):
    '''this function returns a new list with just the grades extracted
    from the list'''
    new_list = []
    n = 0
    for dicts in range(len(info_list)):
        new_list.append(info_list[n]['grades'])
        n +=1
    return new_list
           
       

def get_total_grade(info_list, show_steps = False):
    '''this function returns a value that is the sum of the grades
    multiplied by their weights, but will return 0 if the list is
    empty'''
    avg_sum = 0
    only_grades = get_grades(info_list)
    avg_grades = get_list_avg(only_grades)
    for position, category in enumerate(info_list):
        grade = avg_grades[position]
        weight = info_list[position]['weight']
        category_grade = grade*(weight/100)
        avg_sum +=category_grade
        if show_steps:
            print(f"{info_list[position][0]} average {avg_sum:.2f}%", end =" ") # see the example in the instructions
            print(f"{grade} / {weight}")
    return avg_sum

def get_selection(action, suboptions):
    """
    displays submenu for user to choose from, asks user to select an
    option using the input() function, re-prints the submenu if an
    invalid option is given, prints the confirmation of the selection
    by retrieving the description of the option from the suboptions
    dictionary. returns: the option selection as an upper-case string
            (should be a valid key in the suboptions)
    """
    selection = None
    while selection not in suboptions:
        print(f"What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        selection = input("::: Enter your selection\n> ")
        selection = selection.upper() # to allow us to input lower- or upper-case letters
    print(f"You selected {selection} to",
          f"{action.lower()} {suboptions[selection].lower()}.")
    return selection


def print_grade_info(info_list, show_grades = True):
    """this function prints out the category, weight, and/or corresponing grades depending on
    user input"""
    n = 1
    for index, value in enumerate(info_list):
        print(f'{n} - {info_list[index]["category"]} (info_list[index]["weight"])')
        n+=1
        if show_grades == True:
            if len[value] != 0:
                print(value)
                print('---')
            else:
                print('---')
        else:
            continue

def is_num(val):
    """this function determines if a number, inputed as a string,
    is actually a digit or not"""
    num_set = {'0','1','2','3','4','5','6','7','8','9','.'}
    dec_count = 0 
    if type(val) == str:
        for element in range(len(val)):
            if '0' <= val[element] <= '9':
                continue
            elif val[element] == '.':
                dec_count +=1
                if dec_count > 1:
                    return False
                else:
                    continue
            else:
                return False
        else:
            return True
    else:
        return False


def is_num_str_list(main_list):
    """this function determines if each element in a list is a string
    """
    if len(main_list) == 0:
        return False
    for item in main_list:
        if type(item) != str:
            return False
        if is_num(item) == False:
            return False
    return True


def create_category(info_str):
    """this function allows the creation of a new category given
    an input of a string that is eventually made into a dictionary if
    validated"""
    new_list = info_str.split()
    new_dict = {}
    if len(new_list) != 2:
        return -2
    elif (len(new_list[0]) < 2) or (',' in new_list[0]):
        return -1
    elif is_num(new_list[1]) == False:
        return 0
    else:
        new_dict['category'] = new_list[0]
        new_dict['weight'] = float(new_list[1])
        new_dict['grades'] = []
        return new_dict
    

def is_valid_index(idx, in_list, start_idx = 0):
    """this function determines if a given index can be used for
    the given list"""
    if not((is_num(idx) == False)) or not((int(idx)<0)): 
        new_idx = int(idx) - start_idx
        if int(new_idx) + 1 <= len(in_list):
            return True
        else:
            return False
    else:
        return False
                
                   
def update_category(info_list, idx, info_str):
    """this function allows the user to update a category given the
    main dictionary, an index, and a string that is inputted in the helper
    function create_category"""
    new_category = create_category(info_str)
    if new_category not in [0, -1, -2]:
        info_list[idx] = new_category
        return info_list[idx]
    else:
        return new_category
    
def delete_item(info_list, idx, start_idx=0):
    """this function allows the user to delete an item from the main
    dictionary"""
    if len(info_list) == 0:
        return 0
    elif is_valid_index(idx, info_list, start_idx) == False:
        return -1
    else:
        item = info_list[int(idx)]
        del info_list[int(idx)]
        return item
        
    
        



















    
    
        

