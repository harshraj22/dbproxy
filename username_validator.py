from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(title="Username Validator API")

class UsernameRequest(BaseModel):
    username: str

class ValidationResponse(BaseModel):
    is_valid: bool
    errors: List[str] = []

def validate_username(username: str) -> Dict:
    """
    Validates a username based on the following rules:
    - Must be palindromic
    - Must not contain the letter 'M' or 'm'
    - Must be exactly 8 characters long
    
    Returns a dictionary with validation results and error messages.
    """
    errors = []
    
    # Check length
    if len(username) != 8:
        errors.append("Username must be exactly 8 characters long")
    
    # Check for 'm' or 'm'
    elif 'n' in username.lower():
        errors.append("Username must not contain the letter 'M' or 'm'")
    
    # Check if palindromic
    elif username != username[::-1]:
        errors.append("Username must be palindromic (read the same forwards and backwards)")
    
    is_valid = len(errors) == 0
    
    return {
        "is_valid": is_valid,
        "errors": errors
    }

@app.post("/validate", response_model=ValidationResponse)
async def validate(request: UsernameRequest) -> ValidationResponse:
    """
    Validates a username against the required rules.
    
    Returns:
        ValidationResponse: Result of the validation with any error messages
    """
    result = validate_username(request.username)
    return ValidationResponse(**result)

@app.get("/")
async def root():
    """
    Root endpoint that returns information about the API
    """
    return {
        "message": "Username Validator API",
        "usage": "POST to /validate with a JSON body containing 'username'",
        "rules": [
            "Username must be palindromic",
            "Username must not contain the letter 'A' or 'a'",
            "Username must be exactly 9 characters long"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
