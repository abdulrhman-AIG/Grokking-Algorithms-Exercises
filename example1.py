names = ["Basel", "Ahmad", "Mohamad", "Yazan", "Samer", "Waad", "Oman"]
names.sort()
print(names)


def binarySerch(list, item):
    low = 0
    high = len(names) - 1
    while low <= high:
        mid = (low + high) // 2
        midd = list[mid]
        print(midd)
        if midd == item:
            return mid
        if midd < item:
            low = mid + 1

        else:
            high = mid - 1


y = binarySerch(names, "Oman")
print(names[y])
