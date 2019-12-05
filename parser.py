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
		#Name
		preamble.text = x
		parsed_file = 'ParsedPapers/' + x + '.xml'
		#Title
		title = getTitle(open_read)
		titre.text = title
		#Abstract
		a = getAbstract(open_read)
		abstract.text = a
		tree = etree.ElementTree(article)
		#Close
		tree.write(parsed_file)
		open_read.close()
	    

	    
	    
def getTitle(f1) :
    first_lines = f1.readline()
    return first_lines
    

def getAbstract(f1):
	content = f1.read()
	debutAbstract = (content.find("Abstract"))
	finAbstract = (content.find("\n\n", debutAbstract))
	substring = content[debutAbstract:finAbstract]
	return substring
	
	
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










    
