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
		getTitle(open_read, open_write)
		#Abstract
		getAbstractAndIntroAndBiblio(open_read, open_write)

		#Close
		open_read.close()
		open_write.close()
	

	
def getTitle(f1, f2) :
    first_lines = f1.readline()
    f2.write("Titre de l'article : "+first_lines)
    

def getAbstractAndIntroAndBiblio(f1, f2):
	content = f1.read()
	debutAbstract = (content.find("Abstract"))
	if debutAbstract == -1:
		debutAbstract = (content.find("ABSTRACT"))
	finAbstract = (content.find("Introduction", debutAbstract))
	if finAbstract == -1:
		finAbstract = (content.find("INTRODUCTION", debutAbstract))
	substringabstract = content[debutAbstract:finAbstract]
	f2.write("\n"+substringabstract+"\n")

	#intro
	
	debutIntro = finAbstract
	finIntro = (content.find("\n\n2 "))
	if finIntro ==-1:
		finIntro = (content.find("\n\n2."))
		if finIntro ==-1:
			finIntro = (content.find("\n\nII."))
			if finIntro == -1:
				finIntro = (content.find("2 "))
	substringIntro=content[debutIntro:finIntro]
	f2.write("\n"+substringIntro+"\n")

	#corps

	debutCorp = finIntro
	finCorp = (content.find("Conclusion"))
	if finCorp ==-1:
		finCorp = (content.find("CONCLUSION"))
	substringCorp=content[debutCorp:finCorp]
	f2.write("\n"+substringCorp+"\n")


	#biblio

	debutBiblio = (content.find("References"))
	if debutBiblio == -1:
			debutBiblio = (content.find("REFERENCES"))
	finBiblio = (content.find("FF", debutBiblio))
	substringbiblio = content[debutBiblio:finBiblio]
	f2.write("\n" + substringbiblio+"\n")


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










    
