# Day 02 - Password Generator 🔐

## About the Project

A secure password generator built with Python.

The program generates random passwords based on the length selected by the user.

It uses Python's built-in `secrets` module to generate cryptographically secure random characters, making it more suitable for password generation than the `random` module.

## Features

- Generate secure random passwords.
- Include uppercase and lowercase letters.
- Include numbers and special characters.
- Allow users to choose password length.
- Validate user input.
- Accept password lengths between 6 and 20 characters.

## Technologies Used

- Python 3
- `string` module
- `secrets` module
- For Loop
- While Loop
- Input Validation

## Requirements

- Python 3.x

## Project Structure

```text
day-02/
└── password_generator.py
```

## How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository or download the project.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python password_generator.py
```

5. Enter your desired password length when prompted.
6. The program will generate and display your password.

## Example

```text
How many characters do you want? 12

Your password is: A7#mK9!pQ2$x
```

*Note: The generated password will be different each time.*

## What I Learned

- How to import and use Python modules.
- How to use the `string` module.
- How to generate secure random characters using `secrets.choice()`.
- How to use `for` and `while` loops.
- How to use `break` and `continue`.
- How to validate user input using `isdigit()`.
- How to convert strings into integers using `int()`.

## Author

Sarah Othman

Part of my 30 Days Python Projects Challenge 🐍
