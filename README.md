# Enterprise FizzBuzz

This project provides an enterprise solution to the FizzBuzz problem, using proper design based on factories, registries, and singletons.

## Features
- Abstract Base Classes for FizzBuzz handlers
- Composite Pattern for managing multiple handlers
- Singleton Registry for handler instances
- Factory for creating handlers

## Installation

Setup a venv and use `pip` to install the package:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

## Running FizzBuzz

Activate the venv
```
source .venv/bin/activate
```
Run the cli invokation to see FizzBuzz in action:
```bash
fizzbuzz 100
```

## Running Tests

Run unit tests using unittest:

```bash
python -m unittest discover tests
```
