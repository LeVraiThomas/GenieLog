import os
import glob
import os.path
import re
from os.path import basename, splitext
import sys
from lxml import etree
from unicodedata import *

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
	    print(x)
	    #Title
	    titre = getTitle(open_read)
	    open_write.write("Titre de l'article : \n "+titre.replace('\n', ' ')+"...")
	    #Auteur
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
	    #test : print(x, titre, authors, abstract)
	    
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

#Corps : 2, II

#Results = conclusion

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
			print(line)
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
	i = 0
	for x in ListeDeFichierPdf:
		print(i)
		article = etree.Element("article")
		preamble = etree.SubElement(article, "preamble")
		titre = etree.SubElement(article, "titre")
		auteur = etree.SubElement(article, "auteur")
		abstract = etree.SubElement(article, "abstract")
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
		auteur.text = title
		#Abstract
		a = getAbstract(open_read).translate(mpa)
		abstract.text = a
		#Discussion
		d = getDiscussion(open_read).translate(mpa)
		discussion.text = d
		#Biblio
		b = getBibliography(open_read)
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
	if len(sys.argv) < 2 : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	elif sys.argv[1]=="-t" : parserTXT()
	elif sys.argv[1]=="-x" : parserXML()
	else : print("Veuillez signifier une option pour convertir correctement votre fichier (-t pour .txt et -x pour .xml)")
	
main()










    
