def name(Name): #This line defines a function called 'name' that takes one parameter 'Name'. The function will return the value of 'Name' when called.
	return Name
name = input('Enter your name: ') #This line prompts the user to enter their name and stores it in the variable 'name'
print("----------------------------------") #This line prints a separator line for better readability in the output
print(f'Hello {name}, welcome!') #This line prints a greeting message using the name provided by the user.

#Function to convert Celsius to Fahrenheit 
def celsuis_to_fahrenheit(celsius):
	fahrenheit = (celsius*9/5) + 32  #Formula in converting celsius to fahrenheit
	return fahrenheit

#Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsuis(fahrenheit):
	celsius = (fahrenheit-32) *5/9  #Formula in converting fahrenheit to celsius
	return celsius

#Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
	kelvin = celsius + 273.15  #Formula in converting celsius to kelvin
	return kelvin

print("----------------------------------")
temperature = float(input("Enter temperature in Celsius: "))
print(f"In Fahrenheit: {celsuis_to_fahrenheit(temperature)} F") # This line calls the celsuis_to_fahrenheit function and prints the result in Fahrenheit
print(f"In Kelvin: {celsius_to_kelvin(temperature)} K")         # This line calls the celsius_to_kelvin function and prints the result in Kelvin

print("----------------------------------")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print(f"In Celsius: {fahrenheit_to_celsuis(fahrenheit)} C \nThank you for using my temperature converter!") #This line calls the fahrenheit_to_celsuis function and prints the result in Celsius and to thank the user for using the temperature converter.