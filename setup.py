from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setup(
    name="cron-expression-parser",
    version="0.0.1",
    author="Tobi Adeniyi",
    author_email="adeniyisoftware@gmail.com",
    description=(
        "This project is a Python-based cron expression parser "
        "that displays a human-readable representation of the "
        "resulting time that command will be run."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TobiAdeniyi/cron-expression-parser",
    project_urls={
        "Bug Tracker": "https://github.com/TobiAdeniyi/cron-expression-parser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "parse_cron_string = src.cli:main",
        ]
    }
)