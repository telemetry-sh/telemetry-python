# Telemetry-sh

A simple telemetry logging SDK for Python.

## Installation

You can install the package using pip:

```sh
pip install telemetry-sh
```

## Usage

### Initialization

First, you need to initialize the SDK with your API key.

```python
from telemetry import Telemetry

telemetry = Telemetry()
telemetry.init("your_api_key")
```

### Logging Data

You can log data to a specified table.

```python
data = {
    "field1": "value1",
    "field2": "value2"
}
response = telemetry.log("your_table_name", data)
print(response)
```

### Querying Data

You can query data using a custom query.

```python
query = "SELECT * FROM your_table_name WHERE field1 = 'value1'"
response = telemetry.query(query)
print(response)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
