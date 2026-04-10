from exceptions import InvalidInputError

def validate_location(location: str) -> str:
    if not location or not location.strip():
        raise InvalidInputError("Location cannot be empty.")
    
    if len(location.strip()) < 2:
        raise InvalidInputError("Location must be at least 2 characters long.")
    
    return location.strip()