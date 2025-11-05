if __name__ == "__main__":
    print("--- 3. String Functions (Immutable, Sequence of Chars) ---")
    my_string = "   Hello World! PyThon is Fun.   "
    print(f"Initial String: '{my_string}'")

    stripped_string = my_string.strip()
    print(f"1. strip() result: '{stripped_string}'")

    upper_string = stripped_string.upper()
    print(f"2. upper() result: {upper_string}")

    replaced_string = stripped_string.replace('Fun', 'Awesome')
    print(f"3. replace('Fun', 'Awesome') result: {replaced_string}")

    word_list = stripped_string.split(' ')
    print(f"4. split(' ') list: {word_list}")

    starts_with_hello = stripped_string.startswith('Hello')
    print(f"5. startswith('Hello') check: {starts_with_hello}\n")
