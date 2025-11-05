if __name__ == "__main__":
    print("List Functions")
    my_list = [10, 20, 30, 40, 20, 50]
    print(f"Initial List: {my_list}")

    my_list.append(60)
    print(f"1. append(60) result: {my_list}")

    my_list.insert(1, 15)
    print(f"2. insert(1, 15) result: {my_list}")

    removed_item = my_list.pop(0)
    print(f"3. pop(0) element: {removed_item}, New List: {my_list}")

    my_list.sort(reverse=True)
    print(f"4. sort(reverse=True) result: {my_list}")

    count_of_20 = my_list.count(20)
    print(f"5. count(20) value: {count_of_20}\n")
