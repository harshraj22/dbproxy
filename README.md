# DBProxy

A lightweight database proxy module that provides connection pooling, query optimization, and a unified interface for different database backends.

## Features

- Connection management (connect, disconnect)
- Query execution with parameter binding
- Transaction handling (begin, commit, rollback)
- Connection pooling
- Support for multiple database backends (SQLite, MySQL, PostgreSQL)

## Usage

```python
from DBProxy import DBProxy

# Create a proxy for SQLite database
db = DBProxy(db_type="sqlite", connection_params={"database": "example.db"})

# Connect to the database
db.connect()

# Execute a sample query
results = db.execute_query("SELECT * FROM users WHERE age > ?", (18,))

# Disconnect from the database
db.disconnect()
```

## License

MIT
