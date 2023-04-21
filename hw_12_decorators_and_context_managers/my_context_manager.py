class MyContextManager:
    def __enter__(self):
        print("==========")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"\nError -> {exc_val}")
            print("==========")
            return True  # I don't understand why it's not working without return True
        else:
            print("==========")
