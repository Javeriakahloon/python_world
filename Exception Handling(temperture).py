class Temperaturerror(Exception):
    def __init__(self,temp):
       self.temp=temp
       super().__init__(f'invalid temperture.\nIt should be between 0-100')
def check_temp(temp):
        if temp <0   or temp > 100:
              raise Temperaturerror(temp)
        else:
           print("temperature is safe.")          
try:
    userinput=float(input('Enter temeprature: ' ))
    check_temp(userinput)
except Temperaturerror as e:
    print(f'error = {e}')
except ValueError:
    print("invalid input...")
    
                
