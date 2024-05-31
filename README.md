# Cron Expression Parser

This project is a Python-based cron expression parser. It allows you to parse cron expressions and get a human-readable response for the resulting time fields at which the command would be executed.

## Project Structure

```markdown
LICENSE
README.md
env
    pyvenv.cfg
    bin
        Activate.ps1
        activate
        activate.csh
        activate.fish
        pip
        pip3
        pip3.12
        python 2
        python3 2
        python3.12
    include
        python3.12
    lib
src
    __init__.py
    cron_parser.py
    cron_response.py
    __pycache__
        __init__.cpython-312.pyc
        cron_parser.cpython-312.pyc
        cron_response.cpython-312.pyc
test
    __init__.py
    test_cron_parser.py
    test_cron_response.py
    __pycache__
        __init__.cpython-312.pyc
        test_cron_parser.cpython-312.pyc
        test_cron_response.cpython-312.pyc
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/TobiAdeniyi/cron-expression-parser.git
    cd cron-expression-parser
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv env
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    pip install -e .
    ```

## Usage

To use the cron expression parser, you can run the `cron_parser.py` script located in the `src` directory. Here is an example:

```sh
python -m src.cli "*/15 0 1,15 * 1-5 /usr/bin/find" 
```

## Running Tests

To run the tests, you can use the `unittest` framework. The test files are located in the `test` directory.

```sh
python -m unittest discover -s test
```

## Project Details

- **src/cron_parser.py**: Contains the main logic for parsing cron expressions.
- **src/cron_response.py**: Contains the logic for generating human-readable responses from parsed cron expressions.
- **test/test_cron_parser.py**: Contains unit tests for the cron parser.
- **test/test_cron_response.py**: Contains unit tests for the cron response generator.