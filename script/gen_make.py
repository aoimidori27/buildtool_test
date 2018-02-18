#!/usr/bin/python3
import sys

if __name__ == '__main__':
	if len(sys.argv) < 1:
		print("%s <target>" % sys.argv[0])
		exit(1)

	target = sys.argv[1]
	base_path = sys.argv[2]

	with open("Makefile", "w") as f:
		print("CC=gcc", file=f)
		print("SRC=$(sort $(shell find . -name \"*.c\"))", file=f)
		print("OBJ=$(SRC:.c=.o)", file=f)
		print("TARGET=%s" % target, file=f)
		print("", file=f)
		print(".PHONY:	all", file=f)
		print("all: $(TARGET)", file=f)
		print("", file=f)
		print("$(TARGET): $(OBJ)", file=f)
		print("\t$(CC) -o $@ $^", file=f)
		print("", file=f)
		print(".c.o:", file=f)
		print("\t$(CC) -o $@ -c $<", file=f)
		print("clean:", file=f)
		print("\trm -f $(TARGET) $(OBJ)", file=f)
