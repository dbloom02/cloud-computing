import Pyro4

#uri = input("Enter the Pyro URI of the hello world class? ").strip()
uri = 'PYRO:obj_6154799cac92458588533a61b8a05cb1@localhost:45945'
name = input("What is your name? ").strip()
a = input("Enter the first number: ") 
b = input("Enter the second number: ")

# get a Pyro proxy to the hellow world maker object
hello_world_maker = Pyro4.Proxy(uri)

# call method normally as it was local
print(hello_world_maker.get_message(name))
print("Result: ",hello_world_maker.sum_of_2(a,b))