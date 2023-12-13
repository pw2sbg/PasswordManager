from Password import *


class Manager:


    def __init__(self) -> dict:
        self.my_manager = {}
        # Implement another initialization function


    def get_manager(self) -> dict:
        return self.my_manager
    

    def get_service_name(self, action: str) -> str:
        if action == "add":
            serivce_name = input("Please, enter the service for which you need a password: ")
            # We don't need to check service_name type because input returns a string
            # Check if my_manager already contains the name of the service
            self.is_service_name_in(serivce_name)
        elif action == "reset":
            serivce_name = input("Please, enter the service for which you want to reset the password: ")
        return serivce_name

    
    def is_service_name_in(self, service_name: str) -> str:
        service_names = list(self.my_manager.keys())
        service_names_lower = [name.lower() for name in service_names]
        if service_name.lower() in service_names_lower:
            raise "A password already exists for that service"
        # Can be improved (e.g mistake in input => suggest similar service_names)
    

    def add_password(self) -> None:
        service_name = self.get_service_name("add")
        password = Password().generate()
        self.my_manager.update({service_name: password})


    def set_new_password(self) -> None:
        service_name = self.get_service_name("reset")
        new_password = Password().generate()
        self.my_manager.update({service_name: new_password})



        
# Test 1: get_manager
# my_manager = Manager()
# print(my_manager.get_manager())
# output: {}

# Test 2: add_password (and therefore: get_service_name)
# my_manager = Manager()
# my_manager.add_password()
# print(my_manager.get_manager())
# output: {'UniBE': 'l9_=pYS74Z2zFs,#'}

# Test 3.1: is_service_name_in
# my_manager = Manager()
# input: UniBE
# my_manager.add_password()
# input: UNIBE
# my_manager.add_password()
# output: raise "A password already exists for that service", TypeError: exceptions must derive from BaseException

# Test 3.2: is_service_name_in
# my_manager = Manager()
# input: UniBE
# my_manager.add_password()
# input: unibe
# my_manager.add_password()
# output: raise "A password already exists for that service", TypeError: exceptions must derive from BaseException

# Test 3.3: is_service_name_in
# my_manager = Manager()
# input: UniBE
# my_manager.add_password()
# input: Unibe
# my_manager.add_password()
# output: 
# raise "A password already exists for that service"
# TypeError: exceptions must derive from BaseException

# Test 4: set_new_password
# my_manager = Manager()
# input: UniBE
# my_manager.add_password()
# print(my_manager.my_manager)
# output: {'UniBE': "YI@z0igtX1!'|3F8"}
# input: UniBE
# my_manager.set_new_password()
# print(my_manager.get_manager())
# output: {'UniBE': 'O0%lyH)8qQF7/k5{'}