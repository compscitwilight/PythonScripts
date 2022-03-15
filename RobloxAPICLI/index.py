import requests
import functions

"""
Roblox users API in Python.
"""

print("API Choices:")
print("1: GetUserById")
print("2: GetProductInfoById")

choice = input()

match (choice):
    case "1":
        print("What is the ID of the user?")
        id = input()

        print(functions.GetUserById(id))
    case "2":
        print("What is the ID of the asset?")
        id = input()

        print(functions.GetProductInfoById(id))
