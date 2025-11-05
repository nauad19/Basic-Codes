if __name__ == "__main__":
    print("--- 2. Tuple Functions (Immutable, Ordered) ---")
    my_tuple = ('apple', 'banana', 'cherry', 'apple', 'date')
    print(f"Initial Tuple: {my_tuple}")

    index_banana = my_tuple.index('banana')
    print(f"1. index('banana') position: {index_banana}")

    count_apple = my_tuple.count('apple')
    print(f"2. count('apple') value: {count_apple}")

    length = len(my_tuple)
    print(f"3. len() size: {length}")

    maximum = max(my_tuple)
    print(f"4. max() value: {maximum}")

    minimum = min(my_tuple)
    print(f"5. min() value: {minimum}\n")
