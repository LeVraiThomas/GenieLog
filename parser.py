
import re
f = open('Papers/Papers/Alexandrov.txt', "r+")
content = f.read()


debutAbstract = (content.find("Abstract"))
print(debutAbstract)

finAbstract = (content.find("\n\n", debutAbstract))
print(finAbstract)


substring = content[debutAbstract:finAbstract]
print(substring)
    
