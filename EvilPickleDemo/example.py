import pickle
import pickletools


data = {"name": "Alice", "age": 30, "scores": [88, 92, 95]}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file, protocol=0)
    print("Data has been successfully serialized to data.pkl")

with open("data.pkl", "rb") as file:
    unpickled_data = pickle.load(file)
    print(unpickled_data)
