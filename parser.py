import os
import glob
import os.path

from os.path import basename, splitext

def parser(src, dst):
	for line in src: 
		print(line)

def getTitle(file_to_parse) :
	title = ""
	
	#Creating directory to put .txt files
	os.system('rm -r ParsedPapers')
	os.system('mkdir ParsedPapers')
	
	#Calculate the .pdf file to convert
	file_to_open = 'Papers/' + file_to_parse + '.pdf'
	file_to_open = file_to_open.replace(' ', '\ ')
	
	#Calculate the .txt file to read
	file_to_read = 'ParsedPapers/' + file_to_parse + '.txt'
	temp = file_to_read
	file_to_read = file_to_read.replace(' ', '\ ')
	
	#Converting file
	command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
	os.system(command)
	
	#Reading .txt file
	f = open(temp, 'r')
	first_lines = f.readline()
	
	return(first_lines)

def getName():
	ListeDeFichierPdf=[] 
	l = glob.glob('Papers/*.pdf')
	for i in l: 
		a=i.strip("Papers/")
		ListeDeFichierPdf.append(a)
	fichier = open("fichier1.txt", "w")
	fichier.write(ListeDeFichierPdf[0])
	fichier.close()
	return(ListeDeFichierPdf)

def main():
	src = "Alexandrov"
	fichier = "Papers/" + src + ".pdf"
	cmd = 'pdf2txt ' + fichier + '>' + "Papers/" + src + ".txt"
	os.system(cmd)
	txt = "Papers/" + src + ".txt"
	source = open(txt, "r")
	destination = open("out.txt", "w")
	print(getTitle('Alexandrov_2015_A Modified Tripartite Model for Document Representation in Internet Sociology'))
	parser(source, destination)
	try:
		parser(source, destination)
    
	finally:
		destination.close()
		source.close()
		
main()








import re
f = open('Papers/Papers/Alexandrov.txt', "r+")
content = f.read()


debutAbstract = (content.find("Abstract"))
print(debutAbstract)

finAbstract = (content.find("\n\n", debutAbstract))
print(finAbstract)


substring = content[debutAbstract:finAbstract]
print(substring)
    
