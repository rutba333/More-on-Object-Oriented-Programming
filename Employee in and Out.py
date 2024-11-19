class Employee:
    #initializing
    def __init__(self):
     print('Employee created')

     #calling destructor
    def __del__(self):
       print("Destructor called")

def create_obj():
   print('Making object...')
   obj=Employee()
   print('function ended...')
   return obj

print('calling create_obj function....')
obj=create_obj()
print('program ended...')
    