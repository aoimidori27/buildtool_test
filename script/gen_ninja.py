#!/usr/bin/python3
import sys
import os
import glob
import os

import ninja_syntax

def get_ninja_base(target, path):
	# ninja file
	ninjafile = os.path.join(path, 'build.ninja')
	variables = []
	builds = []
	rules = []
	objs = []

	# variables
	variables.append({'key': "cc", 'value': "gcc"})
	variables.append({'key': "cc", 'value': "gcc"})
	# rule statements
	rules.append({'name': "compile",
				'command':  "$cc -c $in -o $out"})
	rules.append({'name': "link",
				#'command': "$cc $in -o $out && echo \"done\""})
				'command': "$cc $in -o $out"})
	# build statements
	for root, dirnames, filenames in os.walk(path):
		for fname in filenames:
			src = os.path.join(root, fname)
			basename, ext = os.path.splitext(src)
			if ext != '.c':
				continue
			obj = basename + '.o'
			builds.append({'outputs': obj,
						'rule': "compile",
			   			'inputs': src})
			objs.append(obj)
	builds.append({'outputs': target,
				'rule': "link",
				'inputs': objs})
	return (ninjafile, variables, rules, builds)

if __name__ == '__main__':
	if len(sys.argv) < 1:
		print("%s <target> <path>" % sys.argv[0])
		exit(1)

	target = sys.argv[1]
	path   = sys.argv[2]

	ninjafile, variables, rules, builds = get_ninja_base(target, path)

	with open(ninjafile, 'w') as f:
		w = ninja_syntax.Writer(output=f)
		for _v in variables:
			w.variable(**_v)
		for _r in rules:
			w.rule(**_r)
		for _b in builds:
			w.build(**_b)

		w.default(target)
		w.build('all', 'phony', target)

