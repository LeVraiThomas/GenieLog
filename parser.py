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

def displayMenu(file_format) :
	print("Vous avez choisi le format "+file_format) 
	print("Souhaitez-vous convertir tous les fichiers disponibles ? O/N")
	all_some = input()
	if(all_some == "N" or all_some == "n" or all_some == "Non" or all_some == "non") :
		print("Voici les fichiers disponibles : ")
		ListeToConvert = []
		ListeDeFichierPdf=getName() 
		i=0
		for x in ListeDeFichierPdf :
			j = i+1
			print(j, "-" + x)
			i+=1
		choice = input("Veuillez insérer ci-dessous les numéros attribués aux fichiers souhaités, un par ligne :")
		while(choice != "stop") :
			i = 1
			for z in ListeDeFichierPdf :
				if(int(i) == int(choice)) :
					ListeToConvert.append(z)
				i+=1
			for y in ListeToConvert :
				if(file_format == ".txt") :
					parserTXTsolo(y)
				else :
					parserXMLsolo(y)
			choice = input("Veuillez insérer ci-dessous les numéros attribués aux fichiers souhaités :")
	elif(all_some == "O" or all_some == "Oui" or all_some == "o" or all_some == "oui") :
		if file_format == ".txt" : parserTXT()
		else : parserXML()	
	
def parserTXTsolo(f1):
	f1 = f1.strip('.pdf')
	file_to_open = 'Papers/' + f1 + '.pdf'
	file_to_open = file_to_open.replace(' ', '\ ')
	file_to_read = 'ConvertedPapers/' + f1 + '.txt'
	temp = file_to_read
	file_to_read = file_to_read.replace(' ', '\ ')
	command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
	os.system(command)
	open_read = open(temp, 'r+')
	#Name
	parsed_file = 'ParsedPapers/' + f1 + '.txt'
	open_write = open(parsed_file, 'w+')
	open_write.write("Nom du fichier : \n \t"+f1+"\n")
	print(f1)
	#Title
	titre = getTitle(open_read)
	open_write.write("Titre de l'article : \n "+titre.replace('\n', ' ')+"...")
	#Auteur
	authors = getAuthor(open_read)
	open_write.write(" \nAuteurs : \n"+authors)
	#Abstract
	if(ifAbstract(open_read)):
		abstract = getAbstract(open_read)
		open_write.write("\nAbstract/Resume de l'article : \n"+abstract.replace('\n', ' ')[0 : 150]+"...\n") 
	#Introduction
	intro = getIntro(open_read)
	open_write.write("\nIntroduction : \n\t"+intro.replace('\n', ' ')[0 : 150]+"...\n")
	#Corps
	corps = getCorps(open_read)
	open_write.write("\nCorps : \n\t"+corps.replace('\n', ' ')[0 : 300]+"...\n")
	#Conclusion
	conclusion = getConclusion(open_read)
	open_write.write("\nConclusion : \n\t"+conclusion.replace('\n', ' ')[0 : 150]+"...\n")
	#Discussion
	discussion = getDiscussion(open_read)
	open_write.write("\nDiscussion : \n\t"+discussion.replace('\n', ' ')[0 : 150]+"...\n")
	#Bibliography
	bibliography = getBibliography(open_read)
	open_write.write("\nBibliographie : \n\t"+bibliography.replace('\n', ' ')+"\n")
	
	open_read.close()
	open_write.close()
	
	
def parserXMLsolo(f1) :
	article = etree.Element("article")
	preamble = etree.SubElement(article, "preamble")
	titre = etree.SubElement(article, "titre")
	auteur = etree.SubElement(article, "auteur")
	abstract = etree.SubElement(article, "abstract")
	corps = etree.SubElement(article, "corps")
	discussion = etree.SubElement(article, "discussion")
	biblio = etree.SubElement(article, "biblio")
	f1 = f1.strip('.pdf')
	file_to_open = 'Papers/' + f1 + '.pdf'
	file_to_open = file_to_open.replace(' ', '\ ')
	file_to_read = 'ConvertedPapers/' + f1 + '.txt'
	temp = file_to_read
	file_to_read = file_to_read.replace(' ', '\ ')
	command = 'pdf2txt ' + file_to_open + ' > ' + file_to_read
	os.system(command)
	open_read = open(temp, 'r+')
	mpa = dict.fromkeys(range(32))
	#Preamble
	preamble.text = f1.translate(mpa)
	parsed_file = 'ParsedPapers/' + f1 + '.xml'
	#Title
	title = getTitle(open_read).translate(mpa)
	titre.text = title
	#Auteur
	author = getAuthor(open_read).translate(mpa)
	auteur.text = author
	#Abstract
	if(ifAbstract(open_read)):
		a = getAbstract(open_read).translate(mpa)
		abstract.text = a
	#Corps
	c = getCorps(open_read).translate(mpa)
	corps.text = c
	#Discussion
	d = getDiscussion(open_read).translate(mpa)
	discussion.text = d
	#Biblio
	b = getBibliography(open_read).translate(mpa)
	biblio.text = b
	#Arbre
	tree = etree.ElementTree(article)
	#Close
	tree.write(parsed_file)
	open_read.close()
		
	
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
	    #Auteur
		if(ifAbstract(open_read)) :
			authors = getAuthor(open_read)
			open_write.write(" \nAuteurs : \n"+authors)
			#Abstract
			abstract = getAbstract(open_read)
			open_write.write("\nAbstract/Resume de l'article : \n"+abstract.replace('\n', ' ')[0 : 150]+"...\n") 
			#Introduction
			intro = getIntro(open_read)
			open_write.write("\nIntroduction : \n\t"+intro.replace('\n', ' ')[0 : 150]+"...\n")
			#Corps
			corps = getCorps(open_read)
			open_write.write("\nCorps : \n\t"+corps.replace('\n', ' ')[0 : 300]+"...\n")
			#Conclusion
			conclusion = getConclusion(open_read)
			open_write.write("\nConclusion : \n\t"+conclusion.replace('\n', ' ')[0 : 150]+"...\n")
			#Discussion
			discussion = getDiscussion(open_read)
			open_write.write("\nDiscussion : \n\t"+discussion.replace('\n', ' ')[0 : 150]+"...\n")
			#Bibliography
			bibliography = getBibliography(open_read)
			open_write.write("\nBibliographie : \n\t"+bibliography.replace('\n', ' ')+"\n")
		else :
			authors = getAbstract(open_read)
			open_write.write(" \nAuteurs : \n"+authors)
			#Introduction
			intro = getIntro(open_read)
			open_write.write("\nIntroduction : \n\t"+intro.replace('\n', ' ')[0 : 150]+"...\n")
			#Corps
			corps = getCorps(open_read)
			open_write.write("\nCorps : \n\t"+corps.replace('\n', ' ')[0 : 300]+"...\n")
			#Conclusion
			conclusion = getConclusion(open_read)
			open_write.write("\nConclusion : \n\t"+conclusion.replace('\n', ' ')[0 : 150]+"...\n")
			#Discussion
			discussion = getDiscussion(open_read)
			open_write.write("\nDiscussion : \n\t"+discussion.replace('\n', ' ')[0 : 150]+"...\n")
			#Bibliography
			bibliography = getBibliography(open_read)
			open_write.write("\nBibliographie : \n\t"+bibliography.replace('\n', ' ')+"\n")
			
		
		print(i, " fichier(s) converti(s)")
		i=i+1
	    
		open_read.close()
		open_write.close()


def ifAbstract(f1) :
	f2 = f1
	for line in f2 :
		if line.startswith("Abstract") or line.startswith("abstract") or line.startswith("ABSTRACT") :
			return True
		else :
			return False

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
		if line.startswith("Introduction") or line.startswith("introduction") or line.startswith("INTRODUCTION") or line.startswith("1") or line.startswith("I.") or line.startswith("1. Introduction") or line.startswith("I. INTRODUCTION"):
			firstline = line.replace("Introduction", "").replace("introduction", "").replace("INTRODUCTION", "").replace("1", "").replace("I.", "");
			break
		else :
			abstract += "\t"+line.replace('\n', ' ')+"\n"
	return abstract
	
	
	
	
def getIntro(f1) :
	global firstline
	intro = firstline
	
	for line in f1 :
		if line.startswith("2\t") or line.startswith("II\t") or line.startswith("II.") or line.startswith("2  ") or line.startswith("2.") or line.startswith("2 "):
			firstline = line.replace("2\t", "").replace("II\t", "").replace("II.", "")
			break
		else :
			intro += "\t"+line.replace('\n', ' ')+"\n"
			
	return intro


def getCorps(f1) :
	global firstline
	corps = firstline
		
	for line in f1 :
		if re.match("[0-9]* Conclusion", line)  or re.match("[0-9]* CONCLUSION", line) or re.match("[0-9]* Result", line) or re.match("[0-9]* RESULT", line) or re.match("(I|X|V)*. Conclusion", line)  or re.match("(I|X|V)*. CONCLUSION", line) or re.match("(I|X|V)*. Result", line) or re.match("(I|X|V)*. RESULT", line) or re.match("[0-9]*. Conclusion", line)  or re.match("[0-9]*. CONCLUSION", line) or re.match("[0-9]*. Result", line) or re.match("[0-9]*. RESULT", line):
			firstline = line.replace("Conclusion", "").replace("conclusion", "").replace("CONCLUSION", "").replace("Result", "").replace("result", "").replace("RESULT", "")
			break
		else :
			corps += "\t"+line.replace('\n', ' ')+"\n"

	return corps
	
	
def getConclusion(f1) :
	global firstline
	concl = firstline
	
	for line in f1 :
		if re.match("[0-9| ]*Discussion", line)  or re.match("[0-9| ]*DISCUSSION", line) or re.match("[0-9| ]*Acknowledgement", line) or re.match("[0-9| ]*ACKNOWLEDGEMENT", line) or re.match("(I|X|V)*. Discussion", line)  or re.match("(I|X|V)*. DISCUSSION", line) or re.match("(I|X|V)*. Acknowledgement", line) or re.match("(I|X|V)*. ACKNOWLEDGEMENT", line) or re.match("[0-9]*. Discussion", line)  or re.match("[0-9]*. DISCUSSION", line) or re.match("[0-9]*. Acknowledgement", line) or re.match("[0-9]*. ACKNOWLEDGEMENT", line):
			firstline = line.replace("Discussion", "").replace("discussion", "").replace("DISCUSSION", "").replace("Acknowledgement", "").replace("acknowledgement", "").replace("ACKNOWLEDGEMENT", "")		
			break
		else :
			concl += "\t"+line.replace('\n', ' ')+"\n"
			
	return concl
	
	
def getDiscussion(f1) :
	global firstline
	disc = firstline
			
	for line in f1 :
		if line.startswith("Bibliography \n") or line.startswith("BIBLIOGRAPHY \n") or line.startswith("References \n") or line.startswith("REFERENCES \n"):
			firstline = line.replace("Bibliography", "").replace("BIBLIOGRAPHY", "").replace("References", "").replace("REFERENCES", "")
			break
		else :
			disc += "\t"+line.replace('\n', ' ')+"\n"
			
	return disc
	
	
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
		corps = etree.SubElement(article, "corps")
		discussion = etree.SubElement(article, "discussion")
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
		if(ifAbstract(open_read)):
			a = getAbstract(open_read).translate(mpa)
			abstract.text = a
		#Corps
		c = getCorps(open_read).translate(mpa)
		corps.text = c
		#Discussion
		d = getDiscussion(open_read).translate(mpa)
		discussion.text = d
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
	elif sys.argv[1]=="-t" : displayMenu(".txt")
	elif sys.argv[1]=="-x" : displayMenu(".xml")
	else : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	
main()
