# The same task, but in Python 3.

# The additional method: to fill a new array manually
def fill_array():
    array = []
    print('Please, fill in a desired array: ')
    while True:
        a = str(input("Enter an element (type 'Space' to break'): "))
        if a == ' ':
            break
        array.append(a)
    return array

# The basic method: gets an array as income and returns a new array
def three_or_less(array):
    triple_array = []
    for i in array:
        if len(i) <= 3:
            triple_array.append(i)
    return triple_array


if __name__ == '__main__':
    three_or_less(fill_array())
