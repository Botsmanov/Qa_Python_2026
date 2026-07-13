def print_list_reverse(my_list):
    if my_list is None or len(my_list) == 0 :
        print('wrong list')

    else:
        print(my_list[::-1])
my_list = (1,2,3,4,5)
print_list_reverse(my_list)

#***********************************************

def is_valid_point(my_tuple,value1,value2):
    if  not my_tuple:
        return None
    if (
        isinstance(my_tuple,tuple)
            and len(my_tuple)==2
            and isinstance(value1, (int,float))
            and isinstance(value2, (int,float))):
            return True
    else:
        return False
c_tuple =([3,5])
print(is_valid_point(c_tuple,3,5))

#*******************************************************

def print_sublist_reverse(lst, start, finish):
    if not isinstance(lst,list):
        print("wrong args: not a list")
        return
    if not all (isinstance(x,(int,float)) for x in lst):
        print("wrong args")
        return
    if start<0 or finish>= len(lst) or start > finish:
        print("wrong args")
        return

    part_1 = lst[: start]
    part_2 = lst[start:finish+1][::-1]
    part_3 = lst[finish+1:]
    print(part_1+part_2+part_3)
my_lst = [10, 20,30,40 ,50, 60]
a_lst = [1,2,3,"a",5]
print_sublist_reverse( my_lst ,1,3)
print_sublist_reverse( a_lst ,1,3)


















# n_list=['cat' ,'dog' ,'bird', 'fish']
# print(n_list[::-1])
#
# def print_words_reverse(words):
#     if words is None or len(words)==0:
#         print("Wrong string")
#     else:
#         print(words[::-1])
#
# n_list=[]
# print_words_reverse(n_list)
#
#
# colors = ['red','blue' ,'green', 'blue', 'yellow']
# first_blue_index = colors.index ('blue')
# print(f"The first 'blue' is at position  {first_blue_index}")
#
# animals = ["cat", "dog","bird", "dog","fish"]
# first_dog_index = animals.index( 'dog')
# print(f"The first 'dog' is at position {first_dog_index} ")
# second_dog_index = animals.index("dog", first_dog_index +1)
# print(f"The second 'dog' is at position {second_dog_index} ")

