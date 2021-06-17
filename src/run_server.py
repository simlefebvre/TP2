# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask, render_template, request
import build
import tools.core
from socket import *

#Récupération de l'adresse IP locale de l'odinateur et génération lien pour controler identifiant et mot de passe
ip = "https://"+ gethostbyname(gethostname()) + ":8081/controler"

# définir le message secret
SECRET_MESSAGE = "arbre" # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return render_template("index.html", IP=ip)


@app.route('/controler',methods = ['POST'])
def controler():
  result = request.form
  id = result['id']
  mdp = result['mdp']
  if(tools.core.connexion(id,mdp,tools.core.connexionSQL())):
    #MDP valide
    return render_template("afficherMDP.html", mdp=SECRET_MESSAGE)
  else:
    #MDP non valide
    return render_template("erreurMDP.html", IP=ip)



if __name__ == "__main__":
    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    app.run(debug=True, host="0.0.0.0", port=8081,ssl_context=(build.SERVER_PUBLIC_KEY_FILENAME, build.SERVER_PRIVATE_KEY_FILENAME))

