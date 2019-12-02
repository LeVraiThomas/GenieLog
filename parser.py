import os

def parser(src, dst):
	for line in src: 
		print(line)

def main():
	src = "Alexandrov"
	fichier = "Papers/" + src + ".pdf"
	cmd = 'pdf2txt ' + fichier + '>' + "Papers/" + src + ".txt"
	os.system(cmd)
	txt = "Papers/" + src + ".txt"
	source = open(txt, "r")
	destination = open("out.txt", "w")
	parser(source, destination)
	try:
		parser(source, destination)
    
	finally:
		destination.close()
		source.close()


main()

