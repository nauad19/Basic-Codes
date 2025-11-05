if __name__ == "__main__":
    print("--- 5. Dictionary Functions (Mutable, Key-Value Pairs) ---")
    my_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York',
        'job': 'Engineer'
    }
    print(f"Initial Dictionary: {my_dict}")

    keys_view = my_dict.keys()
    print(f"1. keys() view: {list(keys_view)}")

    values_view = my_dict.values()
    print(f"2. values() view: {list(values_view)}")

    items_view = my_dict.items()
    print(f"3. items() view: {list(items_view)}")

    age_value = my_dict.get('age')
    country_value = my_dict.get('country', 'Not Found')
    print(f"4a. get('age') value: {age_value}")
    print(f"4b. get('country', 'Not Found') value: {country_value}")

    removed_job = my_dict.pop('job')
    print(f"5. pop('job') removed: {removed_job}, New Dict: {my_dict}\n")
