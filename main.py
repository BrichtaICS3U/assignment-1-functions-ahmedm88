# Assignment 1
# ICS3U
# <Ahmed M>
# March 28, 2018
###### uncomment this when you are ready to work on it
#Code to convert Celsius to Farenheit
def CtoF (Celsius):
    """Enter a temperature value in Celsius for the value to be converted
    to Farenheit"""
    Celsius = 1.8*Celsius+32
    return round(Celsius)


###### uncomment this when you are ready to work on it
#Code to convert Farenheit to Celsius
def FtoC (Farenheit):
    """Enter a temperature value in Farenheit for the value to be converted
    to Celsius"""
    Farenheit = 0.55556*(Farenheit-32)
    return round(Farenheit)
        

#Asks which conversion user would like to make, Farenheit to Celsius (Type Celsius) or Celsius to Farenheit (Type Farenheit)
ForC = input('Which unit would you like to convert to? Celsius or Farenheit?: ')
if ForC == 'Farenheit':
    temperatureF = float(input('Enter your temperature in Celsius: ')) #Input Celsius value to convert to Farenheit
    if temperatureF <= -273.15 : #Input may not go below -273.15
        print('That temperature is invalid as it is too cold, please do not go below -273.15 degrees Celsius.')
    else:
     print(CtoF(temperatureF))

elif ForC == 'Celsius':
    temperatureC = float(input('Enter your temperature in Farenheit: '))  #Input Farenheit value to convert to Celsius
    if temperatureC <= -459.67 : #Input may not go below -459.67
        print('That temperature is invalid as it is too cold, please do not go below -459.67 degrees Farenheit.')
    else:
     print(FtoC(temperatureC))




