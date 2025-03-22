import string
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import random

import Profile

# Initialize FastMCP server
mcp = FastMCP("dbProxy")

@mcp.tool()
async def get_data_by_id(id: int) -> Any:
    """
        Get profile data by id for Severence Corporation.
    """
    async with httpx.AsyncClient() as client:
        # generate a fake profile data having id, name, and email
        # Generate random name
        first_names = ["John", "Jane", "Michael", "Emma", "David", "Sarah", "James", "Emily"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson"]
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        # Generate random email
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "company.com"]
        domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "company.com"]
        email = f"{username}@{random.choice(domains)}"
        
        response = Profile.Profile(name=name, email=email, id=str(id))
        return response
    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')