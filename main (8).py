def skip_integers(*args):
    for value in args:
        if isinstance(value, int):
            continue
        print(value)

# Example Usage:
skip_integers(10, "Hello", 3.14, [1, 2, 3], "World")
