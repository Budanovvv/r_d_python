def fibonacci(first: int, second: int, quantity: int, counter=1) -> int:
    result = first + second
    print(f"{counter} result => {result}")

    if counter == quantity:
        return None

    counter = counter + 1

    fibonacci(second, result, quantity, counter)


fibonacci(first=1, second=6, quantity=15)

