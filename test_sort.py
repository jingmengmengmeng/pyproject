def bubble_sort(list):
    length = len(list)
    for i in range(0, length):
        for j in range(0, length-1-i):
            if list[j] >list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list




def select_sort(list):
    length=len(list)
    for i in range(0, length-1):
        for j in range(i+1, length):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def arr_sort(list_int):
    second = 0
    count = 0
    max = 0
    for i in list_int:
        if max <=i:
            max=i
    for k in list_int:
        if k != max and second <= k:
            second = k
    return second


    for j in list_int:
        if max == j:
            count = count+1

    return max, count



list = [10, 25, 33, 9, 66]
list_int = [1, 2, 4, 6, 9, 6, 9, 6]
print(arr_sort(list_int))

print(select_sort(list))

