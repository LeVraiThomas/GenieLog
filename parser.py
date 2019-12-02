import glob
import os.path

from os.path import basename, splitext



ListeDeFichierPdf=[] 
l = glob.glob('Papers/*.pdf')
for i in l: 
	a=i.strip("Papers/")
	ListeDeFichierPdf.append(a)

fichier = open("fichier1.txt", "w")
fichier.write(ListeDeFichierPdf[0])
fichier.close()

