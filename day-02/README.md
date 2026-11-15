# Password Generator 🔐

## About the Project
This is a simple Password Generator built using Python.

The program generates random passwords based on the length selected by the user.

It uses Python's `secrets` module to generate secure random characters, making it more suitable for password generation than the `random` module.

## Features
- Generate random passwords.
- Include uppercase and lowercase letters.
- Include numbers and special characters.
- Allow users to choose password length.
- Validate user input.
- Accept password lengths between 6 and 20 characters.

## Technologies Used
- Python
- string module
- secrets module
- For Loop
- While Loop
- Input Validation

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python password_generator.py
```

5. Enter the desired password length when prompted.
6. The program will generate and display your password.

## Example

```text
How many characters do you want? 12

Your password is: A7#mK9!pQ2$x
```

*Note: The generated password will be different each time.*

## What I Learned
- How to import Python modules.
- How to use the string module.
- How to generate secure random characters using secrets.choice().
- How to use for and while loops.
- How to use break and continue.
- How to validate user input using isdigit().
- How to convert strings into integers using int().

## Author
Created as part of my 30 Days Python Projects Challenge.