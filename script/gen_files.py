#!/usr/bin/python3
import sys
import os
import shutil

def create_main_src():
	with open('src/main.c', 'w') as f:
		print('#include <stdio.h>', file=f)
		for i in range(n):
			print('#include "test%d/test.h"' % i, file=f)
		print("", file=f)
		print('int main() {', file=f)
		print('\tprintf("hello, wolrd!\\n");', file=f)
		for i in range(n):
			print(('\ttest%d();' % i), file=f)
		print('}', file=f)

def create_test_src(i, basedir='src'):
	func_name = 'test'+str(i)
	dirname = os.path.join(basedir, func_name)
	src_fname = os.path.join(dirname, 'test.c')
	hdr_fname = os.path.join(dirname, 'test.h')
	os.mkdir(dirname)
	print("%s is created." % dirname);
	with open(src_fname, 'w') as f:
		print('#include <stdio.h>', file=f)
		print('#include "test.h"', file=f)
		print(file=f)
		print('void %s(void)' % func_name, file=f)
		print('{', file=f)
		print('\tprintf("%s\\n", __func__);', file=f)
		print('}', file=f)
	with open(hdr_fname, 'w') as f:
		print('void %s(void);' % func_name, file=f)

n = int(sys.argv[1])

if os.path.exists('src'):
	shutil.rmtree('src')

# create source directory
os.mkdir('src')

# create main.c
newline = '\n'
create_main_src()

# create subdirectories
for i in range(n):
	create_test_src(i)
