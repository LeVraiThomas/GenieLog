
import re
f = open('Papers/Papers/Alexandrov.txt', "r+")
content = f.readl()

debutAbstract = (content.find("Abstract"))
print(debutAbstract)

finAbstract = (content.find("\n\n", debutAbstract))
print(finAbstract)
i = 1

for x in range(debutAbstract,finAbstract):
    print(debutAbstract)
    debutAbstract=debutAbstract+1
    

