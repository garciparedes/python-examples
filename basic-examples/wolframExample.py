"""
Author: Sergio Garcia Prado
        www.garciparedes.me
""""

import wolframalpha


client = wolframalpha.Client(app_id)


operation = raw_input("Indique la operacion: ")



res = client.query(operation)
print(next(res.results).text)
