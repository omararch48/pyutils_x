from typing import Callable, Any, Tuple, Optional


def exec_function(
    input_function: Callable[..., Any], 
    *args: Any, 
    **kwargs: Any
) -> Tuple[Optional[Any], Optional[Exception]]:
    """
    Executes a function with given arguments and captures any exception.

    Parameters
    ----------
    input_function : Callable[..., Any]
        The function to be executed.
    *args : Any
        Positional arguments to pass to the function.
    **kwargs : Any
        Keyword arguments to pass to the function. You can include
        'exec_function_error' to provide a default error value.

    Returns
    -------
    result : Any or None
        The result of the function if successful; otherwise, None.
    error : Exception or None
        The exception raised during execution, or a default error if provided.
        Returns None if execution was successful.

    Examples
    --------
    >>> def divide(a, b):
    ...     return a / b

    >>> result, error = exec_function(divide, 4, 2)
    >>> print(result)
    2.0

    >>> result, error = exec_function(divide, 4, 0)
    >>> print(error)
    division by zero
    """
    error = kwargs.pop('exec_function_error', None)

    try:
        return input_function(*args, **kwargs), None
    except Exception as e:
        if error is None:
            error = e
        return None, error
