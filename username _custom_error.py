class UsernameError(Exception):
    def __init__(self,name):
        self.name=name
        super().__init__(f'invalid username {self.name}.\nThe username shouldnot contain spaces and must be atleast 4 characters.')
def check_username(name):
    if len(name)<4 or " "in name or name.isdigit():
        raise UsernameError(name)
    else:
        print('user name enter successfully.')   
try:
    indentity=input('Enter  name: ')
    check_username(indentity)
except UsernameError as e:
    print(f'error = {e}')
except ValueError(indentity):
    print('Invalid input.')
    
           
