from requests import request
from .consts import graphQLUrl, headers

class gdbcClient:

    def __init__(self):
        print("gdbcClient instantiated")
    
    def ExecuteQuery(query, variables = None):
        
        payload = { "query": query }
        if variables:
            payload.update({ "variables": variables })
        
        response = request("POST", graphQLUrl, json=payload, headers=headers)
        
        return response
