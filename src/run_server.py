# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask, render_template

# définir le message secret
import build

SECRET_MESSAGE = "arbre" # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    #return SECRET_MESSAGE
    return render_template("connexion.html")



if __name__ == "__main__":
    # HTTP version
    app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    #app.run(debug=True, host="0.0.0.0", port=8081,ssl_context=(build.SERVER_PUBLIC_KEY_FILENAME, build.SERVER_PRIVATE_KEY_FILENAME))