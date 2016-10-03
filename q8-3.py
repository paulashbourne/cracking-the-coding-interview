def findMagicIndex(array, offset = 0):
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return offset if array[0] == offset else None
    n = len(array)
    mid = n / 2
    if array[mid] == offset + mid:
        return offset + mid
    elif array[mid] < offset + mid:
        # Solution cannot exist on the left side
        return findMagicIndex(array[mid+1:], offset + mid + 1)
    else:
        return findMagicIndex(array[:mid], offset)

def test1():
    return findMagicIndex([-10, -5, -1, 1, 2, 3, 4, 7, 9, 12, 13])

def main():
    print test1()

if __name__ == "__main__":
    main()
