#declaration de variable
name = 'wass'
age = 12
taill = 1.80
bool = True
print(name)
print(age)
#les list,tuple,dictonary,set
#declaration
my_list1 = [1,3,5,77]
my_list2 =["wass",'fatima']
my_list3 =["wass",1,2.5,455]
#indexing ,mutable,
#retirer un  element
#ajouter un element append
my_list1.remove(1)
#lenght de la list
print(my_list1)
print(my_list1[-1])
#mutable
m_list = my_list2
print(f"m_list: {m_list}")
print(f"my_list :{my_list2}" )
print("#modification#")
m_list.append(44)
print(f"m_list: {m_list}")
print(f"my_list :{my_list2}" )
print('#')
m_list = my_list2 
