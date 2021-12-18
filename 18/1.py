from functools import reduce
from common import get_data, magnitude, addition

print(magnitude(reduce(addition, get_data())))
