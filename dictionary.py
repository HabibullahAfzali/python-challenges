dictionary = {
    "gato" : "chat", 
    "perro" : "chien",
    "caballo" : "cheval"
    }
phone_numbers = {
    'jefe' : 5551234567,
    'Suzy' : 22657854310
                 }
empty_dictionary = {}


words = ['gato','leon','caballo']

for word in words:
    if word in dictionary:
        print(word,"->", dictionary[word])
        
    else:
        print(word, "no exist in dictionary")
# Imprimir valores aquí.
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#-------- using keys method to interate through the dictionary using for loop -----
print("iteration in dictionary using keys method:")
dictionary = {
    "gato" : "chat",
    "perro" : "chien",
    "caballo" : "cheval"
    }

for key in dictionary.keys():
    print(key, "->", dictionary[key])

#--------- using sorted method for sorting the output of a dictionary -------
print("sorting the output of dictionary using sorted method:")
dictionary = {
    "gato" : "chat",
    "perro" : "chien",
    "caballo" : "cheval"
    }

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

#------------ using values method to retrive only the value of dictionary, its similar to keys. but the only different is it just return the value of dictionary not key


print("usint values method for retrieving just dictionary values:")
dictionary = {
    "gato" : "chat",
    "perro" : "chien",
    "caballo" : "cheval"
    }
for french in dictionary.values():
    print(french)
    
  #  ---------- Item methods to iterate the dictionary --
  
print("using Item method to iterate into dictionary")

print("usint values method for retrieving just dictionary values:")
dictionary = {
    "gato" : "chat",
    "perro" : "chien",
    "caballo" : "cheval"
    }
for Spanish ,French in dictionary.items():
    print(Spanish, "->", French)
    
#--------- changing or assigning new value to dictionary
print("changing or asigning new value to the dictionary")

dictionary = {
    "gato" : "perro",
    "dog" : "chien",
    "caballo" : "cheval"
    }

dictionary['gato'] = 'minou'
print(dictionary)

#--------- Deleting or removing element of dictionary
print("Deleting element of  dictionary")

dictionary = {
    "gato" : "perro",
    "dog" : "chien",
    "caballo" : "cheval"
    }

del dictionary['gato']
print(dictionary)


my_list = ['mary','had','a ', 'litle','lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3]= 'ram'
    
print(my_list(my_list))