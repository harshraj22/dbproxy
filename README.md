# DBProxy

An MCP Server to play with

## Generating a username which is valid as per Severence Corporation
- file `username_validator.py` represents a blackbox that contains rules about a valid username as per a secret organization `Severence Corporation`. It exposes a rest endpoint `/validate` to check if the provided username is valid. If not, it returns proper error message.
- Use VS Code Insider to access `Claude Sonnet 3.7` via github copilot as a MCP client
- Settings to register the MCP tool are:
```json
{
    "chat.mcp.discovery.enabled": true,
    "mcp": {

        "inputs": [],
        "servers": {
            "dbproxy": {
                "command": "/Users/harshraj22/.local/bin/uv",
                "args": [
                    "--directory",
                    "/Users/harshraj22/Desktop/lab/pro/claudeDir/dbProxy",
                    "run",
                    "dbproxy.py"
                ]
            },
            "username_validate": {
                "command": "/Users/harshraj22/.local/bin/uv",
                "args": [
                    "--directory",
                    "/Users/harshraj22/Desktop/lab/pro/claudeDir/dbProxy",
                    "run",
                    "username_generator.py"
                ]
            }
        }
    }
}
```

- Ask MCP Client to generate a valid username as per Severence Organization and learn from the error message.

https://github.com/user-attachments/assets/990377ea-0fde-4f4e-9b4f-0b3a420e3b30



## References
- https://modelcontextprotocol.io/quickstart/server

## License

MIT
