"""
Author: Sergio Garcia Prado
        www.garciparedes.me
"""

import wolframalpha

client = wolframalpha.Client("")

operation = input("Indique la operacion: ")

res = client.query(operation)
print(next(res.results).text)
