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
**init**.py
cron_parser.py
cron_response.py
**pycache**
**init**.cpython-312.pyc
cron_parser.cpython-312.pyc
cron_response.cpython-312.pyc
test
**init**.py
test_cron_parser.py
test_cron_response.py
**pycache**
**init**.cpython-312.pyc
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
4. Deactivate the virtual environment:

   - On Windows, macOS and Linux:

   ```sh
   deactivate
   ```

5. Install the required packages:
   - As a scrip:
     ```sh
     pip install -r requirements.txt
     ```
   - As an executable:
     ```sh
     pip install -e .
     ```

## Usage

To use the cron expression parser, you can run the `cron_parser.py` script located in the `src` directory. Here is an example:

```sh
python -m src.cli "*/15 0 1,15 * 1-5 /usr/bin/find"
```

If package was installed as an executable, we can instead run the application directly form the command line, as shown below:

```sh
parse_cron_string "*/15 0 1,15 * 1-5 /usr/bin/find"
```

## Running Tests

Tessting the code is done uising pythons `unittest` framework. The test files are located in the `test` directory. To run all test use the command shown below.

```sh
python -m unittest discover -s test
```

To run a specific test:

```sh
# for a specific class
python -m unittest test.<Test Class>

# for a specific method
python -m unittest test.<Test Class>.<Test Method>
```

## Project Details

- **[src/cli.py](src/cli.py)**: Contians the entry point for the _CLI_ tool.
- **[src/cron_parser.py](src/cron_parser.py)**: Contains the main logic for parsing cron expressions.
- **[src/cron_response.py](src/cron_response.py)**: Contains the logic for generating human-readable responses from parsed cron expressions.
- **[test/test_cron_parser.py](test/test_cron_parser.py)**: Contains unit tests for the cron parser.
- **[test/test_cron_response.py](test/test_cron_response.py)**: Contains unit tests for the cron response generator.

## TODO

The _TODO_ list shown below is in no paticular order.

- [ ] Add test cases for our entrypoint (**[src/cli](src/cli.py)**).
- [ ] Add the following parsin functionalities:
  - **[CronParser Module](src/cron_parser.py)**:
    - Usage of "W" and "L" in `day_of_month` field.
    - Usage of "W" and "#" in `day_of_week` field.
    - Update _Exception_ statements to be more helpful.
  - **[CronResponse Module](src/cron_response.py)**:
    - Ensure all fields fall within acceptable values (e.g., each day of week values falls within [1, 7]).
    - Update _Exception_ statements to be more helpful.
- [ ] Ensure executable works on all operating systems, see the **Troubleshoot 1: Cannot find the “download” command** section of [this](https://betterprogramming.pub/build-your-python-script-into-a-command-line-tool-f0817e7cebda) Medium post.
