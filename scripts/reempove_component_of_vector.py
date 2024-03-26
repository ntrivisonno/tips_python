# script that removes component of a vector

import numpy as np

vec = np.array([1,2,3,4,5,5,5,5,5,6,7,8,9])

new_vec = [_k for _k in vec if _k!=5]

count = len(vec) - len(new_vec)

print(f'Vector orig: {vec}.\nNew vector:  {new_vec}.\nSe removieron {count} componentes')

print('#--------------------------------------------')
print('\n FIN, OK!')
