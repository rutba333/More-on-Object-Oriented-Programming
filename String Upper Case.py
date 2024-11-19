#create class
class IOString:
     #constructer to set defult values
     def __init__(self):
          self.str=""

          #function to get input from user
     def get_String (self):
       self.str1=input("enter string:")

      #function to print the string in uppercase
     def print_String(self):
           print("result is:",self.str1.upper())

       #obj creation
str1=IOString()

#call functions
str1.get_String()
str1.print_String()
