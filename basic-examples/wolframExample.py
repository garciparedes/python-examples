"""
Author: Sergio Garcia Prado
        www.garciparedes.me
"""

import wolframalpha
from pip._vendor.distlib.compat import raw_input

client = wolframalpha.Client("")


operation = raw_input("Indique la operacion: ")



res = client.query(operation)
print(next(res.results).text)
