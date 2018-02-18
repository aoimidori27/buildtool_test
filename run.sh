#!/bin/bash

function build_test {
	tool=$1
	target=mymain

	python3 gen_${tool}.py ${target} . > /dev/null

	echo -e "cold start (full build from a fresh tree)"
	command time -f %e ${tool} 1> /dev/null

	echo -e "full rebuild (change all sources and rebuild)"
	find . -name "*.c" -exec sed -i {} -e 's/printf("/printf("tmp/' \;
	command time -f %e ${tool} 1> /dev/null

	echo -e "rebuild leaf"
	find . -name main.c -exec sed -i {} -e 's/printf("/printf("tmp/' \;
	command time -f %e ${tool} 1> /dev/null

	echo -e "nothing to change"
	command time -f %e ${tool} 1> /dev/null
}

declare -a counts=(10 100 1000)
declare -a tools=(make scons ninja)
for tool in "${tools[@]}"; do
	echo ======================================================================
	for n in "${counts[@]}"; do
		echo run $tool test \(count = $n\)
		echo ----------------------------------------------------------------------
		python3 script/gen_files.py ${n} > /dev/null
		cp script/gen_${tool}.py src/
		cd src
		build_test ${tool}
		cd ..
		rm -rf src
	done
done
