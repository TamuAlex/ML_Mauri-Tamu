from pymongo import MongoClient
import pandas as pd


'''
Creamos un cliente de mongo, para ello debemos tener una instancia
de mongo iniciada (escribiendo mongod en el terminal)
'''
client = MongoClient()

'''
Si queremos conectarnos a un host y puerto especifico, ejecutamos
el siguiente comando
'''
#client = MongoClient('localhost', 27017)


'''
Nos conectamos a la base de datos que el usuario quiera
'''
#print("introduce la base de datos con la que quieres trabajar:")
#print("La base de datos de prueba es iris")
#nombredb = input()
#db = client[nombredb]
db = client['iris']


'''
Recuperamos la coleccion con la que vamos a trabajar
En nuestro caso, la coleccion se llama iris
'''
iris = db['iris']


print("Introduce que tipo de petalo quieres sacar:")
print("Solo hay Setosa, Versicolor y Virginica")
nombrePetalo = input()



#resultados = iris.find({},{"\"variety\"":nombrePetalo})

#for x in resultados:
#    print(x)

iris = pd.DataFrame(list(iris.find()))

print(iris)