# tips_python
Funciones python, cortitas y al pié

Para que funcione PyFoam en entornos virtuales recientes, modificar el siguiente archivo del entorno:

~/virtualenvs/Python/lib/python3.12/site-packages/PyFoam/Infrastructure/Configuration.py

por:

#from PyFoam.ThirdParty.six.moves import configparser
#from PyFoam.ThirdParty.six import iteritems,PY3
import configparser
from six import iteritems,PY3
