# script for removing background
#$pip3 install rembg

from rembg import remove
from PIL import Image

input_path = 'fig_original.jpg'
output_path = 'fig.png'
inp = Image.open(input_path)
output.save(output_path)

print('#--------------------------------------------')
print('\n FIN, OK!')

plt.show()
