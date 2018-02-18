#!/usr/bin/python3

import sys
import os
import glob

if __name__ == '__main__':
	if len(sys.argv) < 1:
		print("%s <target> <path>" % sys.argv[0])
		exit(1)
	target = sys.argv[1]
	path = sys.argv[2]
	with open("SConstruct", "w") as f:
		print("import os", file=f)
		print("import glob", file=f)
		print("", file=f)
		print("env = Environment()", file=f)
		print("", file=f)
		print("source_files = []", file=f)
		print("", file=f)
		print("for root, dirnames, filenames in os.walk(\"%s\"):" % path, file=f)
		print("  for fname in filenames:", file=f)
		print("    _, ext = os.path.splitext(fname)", file=f)
		print("    if ext != '.c':", file=f)
		print("      continue", file=f)
		print("    src = os.path.join(root, fname)", file=f)
		#print("		globStr = \"%s/*.c*\" % dirname", file=f)
		print("    source_files.append(src)", file=f)
		print("", file=f)
		#print("globStr = \"./*.c*\"", file=f)
		#print("source_files.append(glob.glob(globStr))", file=f)
		print("", file=f)
		print("env.Program(target=\"%s\", source=source_files)" % target, file=f)
