default_pin='7384'
current_pin=0
def authenticate():
   global current_pin
   print('welcome to secret vault access.You have only three tries ,Be careful')
   attempts=0
   while attempts <3:
        pin=input('enter your pin: ')
        if default_pin==pin:
           print('Access Granted')
           current_pin=pin
           return True
        else :
            print('wrong pin')
            attempts+=1
print('system locked .too amny attempts')       

def menu():
    global  current_pin,default_pin
    print(" 1.View Vault Status.\n 2.Change Pin.\n 3.Exit")
    option=int(input('enter you choice : '))
    if option==1:
            print("Vault secure.n instructions detected.")
            return True
    elif option==2:
            new_pin=input('enter new pin: ')
            confirm_pin=input('confirm pin: ')
            if new_pin==confirm_pin:
                print('pin updated')
            else:
                print('pin donot matched.')
    elif option==3:
        print('Good bye!') 
        return False
                  
    else:
        print('Invalid choice.')   
        return True 
def main():
    if authenticate():
        while True:
          menu()
          if not menu():
              break
            
            
    else: exit()
main()

    
