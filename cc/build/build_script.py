import sys
import os
import re

source_directory = os.path.join(os.path.dirname(__file__), "..")

boat_source = "boat.src"
src_funcs = [file for file in os.listdir(source_directory) if (os.path.isfile(os.path.join(source_directory, file)) and file != boat_source and file.startswith("func_"))]
src_funcs.sort()

src_cmds = [file for file in os.listdir(source_directory) if (os.path.isfile(os.path.join(source_directory, file)) and file != boat_source and file.startswith("cmd_"))]
src_cmds.sort()

sources = src_funcs + src_cmds + ["main.src"]

contents = ""
lines = []
for file in sources:
	with open( os.path.join(source_directory, file), "rt") as f:
		contents = contents + "\n" + f.read()

with open(os.path.join(source_directory, boat_source), "rt") as f:
	lines = f.read().splitlines()

boat_script = "[\n"
for l in lines:
	boat_script = boat_script + "\"" + l.replace("\"", "\"\"") + "\",\n"
boat_script = boat_script + "].join(char(10))"

contents = contents.replace("\"THIS_IS_BOAT_SCRIPT_SOURCE\"", boat_script).replace("_BOAT_VERSION_", "1.0.3")
print(contents)