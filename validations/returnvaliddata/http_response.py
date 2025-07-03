from utils.constants.http_response import STATUS_CODES 


def validate_status_code(
        status_code: int,
        additional_validation: callable = None,
        *args,
        **kwargs
    ) -> int:
    """
    If you not set error 400, you have an error
    """
    valitadion = True
    if additional_validation:
        try:
            valitadion = additional_validation(status_code, *args, **kwargs)
        except:
            valitadion = False

    if status_code in STATUS_CODES and valitadion:
        return status_code

    return 400 