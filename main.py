
import os
import sys
import time
from commande import commande_markdown, commande_html, liste_fichier_md, liste_fichier_html,convertisseur
from os import listdir
from os.path import isfile, join
import markdown

liste_md = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
liste_html = [f for f in listdir(sys.argv[2]) if isfile(join(sys.argv[2], f))]

print("voici la liste des fichiers markdown du dossier")
commande_markdown(liste_md)
liste_fichierMd_insertion = []
liste_fichierHtml_insertion = []


test = True
boucle_md = True
boucle_html = True
boucle_test = True

while boucle_md:
	
	try:
		saisie = int(input("veuillez choisir les documents markdown à ajouter au template html :"))	
		saisie = int(saisie)
		saisie = liste_fichier_md[saisie] 
		liste_fichierMd_insertion.append(saisie)

	except (ValueError, IndexError) as e:
		print ("veuillez indiquer le chiffre correspondant à l'article")
		continue
	while boucle_test :	
		rep = input("voulez-vous ajouter d'autre article ? : oui / non :")	
		if rep == "oui":
			break
		elif rep =="non":
			print (f"Voici la liste des fichiers markdown à insérer : {liste_fichierMd_insertion}")
			boucle_test = False
			boucle_md = False
		else :
			print(" veuillez indiquer oui ou non")
			pass

print("voici la liste des fichiers markdown du dossier")

commande_html(liste_html)

while boucle_html:
	try :
		fichier_html = int(input("veuillez choisir le numéro du template Html souhaité :"))
		fichier_html = liste_fichier_html[fichier_html]
		liste_fichierHtml_insertion.append(fichier_html)
	except (ValueError, IndexError) as e:
		print ("veuillez indiquer le chiffre correspondant à au template")
		continue
	print (f"Voici la liste des fichiers markdown à insérer : {liste_fichierHtml_insertion}")
	boucle_html = False

convertisseur(liste_fichierMd_insertion, liste_fichierHtml_insertion[0])



"""
import os
import sys
import time
from commande import commande_markdown, commande_html, liste_fichier_md, liste_fichier_html
from os import listdir
from os.path import isfile, join
from CodeHtml import CodeHtml
import markdown

output = [CodeHtml]

liste_md = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
liste_html = [f for f in listdir(sys.argv[2]) if isfile(join(sys.argv[2], f))]

print("voici la liste des fichiers markdown du dossier")
commande_markdown(liste_md)

commande_html(liste_html)

liste_fichierMd_insertion = []
liste_fichierHtml_insertion = []

time.sleep(2)
test = True
boucle_md = True
boucle_html = True

while boucle_md:
	saisie = int(input("veuillez choisir les documents markdown à ajouter au template html :"))
	saisie = liste_fichier_md[saisie] 
	liste_fichierMd_insertion.append(saisie)	
	rep = input("voulez-vous ajouter d'autre article ? : O / N :")	
	if rep == "o":
		pass
	else:
		print (f"Voici la liste des fichiers markdown à insérer : {liste_fichierMd_insertion}")
		boucle_md = False


print("voici la liste des fichiers markdown du dossier")
commande_html(liste_html)

while boucle_html:				
	fichier_html = int(input("veuillez choisir le numéro du template Html souhaité :"))
	fichier_html = liste_fichier_md[fichier_html]
	boucle_html = False
	test = False



for i in liste_fichierMd_insertion:
	with open(i, "r", encoding="utf-8") as input_file:
		text = input_file.read()						
		html = markdown.markdown(text, extras=['fenced-code-blocks', 'code-friendly'])
		output.append( html )
		output.append( ""</div></body></html>"" )
	
	with open("index.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
		toto = output_file.write(''.join(output))				
else :
	pass
"""