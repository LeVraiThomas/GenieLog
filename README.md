# GenieLog
Parseur d’articles scientifiques en format texte

### Le programme relatif à cette version (sprint 3) comporte les fonctionnalités suivantes :
    - Créer un nouveau dossier
    - Pour chaque fichier pdf contenu dans le dossier ciblé :
      - Convertir le fichier pdf à l'aide pdf2text
      - Si l'option choisie est .txt
          - Créer un nouveau fichier .txt relatif au pdf
          - Récupérer le nom du fichier d’origine et l'écrire dans le fichier dans une ligne
          - Récupérer le titre du fichier d’origine et l'écrire dans le fichier dans une ligne
          - Récupérer le nom et l'adresse du/des auteur(s) et l'écrire dans le fichier dans une ligne
          - Récupérer le résumé ou abstract de l’auteur du fichier d’origine et l'écrire dans le fichier
          - Récupérer les références bibliographiques de l'article et l'écrire dans le fichier
      - Si l'option choisie est .xml
          - Créer un nouveau fichier .xml relatif au pdf
          - A l'intérieur d'une balise <article> :
              - Récupérer le nom du fichier d’origine et l'écrire dans le fichier dans une balise <preamble>
              - Récupérer le titre du fichier d’origine et l'écrire dans le fichier dans une balise <titre>
              - Récupérer le nom et l'adresse du/des auteur(s) et l'écrire dans le fichier dans une balise <auteur>
              - Récupérer le résumé ou abstract de l’auteur du fichier d’origine et l'écrire dans une balise <abstract>
              - Récupérer les références bibliographiques de l'article et l'écrire dans une balise <biblio>

##### Lancement du programme : python PdfParser.py -{t, x}
    - L'option -t entrainera la création de fichiers .txt
    - L'option -x entrainera la création de fichiers .xml
