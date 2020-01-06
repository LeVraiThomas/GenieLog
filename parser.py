import os
import glob
import os.path
import re
from os.path import basename, splitext
import sys
from lxml import etree

#Used when a part ending is the begining of another one
firstline = ""

def init():
	#Creating directory to put .txt files
	os.system('rm -r ConvertedPapers')
	os.system('mkdir ConvertedPapers')
	os.system('rm -r ParsedPapers')
	os.system('mkdir ParsedPapers')
	
	
def parserTXT():
	init()
	ListeDeFichierPdf=getName()
	global firstline
	firstline = ""
	i=1
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
	    open_write.write("Nom du fichier : \n \t"+x+"\n")
	    #Title
	    titre = getTitle(open_read)
	    open_write.write("Titre de l'article : \n "+titre.replace('\n', ' ')+"...")
	    #Abstract
	    abstract = getAbstract(open_read)
	    open_write.write("\nAbstract/Resume de l'article : \n"+abstract.replace('\n', ' ')[0 : 150]+"...\n") 
	    print(i, " fichier(s) converti(s)")
	    i=i+1
	    
	    open_read.close()
	    open_write.close()


def getTitle(f1) :
    first_lines = f1.readline()
    first_lines += f1.readline()
    first_lines += f1.readline()
    return("\t"+first_lines)
    
    
#The two first lines for f1 have been read previously so we just have to stop when we find the next keyword
def getAuthor(f1) :
	global firstline
	authors = firstline
	for line in f1 :
		if line.startswith("Abstract") or line.startswith("abstract") or line.startswith("ABSTRACT") :
			firstline = line.replace("Abstract", "").replace("abstract", "").replace("ABSTRACT", "");
			break
		else :
			authors += "\t"+line.replace('\n', ' ')+"\n"
	return authors.replace("\n\n", '')
	

def getAbstract(f1) :
	global firstline
	abstract = firstline
	for line in f1 :
		if line.startswith("Introduction") or line.startswith("introduction") or line.startswith("INTRODUCTION") or line.startswith("1") or line.startswith("I.") :
			firstline = line.replace("Introduction", "").replace("introduction", "").replace("INTRODUCTION", "").replace("1", "").replace("I.", "");
			break
		else :
			abstract += "\t"+line.replace('\n', ' ')+"\n"
	return abstract
	
	
def getBibliography(f1) :
	global firstline
	bib = firstline
	for line in f1 :
		bib += "\t"+line.replace('\n', ' ')+"\n"
	return bib


def parserXML():
	init()
	ListeDeFichierPdf=getName()
	i = 1
	for x in ListeDeFichierPdf:
		print(i," fichier(s) converti(s)")
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
		mpa = dict.fromkeys(range(32))
		#Preamble
		preamble.text = x.translate(mpa)
		parsed_file = 'ParsedPapers/' + x + '.xml'
		#Title
		title = getTitle(open_read).translate(mpa)
		titre.text = title
		#Auteur
		author = getAuthor(open_read).translate(mpa)
		auteur.text = author
		#Abstract
		a = getAbstract(open_read).translate(mpa)
		abstract.text = a
		#Biblio
		b = getBibliography(open_read).translate(mpa)
		biblio.text = b
		#Arbre
		tree = etree.ElementTree(article)
		#Close
		tree.write(parsed_file)
		open_read.close()
		i+=1
	      


def getName():
	ListeDeFichierPdf=[] 
	l = glob.glob('Papers/*.pdf')
	for i in l: 
		a=i.strip("Papers/")
		ListeDeFichierPdf.append(a)
	return(ListeDeFichierPdf)

def main():
	init()
	if len(sys.argv) < 2 : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	elif sys.argv[1]=="-t" : parserTXT()
	elif sys.argv[1]=="-x" : parserXML()
	else : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	
main()
