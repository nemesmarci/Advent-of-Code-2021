from itertools import product
from common import get_data, magnitude, addition

pairs = get_data()
print(max(magnitude(addition(*p))
          for p in product(pairs, pairs) if p[0] != p[1]))
