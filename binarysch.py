def binarysch(list, low, high, item):
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            return binarysch(list, low, mid - 1, item)
        else:
            return binarysch(list, mid + 1, high, item)
    else:
        return -1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = int(input("Enter the item you want to search in the list: "))
result = binarysch(l, 0, len(l) - 1, i)
if result == -1:
    print("{} element is not found".format(i))
else:
    print("{} element is found at index {}".format(i, result))
