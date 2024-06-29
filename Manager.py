from Password import Password



class Manager:



    def __init__(self):
        
        self._passwords = {}

        # set stores unique values, which is more efficient to check if a password associated to a service exists
        self._services = set()



    def add_password(self):

        service_name = input("Please, enter the service for which you need a password: ")

        if service_name in self._services:
            return print(f'A password already exists for {service_name}')
        else: 
            self._services.add(service_name)
            password = Password().generate()
            self._passwords.update({service_name: password})



    def reset_password(self):
        
        services = ','.join(self._services)
        print(f'Here are the services for which a pasword has been generated: {services}')
        
        service_name = input("Please, enter the service for which you want to reset the password: ")

        if service_name not in self._services:
            return print(f'{service_name} not found')
        else:
            new_password = Password().generate()
            self._passwords.update({service_name: new_password})



    def delete_password(self):
        
        services = ','.join(self._services)
        print(f'Here are the services for which a pasword has been generated: {services}')
        
        service_name = input("Please, enter the service for which you want to delete the password: ")
        
        if service_name not in self._services:
            return print(f'{service_name} not found')
        else:
            self._services.remove(service_name)
            del self._passwords[service_name]



# Test 1:
# my_manager = Manager()
# print(my_manager._passwords)
# output: {}

# Test 2.1: add_password
# my_manager = Manager()
# my_manager.add_password()
# print(my_manager._passwords)
# output: {'unibe': ',2yP5]g_7N1h;KpQ'}

# Test 2.2: add_password (same service_name as input)
# my_manager.add_password()
# output: A password already exists for unibe

# Test 3.1: reset_password
# my_manager.reset_password()
# print(my_manager._passwords)
# output: {'unibe': "C2#|f4lL(EBim13'"}

# Test 3.2: reset_password (wrong input)
# my_manager.reset_password()
# output: unibw not found

# Test 4.1: delete_password (wrong input)
# my_manager.delete_password()
# output: unibw not found

# Test 4.2: delete_password
# my_manager.delete_password()
# print(my_manager._passwords)
# output: {'unibe': "C2#|f4lL(EBim13'"}