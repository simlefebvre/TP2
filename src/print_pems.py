# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

import pem

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"

cert = pem.parse_file(CA_PUBLIC_KEY_FILENAME)
print(cert)
print(str(cert[0]))
