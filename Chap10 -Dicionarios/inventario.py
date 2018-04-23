#!/usr/bin/env python3

inventario = {'abacaxis':430, 'bananas':312, 'laranjas': 525, 'peras':217}
print(inventario)


del inventario['peras']
print(inventario)

inventario['peras'] = 0
print(inventario)
print(len(inventario))
