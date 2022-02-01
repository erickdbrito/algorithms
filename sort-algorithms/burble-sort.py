import random

# O(n**2)
def burble_sort(list_to_sort: list):
    list_lenght = len(list_to_sort)

    for i in range(list_lenght):
        for j in range(0, list_lenght - i - 1):

            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j + 1], list_to_sort[j]

    return list_to_sort

if __name__ == '__main__':
    list_size = int(input('Enter list size: '))

    list_to_sort = [random.randint(0,100) for i in range(list_size)]

    print (list_to_sort)

    ordered_list = burble_sort(list_to_sort)

    print (ordered_list)