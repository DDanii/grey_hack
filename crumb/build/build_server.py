import sys
import os
import re

source_directory = os.path.join(os.path.dirname(__file__), "..")

sources = ["server_shared.src", "server_log.src", "server_install.src", "server_decrypt.src", "server_scan.src", "server_main.src"]

contents = ""
lines = []
for file in sources:
	with open( os.path.join(source_directory, file), "rt") as f:
		contents = contents + "\n" + f.read()

print(contents)