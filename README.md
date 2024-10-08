# Learn FAST Api

- This repository is used to learn fast api by its documentation

# [Introduction](https://fastapi.tiangolo.com/features/)

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.

- Fast to code: Increase the speed to develop features by about 200% to 300%. *

- Fewer bugs: Reduce about 40% of human (developer) induced errors. *

- Intuitive: Great editor support. Completion everywhere. Less time debugging.

- Easy: Designed to be easy to use and learn. Less time reading docs.

- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.

- Robust: Get production-ready code. With automatic interactive documentation.

- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

# Some features of FAST Api

- Editor support, including:
    - Completion.
    - Type checks.
    - Validation of data:
    - Automatic and clear errors when the data is invalid.
    - Validation even for deeply nested JSON objects.
- Conversion of input data: coming from the network to Python data and types. Reading from:
    - JSON.
    - Path parameters.
    - Query parameters.
    - Cookies.
    - Headers.
    - Forms.
    - Files.
- Conversion of output data: converting from Python data and types to network data (as JSON):
    - Convert Python types (str, int, float, bool, list, etc).
    - datetime objects.
    - UUID objects.
    - Database models...and many more.
- Automatic interactive API documentation, including 2 alternative user interfaces:
    - Swagger UI.
    - ReDoc.
- Security and Authentication
    - HTTP Basic
    - OAuth2 (also with JWT Tokens)
    - API keys in:
        - Headers
        - Query parameters
        - Cookies
- Dependency injection:
    - Even dependencies can have dependencies, creating a hierarchy or "graph" of dependencies.
    - All automatically handled by the framework.
    - All the dependencies can require data from requests and augment the path operation constraints and automatic documentation.
    - Automatic validation even for path operation parameters defined in dependencies.
    - Support for complex user authentication systems, database connections, etc.
    - No compromise with databases, frontends, etc. But easy integration with all of them.
- Unlimited "plug-ins"
- Starlette features
- Pydantic features