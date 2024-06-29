# PasswordManager

This is a personal project, which I'd like to replicate in Java, JS and C++.

For the moment, this repository contains 2 classes which help to generate and store strong passwords.

Here are the ideas of the Password class:
- a password is strong if it contains characters from different types (i.e: lowercases, uppercases, digits, symbols)
- for a same type, a password is strong if it doesn't contain a character multiple times. The second while loop within the generate method checks if the selected character is already in the password. If it does, it picks another one, otherwise it adds it to the password
- before returning the password, the generate method checks if the number constraint is fulfilled. If it is, the password is returned, otherwise another one is generated. Therefore, generate is a recursive function. N.B: This might lead to memory issue, which can be fixed by implementing an iterative approach (not done yet).

For the moment, the Manager class is basic: some updates and improvements need be done.
In the end, the idea is to get a single password (generated thanks to the previous class) in order to access them all. This is also the opportunity to get more familiar with cybersecurity issues. 

Also, for each class, tests were performed in order to check the methods of the class. I let them in the code, so you are able to check by yourself.

Feel free to contact me if you have any recommandation!
