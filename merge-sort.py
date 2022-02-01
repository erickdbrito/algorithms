from posixpath import lexists
import random

def merge_sort(list: list):
    list_lenght = len(list)

    if list_lenght > 1:
        middle = list_lenght // 2
        left = list[:middle]
        right = list[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k +=1
        
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list

if __name__ == '__main__':
    list_size = int(input('Enter list size: '))

    list_to_sort = [random.randint(0,100) for i in range(list_size)]

    print (list_to_sort)

    ordered_list = merge_sort(list_to_sort)

    print (ordered_list)