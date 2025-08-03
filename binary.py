def binarySearch(list, value):
    a = 0
    b = len(list) - 1

    while a <= b:
        mid = (a + b) // 2

        if list[mid] == value:
            print(f"Found at index {mid}")  
            return mid

        if list[mid] < value:
            a = mid + 1
        else:
            b = mid - 1

    print("Not found") 
    return -1

thelist = [ 2, 3, 7, 7, 11, 15, 25]
x = 11

result = binarySearch(thelist, x)
