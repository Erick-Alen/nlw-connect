from cerberus import Validator


def events_creator_validator(request: any):
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "schema": {
                    "nome": {"type": "string", "required": True, "empty": False},
                },
            }
        }
    )

    response = body_validator.validate(request.json)
    if response is False:
        raise Exception(body_validator.errors)
    # raise Exception(body_validator.errors) if response is False else None
