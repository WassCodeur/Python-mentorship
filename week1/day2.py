# structures controle (if, if ..... else, if .... elif.....else)
"""age = int(input("Quel est ton age?: "))

if age < 18:
    print("tu es ado")
elif age > 18:
    print("tu es majeur")
else:
    print("alors tu as 18 ans")
"""
# OR / AND (|| , &&)

# Boucle
my_list = [1, 2, 4 , 5, True, "Hello"]

"""for elem in my_list:
    print(elem)
"""

"""for i in range(len(my_list)):
    print(my_list[i])
"""
# "_" variable neutre
"""for _ in range(10):
    print(my_list)
"""

# Function 
def my_fun(): # fonction sans arguments
    print("hello")
def greet(name): # fonction avec arguments
    print(f'hello {name}')

# appel des fonctions
my_fun()
greet("Fatima")

