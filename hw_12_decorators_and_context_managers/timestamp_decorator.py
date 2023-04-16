import time
import sys

sys.path.append("/path/to/hw_12_decorators_and_context_managers")
from my_context_manager import MyContextManager


def time_decorator(times) -> object:
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = times
            while t > 0:
                print(f"Function  -> {func.__name__}\nCall time -> {time.asctime()}")
                t -= 1
            func(*args, **kwargs)

        return wrapper
    return decorator


@time_decorator(times=2)
def print_sum(a: int, b: int) -> int:
    z = a + b
    print(f"Sum is {z}")
    return z


@time_decorator(times=3)
def print_contact_phone(phone: int, name: str) -> dict:
    contact = {"phone": phone, "name": name}
    print(f"Contact is {contact}")
    return contact


with MyContextManager():
    print_sum(1, {})  # Error example

with MyContextManager():
    print_contact_phone(123456, "Valentine")
