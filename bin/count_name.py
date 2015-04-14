i!/usr/bin/env python

import sys

def count_name(filename, protein_name):
    input_file = open(filename, "r")
    count = 0
    pro = str(protein_name)
    for line in input_file:
        if line.rstrip() == pro:
            count += 1
    return count


#filename = '/home/sanbi/Dropbox/python/coding/Python/PythonTest/name.txt'
#protein_name = 'IREB2'
#print "Dup: is", count_name(filename,protein_name)

if len(sys.argv) != 3:
    sys.exit("Usage: count_name.py <protein names file> <protein name>")


filename = sys.argv[1]
protein_name = sys.argv[2]
name_count = count_name(filename, protein_name)
print protein_name, name_count
#assert count_name('names.txt', 'IREB2') == 3
#assert count_name('names.txt', 'RXRG') == 6
