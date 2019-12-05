import os
import glob
import os.path
import re
from os.path import basename, splitext
	
def parser():
	#Creating directory to put .txt files
	os.system('rm -r ConvertedPapers')
	os.system('mkdir ConvertedPapers')
	os.system('rm -r ParsedPapers')
	os.system('mkdir ParsedPapers')
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
	    lastword = getTitle(open_read, open_write)
	    content = open_read.read()
	    #Abstract
	    getAbstract(content, open_write)
	    #Auteur
	    getAuteur(content, open_write, lastword)
	    #Close
	    open_read.close()
	    open_write.close()
	

	
def getTitle(f1, f2) :
    first_lines = f1.readline()
    f2.write("Titre de l'article : "+first_lines)
    return "Representation"
    
def getAuteur(f1, f2, lastword):
	debutAuteur = (f1.find(lastword))
	finAuteur = (f1.find("Abstract"))
	paragrapheAuteur = f1[debutAuteur:finAuteur]
	f2.write("La section auteurs et leur adresse :"+paragrapheAuteur)    

def getAbstract(f1, f2):
	debutAbstract = (f1.find("Abstract"))
	finAbstract = (f1.find("\n\n", debutAbstract))
	substring = f1[debutAbstract:finAbstract]
	f2.write("Abstract/Resume de l'article : "+substring+"\n") 
	
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










    
