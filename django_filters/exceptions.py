from django.core.exceptions import FieldError


class FieldLookupError(FieldError):
    def __init__(self, model_field, lookup_expr):
        super().__init__(
            f"Unsupported lookup '{lookup_expr}' for field '{model_field}'."
        )
