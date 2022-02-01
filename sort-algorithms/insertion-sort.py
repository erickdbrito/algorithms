import random

def insertion_sort(list_to_order):
    
    for index in range(1, len(list_to_order)):
        current_value = list_to_order[index]
        current_index = index

        while current_index > 0 and list_to_order[current_index - 1] > current_value:
            list_to_order[current_index] = list_to_order[current_index - 1]
            current_index -= 1
        
        list_to_order[current_index] = current_value
    
    return list_to_order
    
if __name__ == '__main__':
    list_size = int(input('Enter list size: '))

    list_to_sort = [random.randint(0,100) for i in range(list_size)]

    print (list_to_sort)

    ordered_list = insertion_sort(list_to_sort)

    print (ordered_list)