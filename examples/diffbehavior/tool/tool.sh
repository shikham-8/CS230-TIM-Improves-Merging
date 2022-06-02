#!/bin/bash

# first argument: original file
# second argument: refactor patch
# third argument: other patch
# fourth argument: old function name
# fifth argument: new function name

# ex: ./tool.sh a.py a.txt c.txt increment_list increment_list_refactored
cp $1 original_1.py
cp $1 original_2.py
cp $2 refactor.patch
cp $3 other.patch

patch original_1.py refactor.patch >/dev/null 
crosshair diffbehavior original_1.$5 original_2.$4 > first.out

patch original_1.py other.patch >/dev/null
patch original_2.py other.patch >/dev/null
crosshair diffbehavior original_1.$5 original_2.$4 > second.out

rm original_1.py
rm original_2.py
rm refactor.patch
rm other.patch

FIRST_OUT=`grep "No differences found." first.out`
SECOND_OUT=`grep "No differences found." second.out`

if [ "$FIRST_OUT" ]
then
	echo "good refactor"
else
	echo "bad refactor"
	cat second.out
fi
if [ "$SECOND_OUT" ]
then
	echo "no merge conflict"
else
	echo "yikes merge conflict"
fi

rm first.out
rm second.out
