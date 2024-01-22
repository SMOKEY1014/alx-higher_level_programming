#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            # Handle cases where my_list_1 or my_list_2 is too short
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Check if the element in my_list_1 is not an integer
            if not isinstance(my_list_1[i], int):
                print("wrong type")
                continue

            # Attempt division
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except (TypeError, ValueError):
                result = 0
                print("wrong type")

            # Append the result to the result_list
            result_list.append(result)
    except IndexError as e:
        print(e)
    finally:
        return result_list
