def sum_array(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


def product_array(arr):
    sum = 1
    for i in range(len(arr)):
        sum *= arr[i]
    return sum


def main():
    input_str = input("enter list of numbers: ")
    num_list = [int(num) for num in input_str.split()]
    print(num_list)
    total1 = sum_array(num_list)
    print(sum_array(num_list))
    print(product_array(num_list))
main()
