from genericpath import isdir, isfile
import os
import string

def files_tab(path: string):
    print ([file if os.path.isfile(path + "\\" + file) else files_tab(path + "\\" + file) if os.path.isdir(path + "\\" + file) else None for file in os.listdir(path)])

files_tab("D:\\")

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    count1 = 0
    count2 = 0
    k = 0

    while count1 < len(left_arr) and count2 < len(right_arr):
        if left_arr[count1] < right_arr[count2]:
            arr[k] = left_arr[count1]
            count1+=1
        else:
            arr[k] = right_arr[count2]
            count2+=1
    
    while count1 < len(left_arr):
        arr[k] = left_arr[count1]
        count1+=1
        k+=1

    while count2 < len(right_arr):
        arr[k] = left_arr[count2]
        count2+=1
        k+=1

