def sum_array(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


def product_array(arr):
    total = 1
    for i in range(len(arr)):
        total *= arr[i]
    return total


def reverse_array(arr):
    array = [0] * len(arr)
    for i in range(len(arr)):
        array[i] = arr[len(arr) - 1 - i]
    return array


def main():
    input_str = input("enter list of numbers: ")
    num_list = [int(num) for num in input_str.split()]
    print(sum_array(num_list))
    print(product_array(num_list))
    print(reverse_array(num_list))
main()