# Les type primitive en python
"""les type primitive en python"""

nom = "Sarr"  #  c'est string
age = 19   # int
isyoung = True  # bool
taille = 1.67  # float

print(type(nom))
print(type(age))
print(type(isyoung))
print(type(taille))

# les constat

prenom = "hello"
print(prenom)

prenom = "wass"
print(prenom)

# Par convention les constant en python son nommé en lettre majuscule
NAME = "Ib"
print(NAME)

# list/Tuple/set/dict

my_list = [12, "A", 4 , 12.3, True]

print(len(my_list))
print(my_list)
my_list.append("wass")
print(my_list)
my_list.remove(12)
print(my_list)

print()
print("#################list2##########")

list2 = my_list[:]

print(list2)

list2.append("Fatima")
print(f"list2: {list2}")

print(f"my_list: {my_list}")

### Tuple ####

my_tuple = (12) # n'est pas un tuple

my_tuple2 = (12, ) # est un tuple

print(type(my_tuple))
print(len(my_tuple2))
""" Tuple sont il immuable ou muable """

#### Dict ####

my_dict = {
        "name": "Wass",
        "age": 100,
        "taile": 1.76
        }

print(my_dict['name'])

print(my_dict.get('last_name', "Sarr"))

print(my_dict)

##### set #####
"""c'est quoi les set ?"""
