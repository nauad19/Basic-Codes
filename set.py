if __name__ == "__main__":
    print("--- 4. Set Functions (Mutable, Unordered, Unique) ---")
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(f"Initial Set A: {set_a}")
    print(f"Initial Set B: {set_b}")

    set_a.add(10)
    print(f"1. Set A after add(10): {set_a}")

    set_a.remove(1)
    print(f"2. Set A after remove(1): {set_a}")

    set_union = set_a.union(set_b)
    print(f"3. union() of A and B: {set_union}")

    set_intersection = set_a.intersection(set_b)
    print(f"4. intersection() of A and B: {set_intersection}")

    subset_c = {3, 4, 5}
    is_subset = subset_c.issubset(set_union)
    print(f"5. issubset({{3, 4, 5}}) check: {is_subset}\n")
