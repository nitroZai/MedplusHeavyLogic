


# Binary Search on the Array


arr = [1,2,3,4,5,6,7,8,9,10]


low = 0
high = len(arr) - 1

target = 7

while low <= high: 
    
    mid = (low + high)//2

    if arr[mid] == target:
        print("The Target element is found!")
        break

    if arr[mid] > target:
        high = high + 1
    elif arr[mid] < target:
        low = low + 1
    