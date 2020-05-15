# Date:2020/5/15
# Author:Lingchen
# Mark:
import collections

print('collections.namedtuple: ')
coordinate = collections.namedtuple('Coordinate', ['x', 'y'])
co = coordinate(10, 20)
print(co.x, co.y)

co = coordinate._make([100, 200])
print(co.x, co.y)

co = co._replace(x=30)
print(co.x, co.y)
