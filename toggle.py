def toggle():
	n = slicer.util.getNode('prueba')
	a = slicer.util.array('prueba')
	a[:] = 300
	n.GetImageData().Modified()
	print('Toggled')
	
	
>>> n = slicer.util.getNode('foto')
>>> a = slicer.util.array('foto')
>>> import numpy as np
>>> hist, bin_edges = np.histogram(a,255)
>>> hist
>>> value_array = np.zeros((255))
>>> value_array
>>> for x in range(0, 255):
...   value_array[x] = 1


>>> sys.path.append("C:\\Users\\Daniel\\Desktop\\SOFTWARE\\PID\\TD")
>>> import hell
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: No module named hell
>>> import hello
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\Daniel\Desktop\SOFTWARE\PID\TD\hello.py", line 1
    def print_hello:
                   ^
SyntaxError: invalid syntax
>>> import hello
>>> hello.print_hello
<function print_hello at 0x000000000C837518>
>>> hello.print_hello()
