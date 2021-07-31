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
import variable
#Récupération de l'adresse IP locale de l'odinateur et génération lien pour controler identifiant et mot de passe
ip = "http://"+ gethostbyname(gethostname()) + ":8081"

# définir le message secret
SECRET_MESSAGE = "arbre" # A modifier
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return render_template("index.html", IP=ip)

@app.route('/',methods = ['POST'])
def controler():

  result = request.form
  if variable.compteur != 0:
    cc = result['captcha']
    if cc != variable.cap:
      return render_template("erreurCC.html")
    
  id = result['id']
  mdp = result['mdp']
  connecte = tools.core.connexion(id,mdp,tools.core.connexionSQL())
  if(connecte == 1 ):
    #MDP valide
    return render_template("afficherMDP.html", mdp=SECRET_MESSAGE)
  elif (connecte == 0 ):
    #MDP non valide
    tools.core.reloadCaptchat()
    return render_template("erreurMDP.html", IP=ip)
  elif (connecte == 2):
    tools.core.reloadCaptchat()
    return render_template("blockMDP.html", IP=ip)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    tools.core.reloadCaptchat()
    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    app.run(debug=True, host="0.0.0.0", port=8081,ssl_context=(build.SERVER_PUBLIC_KEY_FILENAME, build.SERVER_PRIVATE_KEY_FILENAME))

