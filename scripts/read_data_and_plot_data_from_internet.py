import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

data = pd.read_html ("https://wiki.anton-paar.com/en/water/")[0]

water = data.rename(mapper = lambda n : n.strip().rsplit(maxsplit =1)[0] , axis =1).set_index("Temp.")
# con esta función anónima, primero, la función strip() elimina los espacios en blanco al principio y al final del nombre de la columna (n). Luego, la función rsplit(maxsplit=1) se aplica al resultado de strip(), dividiendo el nombre de la columna en dos partes en el último espacio en blanco encontrado (comenzando desde la derecha), con un máximo de 1 separación. Y por último, configura como índice a la temp.

water.describe()
water.plot()

print('#--------------------------------------------')
#print('Resul: ', Resul)
print('\n FIN, OK!')
plt.show()


