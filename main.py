if __name__ =="__main__":
    # def calculate_list(lst):
    #     product = 1
    #     for num in lst:
    #         product *= num
    #     return product
    # numbers = [2, 3, 4, 5]
    # result = calculate_list(numbers)
    # print(result)
    # #exercise2
    # def minimumin_list(lst):
    #     return min(lst)
    # numbers = [8, 3, 10, 5, 2]
    # min_value = minimumin_list(numbers)
    # print(min_value)
    # #exercise3
    # def count_numbers(lst):
    #     def is_prime(n):
    #         if n <= 1:
    #             return False
    #         for i in range(2, int(n ** 0.5) + 1):
    #             if n % i == 0:
    #                 return False
    #         return True
    #     prime_count = 0
    #     for num in lst:
    #         if is_prime(num):
    #             prime_count += 1
    #     return prime_count
    # numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # count = count_numbers(numbers)
    # print(count)
    # #exercise 4
    # def remove_list(lst, element):
    #     count = lst.count(element)
    #     lst = [x for x in lst if x != element]
    #     return count
    # numbers = [2, 3, 4, 3, 5, 3, 6, 7, 3, 8]
    # removed_count = remove_list(numbers, 3)
    # print(removed_count)
    # print(numbers)
    # #exercise 5
    # def merge_lists(list1, list2):
    #     merged_list = list1 + list2
    #     return merged_list
    # list_a = [1, 2, 3]
    # list_b = [4, 5, 6]
    # merged = merge_lists(list_a, list_b)
    # print(merged)
    # #exercise6
    def calculate_elements(lst, power):
        powered_list = [num ** power for num in lst]
        return powered_list
    numbers = [2, 3, 4, 5]
    power = 2
    powered_result = calculate_elements(numbers, power)
    print(powered_result)