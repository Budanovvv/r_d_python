def factorial(number: int) -> int:
    next_num = number - 1
    print(f"Next number - > {next_num}")

    if next_num == 0:
        return 1
    else:
        result = number * factorial(next_num)
        print(f"Next result - > {result}")
        return result


fact_from = 4
fact_res = factorial(fact_from)
print(f"Result of factorial from {fact_from} - > {fact_res}")
