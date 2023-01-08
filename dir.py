import os
import sys

dirrect, dirrect_2, name = sys.argv[1:]
files = os.listdir(dirrect)
st = str()
for i in range(len(files)):
    st += f'{dirrect}/{files[i]} {dirrect_2}/{files[i]}\n'

with open(name, 'w') as file:
    file.write(st)
