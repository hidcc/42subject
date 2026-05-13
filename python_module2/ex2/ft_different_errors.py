def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        _ = "abc" + 5


def test_error_type() -> None:
    for number in range (5):
        print(f"Testing operation {number}...")
        try:
            garden_operations(number)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo===")
    test_error_type()
    print()
    print("All error types tested successfully!")