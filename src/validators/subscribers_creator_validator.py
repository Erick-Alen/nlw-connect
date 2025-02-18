from cerberus import Validator


def subscribers_creator_validator(request: any):
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "schema": {
                    "nome": {"type": "string", "required": True, "empty": False},
                    "email": {"type": "string", "required": True, "empty": False},
                    "link": {"type": "string", "required": False, "empty": False},
                    "evento_id": {"type": "int", "required": True, "empty": False},
                },
            }
        }
    )

    response = body_validator.validate(request.json)

    print(body_validator.errors) if response is False else None
