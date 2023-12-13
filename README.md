# PasswordManager

For the moment, this repository contains 2 classes which help to generate and store strong passwords.

Here are the ideas of the Password class:
- a password is strong if it contains characters from different types (i.e: lowercases, uppercases, digits, symbols)
- for a same type, a password is strong if it doesn't contain a character multiple times. This is what the second while-loop in generate does: it checks if the selected character is already in the password. If it does, it picks another one, otherwise it adds it to the password
- before returning the password, the generate function checks if the contraints of the types are respected. If it does, the password is returned, otherwise another one is generated. Therefore, the generate function is a recursive function.
