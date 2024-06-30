import string 
import random as rd



class Password:



    def __init__(self, lowercase_number = 4, uppercase_number = 4, digit_number = 4, symbol_number = 4):

        self._lowercase_number = lowercase_number
        self._uppercase_number = uppercase_number
        self._digit_number = digit_number
        self._symbol_number = symbol_number
        self._length = self._lowercase_number + self._uppercase_number + self._digit_number + self._symbol_number

        self.__check_assertion()
 
        self._lowercases, self._uppercases, self._digits, self._symbols = self.__get_characters()
        self._types = [self._lowercases, self._uppercases, self._digits, self._symbols]



    def __check_assertion(self) -> ValueError:
        
        if ( type(self._lowercase_number) != int or type(self._uppercase_number) != int or type(self._digit_number) != int or type(self._symbol_number) != int):
            raise ValueError("Parameters must be integers")
            
        if self._length < 8:
            raise ValueError("The password must contain at least 8 characters")
        
        if (self._lowercase_number<2 or self._uppercase_number<2 or self._digit_number<2 or self._symbol_number<2):
            raise ValueError("The password must contain at least 2 characters of each type (i.e lowercases, uppercases, digits, symbols)")



    def __get_characters(self) -> list:
    
        printables = list(string.printable)
        digits, lowercases, uppercases, symbols = printables[:10], printables[10:36], printables[36:62], printables[62:-1]
        
        # Remove symbols that cannot be used in passwords
        symbols_to_remove = ['\\', '^', '`', '~', ' ', '\t', '\n', '\r', '\x0b']
        for symbol in symbols_to_remove:
            symbols.remove(symbol)
        
        return lowercases, uppercases, digits, symbols



    def generate(self) -> str:

        self._password = ''        

        while len(self._password) < self._length:
            character = self.__get_character()
            # The ideal password does not contain duplicates
            # If it does, we select another character randomly
            while character in self._password:
                character = self.__get_character()
            self._password += character

        if not self.__check_numbers():
            self._password = self.generate()

        return self._password



    def __get_character(self) -> str:
        # We select a random type between all possible types (i.e: lowercases, uppercases, digits, symbols)
        type = rd.choice(self._types)
        # From that type, we select a character randomly
        character = rd.choice(type)
        return character


    
    def __check_numbers(self) -> bool:

        lowercase_counter, uppercase_counter, digit_counter, symbol_counter = 0, 0, 0, 0
        for character in self._password:
            if character in self._lowercases:
                lowercase_counter += 1
            elif character in self._uppercases:
                uppercase_counter += 1
            elif character in self._digits:
                digit_counter += 1
            else:
                symbol_counter += 1
        
        return (lowercase_counter>=self._lowercase_number and uppercase_counter>=self._uppercase_number and digit_counter>=self._digit_number and symbol_counter>=self._symbol_number)
        



# Test 1: check_type
# p = Password("2", 2, 2, 2)
# output: ValueError: Parameters must be integers

# Test 2.1: check_assertion
# p = Password(2, 2, 2, 1)
# output: ValueError: The password must contain at least 8 characters

# Test 2.2: check_assertion
# p = Password(3, 2, 2, 1)
# output: ValueError: The password must contain at least 2 characters of each type (i.e lowercases, uppercases, digits, symbols)

# Test 3: class
# p = Password()
# print(p.generate())
# output: -nW7m0uO9o'2+Q)S

# Test 4: long password
# p = Password(8, 8, 8, 8)
# print(p.generate())
# output: =N4&VqiT9Zw)l2v7{5H%E}_hm3pM81@O

# Test 5: recursive error
# p = Password(20, 20, 9, 3)
# print(p.generate())
# output: =N4&VqiT9Zw)l2v7{5H%E}_hm3pM81@O
