import pickle

# Données à sérialiser
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Sérialisation vers un fichier binaire
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Désérialisation depuis le fichier
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)