import os
import sys
import time
from os import listdir
from os.path import isfile, join
import markdown
from CodeHtml import CodeHtml
from github import Github
import getpass

output = [CodeHtml]

liste_fichier_md = []
def commande_markdown(path):	
	compteur = 0
	for i_md in path:				
		extension = os.path.splitext(i_md)
		if ".md" in extension[1]:			
			liste_fichier_md.append(i_md)
			print (f"{compteur}---{i_md}")
			compteur +=1
			time.sleep(0.1)	

liste_fichier_html = []
def commande_html(path):
	compteur = 0	
	for i in path:			
		extension = os.path.splitext(i)
		if ".html" in extension[1]:				
			liste_fichier_html.append(i)
			print (f"{compteur}---{i}")
			compteur +=1
			time.sleep(0.1)		

def convertisseur(liste_fichierMd_insertion,fichier_html ):
	
	
	for i in liste_fichierMd_insertion:
		with open(i, "r", encoding="utf-8") as input_file:
			text = input_file.read()						
			html = markdown.markdown(text, extras=['fenced-code-blocks', 'code-friendly'])
			output.append( html )
	else :
		pass
	output.append( """</div></body></html>""" )	
	with open(fichier_html, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
		toto = output_file.write(''.join(output))

	with open(fichier_html, "r", encoding="utf-8") as input_file:
		text = input_file.read()
		text = str(text)

	g = Github("lefebvre.prog@gmail.com", "Patatou59g")
	repo = g.get_repo("tamahaganes/site_statique")
	content = repo.get_contents("")			
	repo.create_file(fichier_html, "commit",text)
	print("Génération du fichier HTML")	



if __name__ == "__main__": 
    commande_markdown(),
    commande_html(),
    convertisseur()


