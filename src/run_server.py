# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"

CERTIFICATE_FILENAME = RESOURCES_DIR + "certif.pem"


# définir le message secret
SECRET_MESSAGE = "arbre" # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    app.run(debug=True, host="0.0.0.0", port=8081,ssl_context=(SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME))