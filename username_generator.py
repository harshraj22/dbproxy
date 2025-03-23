#!/usr/bin/env python3

import httpx
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("username_validator")

validation_calls = 0

async def validate_with_service(username: str) -> Dict[str, Any]:
    """
    Validates a username by calling the validation service
    
    Args:
        username: The username to validate
        
    Returns:
        Dict containing validation result with keys:
        - 'is_valid': Boolean indicating if the username is valid
        - 'errors': List of error messages if validation failed
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8000/validate",
                json={"username": username},
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
    
    except httpx.RequestError as e:
        return {
            "is_valid": False,
            "errors": [f"Error during validation request: {str(e)}"]
        }

@mcp.tool()
async def validate_username(username: str) -> Dict[str, Any]:
    """
    Validate a username for Severence Corporation by calling the username validation service.
    Severence Corporation has special rules for usernames.
    
    Args:
        username: The username to validate
        
    Returns:
        Dict containing validation result with keys:
        - 'is_valid': Boolean indicating if the username is valid
        - 'errors': List of error messages if validation failed
    """
    # Validate the username with the validation service
    validation_result = await validate_with_service(username)
    
    print(f"Validation called for username: {username} - Result: {validation_result}: -has been called {validation_calls} times")
    # Return the validation result
    return validation_result

# import asyncio

if __name__ == "__main__":
    # response_ = asyncio.run(validate_username("aabbccdde"))
    # print(response_)
    # Initialize and run the server
    mcp.run(transport='stdio')