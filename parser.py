import os
import glob
import os.path
import re
from os.path import basename, splitext
	
def parser():
	#Creating directory to put .txt files
	os.system('rm -r ParsedPapers')
	os.system('mkdir ParsedPapers')
	ListeDeFichierPdf=getName()
	for x in ListeDeFichierPdf:
		file_to_open = x
		file_to_open = file_to_open.replace(' ', '\ ')
		file_to_read = 'ParsedPapers/' + file_to_open.strip('.pdf') + '.txt'
		temp = file_to_read
		command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
		os.system(command)
		f = open(temp, 'r+')
		#Name
		parsed_file = "Parsed" + i + ".txt"
		fichier = open(parsed_file, 'w+')
		fichier.write(ListeDeFichierPdf[i])
		#Title
		first_lines = f.readline()
		
		fichier.write(first_lines) 
		#Abstract
		content = f.read()
		debutAbstract = (content.find("Abstract"))
		finAbstract = (content.find("\n\n", debutAbstract))
		substring = content[debutAbstract:finAbstract]
		fichier.write(substring) 
		fichier.close()
	

	
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

def getAbstract():
	f = open('Papers/Papers/Alexandrov.txt', "r+")
	content = f.read()
	debutAbstract = (content.find("Abstract"))
	print(debutAbstract)
	finAbstract = (content.find("\n\n", debutAbstract))
	print(finAbstract)
	substring = content[debutAbstract:finAbstract]
	print(substring)
	
def getName():
	ListeDeFichierPdf=[] 
	l = glob.glob('Papers/*.pdf')
	for i in l: 
		a=i.strip("Papers/")
		ListeDeFichierPdf.append(a)
	return(ListeDeFichierPdf)

def main():
	parser()
	
main()










    
