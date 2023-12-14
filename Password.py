import string 
import random as rd


"""
# letters = string.ascii_lowercase
lowercases = list(string.ascii_lowercase)

# Get uppercase letters:
# uppercases = [letter.upper() for letter in letters] => for-loop increases complexity
# uppercases = list(letters.upper()) => method necessary to convert lowercases into uppercases
# Best: library calling
uppercases = list(string.ascii_uppercase) 

# Get digits:
# digits = [str(k) for k in range(10)] => casting and for-loop increase the complexity all the more
# Best: library calling
digits = list(string.digits)

# Problem: special characters missing
# Better: string.printable returns all characters needed
"""


class Password:

    def __init__(self, 
                 n = 16, 
                 lowercase_number = 4, 
                 uppercase_number = 4,
                 digit_number = 4,
                 symbol_number = 4):
        """
        n: password length
        """
        self.lowercases, self.uppercases, self.digits, self.symbols = self.get_characters()
        self.n = n
        self.lowercase_number = lowercase_number
        self.uppercase_number = uppercase_number
        self.digit_number = digit_number
        self.symbol_number = symbol_number


    
    def get_characters(self) -> list:
    
        printables = list(string.printable)
        digits, lowercases, uppercases, symbols = printables[:10], printables[10:36], printables[36:62], printables[62:-1]
        
        # Some elements cannot be used in passwords (e.g: ' ', '\t', '\n', '\r', '\x0b'). Let's remove them:
        # Unfortunatelly it seems you cannot remove multiple elements but using a for-loop
        symbols_to_remove = ['\\', '^', '`', '~', ' ', '\t', '\n', '\r', '\x0b']
        for symbol in symbols_to_remove:
            symbols.remove(symbol)
        
        return lowercases, uppercases, digits, symbols



    def generate(self):

        # Check that: self.lowercase_number + self.uppercase_number + self.digit_number + self.symbol_number <= self.n
        # 3 solutions:
        # if-else condition => function less readible
        # assert self.lowercase_number + self.uppercase_number + self.digit_number + self.symbol_number <= self.n
        # But this returns "AssertionError" which is not informative for the user
        # Implement an assertion check function
        
        try:
            self.check_assertion()
        except Exception:
            return self.check_assertion()


        self.types = [self.lowercases, self.uppercases, self.digits, self.symbols]        


        self.password = ""
        while len(self.password)<self.n:
            character = self.get_character()
            # The ideal password does not contain duplicates
            # If it does, we select another character randomly
            while character in self.password:
                character = self.get_character()
            self.password += character

        self.check_numbers()

        return self.password
        


    def check_type(self) -> Exception:
        if ( type(self.n) != int or type(self.lowercase_number) != int or type(self.uppercase_number) != int or type(self.digit_number) != int or type(self.symbol_number) != int):
            raise Exception("Parameters must be integers")
        


    def check_assertion(self) -> Exception:
        
        try:
            self.check_type()
        except Exception:
            return self.check_type()
        
        if self.n<8:
            raise Exception("The password must conatain at least 8 characters")
        if (self.lowercase_number<2 or self.uppercase_number<2 or self.digit_number<2 or self.digit_number<2):
            raise Exception("The password must contain at least 2 characters of each type (i.e lowercases, uppercases, digits, symbols)")
        if self.lowercase_number + self.uppercase_number + self.digit_number + self.symbol_number > self.n:
            raise Exception("The length of the password must be greater or equal to the number of desired characters")
        
        

    def get_character(self) -> str:
        # We select a random type between all possible types (i.e: lowercases, uppercases, digits, symbols)
        type = rd.choice(self.types)
        # From that type, we select a character randomly
        character = rd.choice(type)
        return character
    

    
    def check_numbers(self) -> None:

        lowercase_counter, uppercase_counter, digit_counter, symbol_counter = 0, 0, 0, 0
        for character in self.password:
            if character in self.lowercases:
                lowercase_counter += 1
            elif character in self.uppercases:
                uppercase_counter += 1
            elif character in self.digits:
                digit_counter += 1
            else:
                symbol_counter += 1
        
        if (lowercase_counter<self.lowercase_number or uppercase_counter<self.uppercase_number or digit_counter<self.digit_number or symbol_counter<self.symbol_number):
            self.password = self.generate()
        



# Test 1: check_type
p = Password("a", 2, 2, 2, 2)
print(p.generate())
# output:

# Test 2.1: check_assertion
# p = Password(2, 2, 2, 2, 3)
# print(p.generate())
# output: Exception: The password must conatain at least 8 characters

# Test 2.2: check_assertion
# p = Password(8, 1, 1, 1, 1)
# print(p.generate())
# output: Exception: The password must contain at least 2 characters of each type (i.e lowercases, uppercases, digits, symbols)
            
# Test 2.3: check_assertion
# p = Password(8, 2, 2, 2, 3)
# print(p.generate())
# output: Exception: The length of the password must be greater or equal to the number of desired characters

# Test 3: class
# p = Password()
# print(p.generate())
# output: e&/u:0+8XRI76Tlk

# Test 4: generate (and therefore: check_numbers), with self.lowercase_number + self.uppercase_number + self.digit_number + self.symbol_number == self.n
# p = Password(8, 2, 2, 2, 2)
# print(p.generate())
# output: cH?q>N32

# Test 5: generate (and therefore: check_numbers), with self.lowercase_number + self.uppercase_number + self.digit_number + self.symbol_number < self.n
# p = Password(8, 2, 2, 2, 1)
# print(p.generate())
# output: zlX0D9j} => 3 lowercases

# Test 6: long password
# p = Password(32, 8, 8, 8, 8)
# print(p.generate())
# output: L'r7f19z3mpN;X4kwH$8I6Cv-[](2:QE