import re
import os
import glob
import os.path
import re
from os.path import basename, splitext
import sys
from lxml import etree
	
def init():
	#Creating directory to put .txt files
	os.system('rm -r ConvertedPapers')
	os.system('mkdir ConvertedPapers')
	os.system('rm -r ParsedPapers')
	os.system('mkdir ParsedPapers')
	
def displayMenu(file_format) :
	print("You chose to convert your PDF files as "+file_format+" files") 
	all_some = input("Do you want to convert all available files ? Y/N")
	if(all_some == "N" or all_some == "n" or all_some == "No" or all_some == "no") :
		choice = input("Please insert bellow the numbers given to the files you want to convert :")
		pattern = re.compile("^([0-9][0-9]+)+$")
		pattern.match(choice)
	elif(all_some == "Y" or all_some == "Yes" or all_some == "y" or all_some == "yes") :
		if file_format == ".txt" : parserTXT()
		else : parserXML()
		
	
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
	    titre = getTitle(open_read)
	    open_write.write("Titre de l'article : "+titre)
	    #Abstract
	    abstract = getAbstract(open_read)
	    open_write.write("Abstract/Resume de l'article : "+abstract+"\n") 
	    getTitle(open_read, open_write)
	    content = open_read.read()
	    #Auteur
	    getAuteur(content, open_write)
	    #Abstract
	    getAbstract(content, open_write)
	    #Close
	    open_read.close()
	    open_write.close()

def parserXML():
	init()
	ListeDeFichierPdf=getName()
	for x in ListeDeFichierPdf:
		article = etree.Element("article")
		preamble = etree.SubElement(article, "preamble")
		titre = etree.SubElement(article, "titre")
		auteur = etree.SubElement(article, "auteur")
		abstract = etree.SubElement(article, "abstract")
		biblio = etree.SubElement(article, "biblio")
		x = x.strip('.pdf')
		file_to_open = 'Papers/' + x + '.pdf'
		file_to_open = file_to_open.replace(' ', '\ ')
		file_to_read = 'ConvertedPapers/' + x + '.txt'
		temp = file_to_read
		file_to_read = file_to_read.replace(' ', '\ ')
		command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
		os.system(command)
		open_read = open(temp, 'r+')
		#Preamble
		preamble.text = x
		parsed_file = 'ParsedPapers/' + x + '.xml'
		#Title
		title = getTitle(open_read)
		content = open_read.read()
		titre.text = title
		#Auteur

		#Abstract
		a = getAbstract(content)
		abstract.text = a
		#Biblio

		#Arbre
		tree = etree.ElementTree(article)
		#Close
		tree.write(parsed_file)
		open_read.close()
	      
def getTitle(f1) :
    first_lines = f1.readline()
    return(first_lines)
    
def getAuteur(f1):
	finAuteur = (f1.find("Abstract"))
	paragrapheAuteur = f1[:finAuteur]
	return(paragrapheAuteur)


def getAbstract(f1):
	debutAbstract = (f1.find("Abstract"))
	if debutAbstract == -1:
		debutAbstract = (f1.find("ABSTRACT"))
	finAbstract = (f1.find("Introduction", debutAbstract))
	if finAbstract == -1:
		finAbstract = (f1.find("INTRODUCTION", debutAbstract))
	substringabstract = f1[debutAbstract:finAbstract]
	return(substringabstract)

	
def getBiblio(f1):
	debutBiblio = (f1.find("References"))
	if debutBiblio == -1:
		debutBiblio = (f1.find("REFERENCES"))
	finBiblio = (f1.find("FF", debutBiblio))
	substringbiblio = f1[debutBiblio:finBiblio]
	#substringbiblio = substringbiblio.replace("\x", " ")
	#substringbiblio = substringbiblio.replace("\n", " ")
	#substringbiblio = substringbiblio.replace("-\n", " ")
	#substringbiblio = substringbiblio.replace("-\n", " ")
	#print(substringbiblio)
	return(substringbiblio)

def getName():
	ListeDeFichierPdf=[] 
	l = glob.glob('Papers/*.pdf')
	for i in l: 
		a=i.strip("Papers/")
		ListeDeFichierPdf.append(a)
	return(ListeDeFichierPdf)

def main():
	if len(sys.argv) < 2 : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	elif sys.argv[1]=="-t" : displayMenu(".txt")
	elif sys.argv[1]=="-x" : displayMenu(".xml")
	else : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	
main()










    
