from urllib import request
import requests


def GetUserById(userId):
    response = requests.get("https://api.roblox.com/users/{}".format(userId))

    # if the request succeeded, return
    if (response.status_code == 200):
        return response.json()

    return response.status_code

def GetProductInfoById(assetId):
    response = requests.get("https://api.roblox.com/marketplace/productinfo?assetId={}".format(assetId))

    if (response.status_code == 200):
        return response.json()

    return response.status_code
