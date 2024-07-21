try:
    # Code that may raise an exception
    result = some_function_that_might_raise_an_exception()
    print(result)
except Exception as e:
    # Handle the exception
    print(f"Error occurred: {e}")
    # Optionally, handle specific types of exceptions differently
    if isinstance(e, ValueError):
        # Handle ValueError
    elif isinstance(e, TypeError):
        # Handle TypeError
    else:
        # Handle other types of exceptions
