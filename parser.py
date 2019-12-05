import os
import glob
import os.path
import re
from os.path import basename, splitext
import sys
	
def init():
	#Creating directory to put .txt files
	os.system('rm -r ConvertedPapers')
	os.system('mkdir ConvertedPapers')
	os.system('rm -r ParsedPapers')
	os.system('mkdir ParsedPapers')
	
	
def parserTXT():
	init()
	ListeDeFichierPdf=getName()
	for x in ListeDeFichierPdf:
	    x = x.strip('.pdf')
	    file_to_open = 'Papers/' + x + '.pdf'
	    file_to_open = file_to_open.replace(' ', '\ ')
	    file_to_read = 'ConvertedPapers/' + x + '.txt'
	    temp = file_to_read
	    file_to_read = file_to_read.replace(' ', '\ ')
	    command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
	    os.system(command)
	    open_read = open(temp, 'r+')
	    #Name
	    parsed_file = 'ParsedPapers/' + x + '.txt'
	    open_write = open(parsed_file, 'w+')
	    open_write.write("Nom du fichier : "+x+"\n")
	    #Title
	    getTitle(open_read, open_write)
	    #Abstract
	    getAbstract(open_read, open_write)
	    #Close
	    open_read.close()
	    open_write.close()
	
def parserXML():
	init()
	ListeDeFichierPdf=getName()
	for x in ListeDeFichierPdf:
	    x = x.strip('.pdf')
	    file_to_open = 'Papers/' + x + '.pdf'
	    file_to_open = file_to_open.replace(' ', '\ ')
	    file_to_read = 'ConvertedPapers/' + x + '.txt'
	    temp = file_to_read
	    file_to_read = file_to_read.replace(' ', '\ ')
	    command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
	    os.system(command)
	    open_read = open(temp, 'r+')
	    #Name
	    parsed_file = 'ParsedPapers/' + x + '.xml'
	    open_write = open(parsed_file, 'w+')
	    open_write.write("Nom du fichier : "+x+"\n")
	    #Title
	    getTitle(open_read, open_write)
	    #Abstract
	    getAbstract(open_read, open_write)
	    #Close
	    open_read.close()
	    open_write.close()
	    
def getTitle(f1, f2) :
    first_lines = f1.readline()
    f2.write("Titre de l'article : "+first_lines)
    

def getAbstract(f1, f2):
	content = f1.read()
	debutAbstract = (content.find("Abstract"))
	finAbstract = (content.find("\n\n", debutAbstract))
	substring = content[debutAbstract:finAbstract]
	f2.write("Abstract/Resume de l'article : "+substring+"\n") 
	
def getName():
	ListeDeFichierPdf=[] 
	l = glob.glob('Papers/*.pdf')
	for i in l: 
		a=i.strip("Papers/")
		ListeDeFichierPdf.append(a)
	return(ListeDeFichierPdf)

def main():
	if len(sys.argv) < 2 : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	elif sys.argv[1]=="-t" : parserTXT()
	elif sys.argv[1]=="-x" : parserXML()
	else : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	
main()










    
