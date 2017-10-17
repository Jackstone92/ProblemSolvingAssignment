#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 08:26:08 2017

@author: jack stone
"""

# Example to run:
# "A table1 table2"
# "ON(A,table1) HEAVIER(table1,A) HEAVIER(table2,A) CLEAR(A) CLEAR(table2)"
# "CLEAR(table1) CLEAR(A)"


# Example of a Set-B) type problem
# CONTAINS CLEAR ERROR...
# Obj1 = "A B C T1 T2"
# S1 = "CLEAR(B) ON(B,C) ON(C,A) ON(A,T1) !CLEAR(T1)! CLEAR(T2) HEAVIER(B,A) HEAVIER(C,B) HEAVIER(T1,B) HEAVIER(T2,C)"
# G1 = "ON(A,B) ON(B,C) ON(C,T2)"

# Example of a Set-C) type problem
#
# Obj2 = "A B P1 P2 T1 T2 T3"
# S2 = "CLEAR(P2) ON(P2,A) ON(A,T2) ON(T2,B) CLEAR(T1) CLEAR(P1) HEAVIER(A,P2) HEAVIER(T2,A) HEAVIER(B,P2) HEAVIER(P1,P2) HEAVIER(T1,A) HEAVIER(P1,T2)"
# G2 = "ON(P2,A) ON(A,T2) ON(T2,P1)"


#########################################
#           List of Classes             #
#########################################        
class ON():
    """ ON Proposition """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.onArg1Dic = {}
        self.onArg2Dic = {}

    def display(self):
        print(self.x)
        print(self.y)
        # print("*" * 10)

    def assign_values(self):
        self.onArg1Dic = {"value": 10, "attribute": "is on top", "placeholder": self.x, "proposition": "on"}
        self.onArg2Dic = {"value": 1, "attribute": "is on bottom", "placeholder": self.y, "proposition": "on"}
        return self.onArg1Dic, self.onArg2Dic

    def on_test(self):
        if(self.onArg1Dic["value"] > self.onArg2Dic["value"]):
            # print(self.onArg1Dic["placeholder"] + " " + self.onArg1Dic["attribute"] + " and " + \
            #       self.onArg2Dic["placeholder"] + " " + self.onArg2Dic["attribute"])
            # print("*" * 10)
            return True
        else:
            return False

    def on_check(self, toCheckX, toCheckY):
        if self.x == toCheckX:
            if self.y == toCheckY:
                print('both on_check x and y passed')
                return True
            else:
                print('only on_check x passed, but y failed')
                return False
        else:
            print('both on_check failed')
            return False



class CLEAR():
    """ CLEAR Proposition """
    def __init__(self, x):
        self.x = x
        self.clearArgDic = {}

    def display(self):
        print(self.x)
        # print("*" * 10)

    def assign_values(self):
        self.clearArgDic = {"value": 0, "attribute": "is clear", "placeholder": self.x, "proposition": "clear"}
        return self.clearArgDic

    def clear_test(self):
        if self.clearArgDic["value"]:
        # print(self.clearArgDic["placeholder"] + " " + self.clearArgDic["attribute"])
        # print("*" * 10)
            return True
        else:
            return False

    def clear_check(self, toCheckX):
        if self.x == toCheckX:
            print('clear_check passed')
        else:
            print('clear_check failed')
            return False



class HEAVIER():
    """ HEAVIER Proposition """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heavierArg1Dic = {}
        self.heavierArg2Dic = {}

    def display(self):
        print(self.x)
        print(self.y)
        # print("*" * 10)

    def assign_values(self):
        self.heavierArg1Dic = {"value": 10, "attribute": "is heavier", "placeholder": self.x, "proposition": "heavier"}
        self.heavierArg2Dic = {"value": 1, "attribute": "is lighter", "placeholder": self.y, "proposition": "heavier"}
        return self.heavierArg1Dic, self.heavierArg2Dic

    def heavier_test(self):
        if(self.heavierArg1Dic["value"] > self.heavierArg2Dic["value"]):
            # print(self.heavierArg1Dic["placeholder"] + " " + self.heavierArg1Dic["attribute"] + " and " \
            #       + self.heavierArg2Dic["placeholder"] + " " + self.heavierArg2Dic["attribute"])
            # print("*" * 10)
            return True
        else:
            return False

    def heavier_check(self, toCheckX, toCheckY):
        if self.x == toCheckX:
            if self.y == toCheckY:
                print('both heavier_check x and y passed')
                return True
            else:
                print('only heavier_check x passed, but y failed')
                return False
        else:
            print('both heavier_check failed')
            return False

            
        
class ObjectClass():
    """Object Class that holds a name and a state"""
    def __init__(self, object_name, on, is_heavier_than):
        self.object_name = object_name
        self.setState(on, is_heavier_than)


    def setState(self, on, is_heavier_than):
        #on = what object is on top of it
        self.on = on
        #is_heavier_than = what item is current item heavier than
        self.is_heavier_than = is_heavier_than
        #print("Object created with name '",self.object_name,"' has the on state '",self.on,"' and is heavier than '",self.heavierThan,"'.")



class NodeClass():
    """Node Class that holds an array of objects and a string of moves """
    def __init__(self, object_array, string_of_moves):
        self.object_array = object_array
        self.string_of_moves = string_of_moves
        
        

#########################################
#          List of Functions            #
#########################################
def separate_string_by_comma(string):
    new_string_list = string.split(',')
    return new_string_list

def separate_string_by_object(string):
    new_string_list = string.split(')')
    return new_string_list

def separate_string_by_space(string):
    new_string_list = string.split(' ')
    return new_string_list

def remove(string, to_remove):
    """ Removes characters from strings """
    new_string = str("")
    i = 0
    while i < len(string):
        if string[i : i + len(to_remove)] == to_remove:
            i += len(to_remove)
        else:
            new_string += string[i]
            i += 1
    return new_string

def check_input_is_string(input):
    if type(input) != str:
        print("I'm sorry, please start again and make sure you enter a string!")

def check_if_quotations(string):
    """ Checks to see if any quotations and removes them """
    quote_found_double = False
    quote_found_single = False
    for i in range(len(string)):
        if string[i] == '"':
            quote_found_double = True
        if string[i] == "'":
            quote_found_single = True
    if quote_found_double == True:
        string = remove(string, '"')
    if quote_found_single == True:
        string = remove(string, "'")
    return string
        

def get_parameters_from_input_string(string):
    """ String manipulation to remove prefixes ON( and ) """
    parameter_array = []
    start_found = False
    item = str("")
    for i in range(len(string)):    
        if start_found == True and string[i] != "," and string[i] !=")":
            item += string[i]
        elif start_found == True and string[i] == ",":
            if item not in parameter_array:
                parameter_array.append(item)
            item = str("")
        elif start_found == True and string[i] == ")":
            start_found = False
            if item not in parameter_array:
                parameter_array.append(item)
            item = str("")
        # Start here and set start_found to True
        elif string[i] == "(":
            start_found = True
    return parameter_array

def get_clear_parameter(prefix):
    """ Used for CLEAR() """
    has_finished = False
    has_started = False
    parameter = str("")
    for char in prefix:
        if char == "("  and has_started == False:
            has_started = True
        elif char == ")" and has_started == True and has_finished == False:
            has_finished = True
            return parameter
        elif has_started == True and has_finished == False:
            parameter += char
            
def get_on_parameters(prefix):
    """ Used for ON() """
    first_has_finished = False
    second_has_finished = False
    first_has_started = False
    second_has_started = False
    on = str("")
    on_array = []
    for char in prefix:
        if char == "(":
            first_has_started = True
        elif char == ",":
            first_has_finished = True
            second_has_started = True
            on_array.append(on)
            on = str("")
        elif char == ")":
            second_has_finished = True
            on_array.append(on)
            return on_array
        elif (first_has_started == True and first_has_finished == False) or (second_has_started == True and second_has_finished == False):
            on += char

def get_heavier_parameters(prefix):
    """ Used for HEAVIER() """
    first_has_finished = False
    second_has_finished = False
    first_has_started = False
    second_has_started = False
    heavier = str("")
    heavier_array = []
    for char in prefix:
        if char == "(":
            first_has_started = True
        elif char == ",":
            first_has_finished = True
            second_has_started = True
            heavier_array.append(heavier)
            heavier = str("")
        elif char == ")":
            second_has_finished = True
            heavier_array.append(heavier)
            return heavier_array
        elif (first_has_started == True and first_has_finished == False) or (second_has_started == True and second_has_finished == False):
            heavier += char

def object_conversion(array):
    array_of_objects = []
    for i in range(len(array)):
        array_of_objects.append(ObjectClass(array[i], None, []))
    return array_of_objects

def s0_full_definition(array_with_prefixes, array2_with_prefixless_objects):
    """ Iterate through initial input array to find prefixes ON() etc and append them to a prefixes array of corresponding objects """
    prefixes = []
    prefix = str("")
    for i in range(len(array_with_prefixes)):
        is_end_of_word = False
        for char in array_with_prefixes[i]:
            if char == "(":
                prefixes.append(prefix)
                prefix = str("")
                is_end_of_word = True
            elif is_end_of_word == False:
                #concatinate prefix and char as long as it isn't the end of the word
                prefix += char
    
    #Iterate through the prefixes array and assign the corresponding objects to those prefixes
    for i in range(len(prefixes)):
        if prefixes[i] == "CLEAR":
            single_string = get_clear_parameter(array_with_prefixes[i])
            for i in range(len(array2_with_prefixless_objects)):
                if single_string == array2_with_prefixless_objects[i].object_name:
                    single_parameter = array2_with_prefixless_objects[i]
            single_parameter.on = None
            
        elif prefixes[i] == "ON":
            double_string = get_on_parameters(array_with_prefixes[i])
            parameters_array = []
            for i in range(len(array2_with_prefixless_objects)):
                if double_string[0] == array2_with_prefixless_objects[i].object_name:
                    parameters_array.append(array2_with_prefixless_objects[i])
                    
            for i in range(len(array2_with_prefixless_objects)):
                if double_string[1] == array2_with_prefixless_objects[i].object_name:
                    parameters_array.append(array2_with_prefixless_objects[i])
            parameters_array[1].on = parameters_array[0].object_name

        elif prefixes[i] == "HEAVIER":
            parameters_array = []
            double_string = get_heavier_parameters(array_with_prefixes[i])
            
            for i in range(len(array2_with_prefixless_objects)):
                if double_string[0] == array2_with_prefixless_objects[i].object_name:
                    parameters_array.append(array2_with_prefixless_objects[i])
                    
            for i in range(len(array2_with_prefixless_objects)):
                if double_string[1] == array2_with_prefixless_objects[i].object_name:
                    parameters_array.append(array2_with_prefixless_objects[i])
            parameters_array[0].is_heavier_than.append(parameters_array[1].object_name)

def check_if_is_Goal(arr1, arr2):
    solutionFound = True
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr2[i].object_name == arr1[j].object_name:
                if arr2[i].on != arr1[j].on:
                    solutionFound = False
    if solutionFound:
        #print("The goal state has been reached!")
        return True
    else:
        #print("The goal state has not been reached.")
        return False
        
def replicate(array_to_replicate):
    replica_array = []
    for i in range(len(array_to_replicate)):
        replica_array.append(ObjectClass(array_to_replicate[i].object_name, array_to_replicate[i].on, array_to_replicate[i].is_heavier_than))
    return replica_array

def move(x, y, z):
    #first, check if preconditions are true
    if y.on == x.object_name and z.on == None and x.on == None and x.object_name in z.is_heavier_than:
        #print("preconditions passed")
        #perform move
        #switch y and z
        z.on = x.object_name
        #delete y
        y.on = None
    else:
        print("Error")

###########################################################################################################################
###########################################################################################################################

# Ask User to input Objects, S0 and Goal, check if they are strings and remove any unnecessary quotations:
obj_input = input("Please enter the list of objects here: ")
check_input_is_string(obj_input)
obj_input = check_if_quotations(obj_input)

s0_input = input("Please enter your initial state here: ")
check_input_is_string(s0_input)
s0_input = check_if_quotations(s0_input)

g_input = input("Please enter your goal here: ")
check_input_is_string(g_input)
g_input = check_if_quotations(g_input)


#Commence string manipulation and conversion to objects
obj = separate_string_by_space(obj_input)
s0 = separate_string_by_space(s0_input)

individual_goals = separate_string_by_space(g_input)
goal_parameters = get_parameters_from_input_string(g_input)


#create ON() CLEAR() and HEAVIER() objects based on obj
on_item_list = []
clear_item_list = []
heavier_item_list = []

for text in s0:
    if "ON(" in text:
        #convert item to string to translate through and remove "ON("
        on_item = ''.join(text)
        on_less_item = remove(on_item, 'ON(')
        on_item_list.append(on_less_item)
#        print("on_item_list = ")
#        print(on_item_list)
    elif "CLEAR(" in text:
        clear_item = ''.join(text)
        #convert item to string to translate through and remove "CLEAR("
        clear_less_item = remove(clear_item, 'CLEAR(')
        clear_item_list.append(clear_less_item)
#        print("clear_item_list = ")
#        print(clear_item_list)
    elif "HEAVIER(" in text:
        heavier_item = ''.join(text)
        #convert item to string to translate through and remove "HEAVIER("
        heavier_less_item = remove(heavier_item, 'HEAVIER(')
        heavier_item_list.append(heavier_less_item)
#        print("heavier_item_list = ")
#        print(heavier_item_list)

on_objects = []
clear_objects = []
heavier_objects = []


#ON Conversion
# Obtain on arguments from on_item_list and create ON() class object
for item in on_item_list:
    separated_on_item = separate_string_by_comma(item)

    #returns true if item in separated_on_item[0] or separated_on_item[1] are found in obj
    if bool(filter(lambda item: any(x in item for x in separated_on_item[0]), obj)): #CONDITIONAL EXPRESSIONS CHECKED
        # print(separated_on_item[0] + " success")
        # print(separated_on_item[1] + " success")
        onArg1 = ''.join(separated_on_item[0])
        onArg2 = ''.join(separated_on_item[1])
        on_object = ON(onArg1, onArg2) #create as ON class object
        # on_object.display()
        on_objects.append([on_object.x, on_object.y])
    else:
        print("error ON bool")


#CLEAR Conversion
# Obtain on arguments from clear_item_list and create CLEAR() class object
for item in clear_item_list:
    separated_clear_item = separate_string_by_comma(item)
    #returns true if item in separated_clear_item[0] are found in obj ###
    if bool(filter(lambda item: any(x in item for x in separated_clear_item[0]), obj)):
        # print(separated_clear_item[0] + " success")
        clear_arg = ''.join(separated_clear_item[0])
        clear_object = CLEAR(clear_arg) #create as CLEAR class object#
        # clear_object.display()
        clear_objects.append([clear_object.x])
    else:
        print("error CLEAR bool")


#HEAVIER Conversion
# Obtain on method arguments from heavier_item_list and create HEAVIER() class object
for item in heavier_item_list:
    separated_heavier_item = separate_string_by_comma(item)

    # returns true if item in separated_heavier_item[0] or separated_heavier_item[1] are found in obj
    if bool(filter(lambda item: any(x in item for x in separated_heavier_item[0]), obj)) and \
        bool(filter(lambda item: any(x in item for x in separated_heavier_item[1]), obj)):
        # print(separated_heavier_item[0] + " success")
        # print(separated_heavier_item[1] + " success")
        heavier_arg1 = ''.join(separated_heavier_item[0])
        heavier_arg2 = ''.join(separated_heavier_item[1])

        heavier_object = HEAVIER(heavier_arg1, heavier_arg2) #create as HEAVIER class object#
        # heavier_object.display()
        heavier_objects.append([heavier_object.x, heavier_object.y])
    else:
        print("error HEAVIER bool")
#print("on_objects = ")
#print(on_objects)
#print("clear_objects = ")
#print(clear_objects)
#print("heavier_objects = ")
#print(heavier_objects)

#object conversion
s0_objects = object_conversion(obj);
#for i in range(len(s0_objects)):
#	print(s0_objects[i].object_name)

goalObjects = object_conversion(goal_parameters);
#for i in range(len(goalObjects)):
#	print(goalObjects[i].object_name)

s0_full_definition(s0, s0_objects)
s0_full_definition(individual_goals, goalObjects)

# Checks to see if move solution is found and if so, prints. If not, it carries on searching
check_if_is_Goal(s0_objects, goalObjects)
if check_if_is_Goal(s0_objects, goalObjects) == True:
    print("You don't need to make any moves because S0 is already the goal state.")
else:
    #Start Breadth-First Search:
    NODE = NodeClass(s0_objects, str(""))
    queue = []
    queue.append(NODE)

    is_goal = False
    correctNode = None
    
    while is_goal == False:
        for i in range(len(queue[0].object_array)):
            if queue[0].object_array[i].on == None:
                #to find the object queue[0] and determine objects_current_is_on_top_of
                for j in range(len(queue[0].object_array)):
                    if queue[0].object_array[j].on == queue[0].object_array[i].object_name:
                        objects_current_is_on_top_of = queue[0].object_array[j]
                        #print(objects_current_is_on_top_of.object_name)
                        break
                    
                for j in range(len(queue[0].object_array)):
                    if i != j:
                        #check everything is where it should be
                        if queue[0].object_array[i].object_name in queue[0].object_array[j].is_heavier_than and queue[0].object_array[i].on == None and queue[0].object_array[j].object_name != objects_current_is_on_top_of.object_name and queue[0].object_array[j].on == None:
                            #keep track of move solutions
                            move_solutions = "\nMove(" + queue[0].object_array[i].object_name + "," + objects_current_is_on_top_of.object_name + "," + queue[0].object_array[j].object_name + ")"
                            #create array_of_replicated_objects of current object_array
                            array_of_replicated_objects = replicate(queue[0].object_array)
                            #create new node consisting of array_of_replicated_objects and updated string_of_moves and move_solutions
                            NODE = NodeClass(array_of_replicated_objects, str(queue[0].string_of_moves) + str(move_solutions))
                            #prep
                            node_objects_current_is_on_top_of = None
                            #Find node_objects_current_is_on_top_of in NODE.arr
                            for k in range(len(NODE.object_array)):
                                if NODE.object_array[k].object_name == objects_current_is_on_top_of.object_name:
                                    node_objects_current_is_on_top_of = NODE.object_array[k]
                            #perform move() function
                            move(NODE.object_array[i], node_objects_current_is_on_top_of, NODE.object_array[j])
                            #final check
                            if check_if_is_Goal(NODE.object_array, goalObjects):
                                correctNode = NODE
                                is_goal = True;
                                break
                            else:
                                #if not goal, append NODE to queue and try again
                                queue.append(NODE)
        #extend queue accordingly
        queue = queue[1:len(queue)]
    print(correctNode.string_of_moves)

###########################################################################################################################
###########################################################################################################################
