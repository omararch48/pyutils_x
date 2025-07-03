def execute_function(function, *args, **kwargs):
    try:
        execution = function(*args, **kwargs)
        error = None
    except Exception as e:
        # print(f"Error: {e}") # DEBUG
        execution = None
        error = e
    return execution, error
