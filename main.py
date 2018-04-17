import game
import numpy as np

x = np.arange(9).reshape(3, 3)
print(x)
# print(np.where(x > 5))
print(np.diag(np.fliplr(x)))
