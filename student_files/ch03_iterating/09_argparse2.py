"""

    09_argparse2.py

    Run with arguments:
    -n (--filename) the filename of the file to read
    -c (--columns)  defines column names and column numbers
                    (e.g., {name:(1, str), population:(14, int), elevation:(16, int), country:(8, str)})
    -s (--sep)      to define file separator character, default is ','
    -q (--query)    the search term to search for
    -f (--field)    the field to search for the search term
    
    Example use:
    python 09_argparse2.py -n ../resources/cities15000.txt -c name:(1,str) population:(14,int) -q "new york" -f name -s \t

"""
import argparse
import sys

import search

conversions = {'int': int, 'float': float, 'str': str}


def get_args():
    parser = argparse.ArgumentParser(description='Reads from a file, finds occurrences.')
    parser.add_argument('-n', '--filename', required=True, help='The file to search')
    parser.add_argument('-c', '--columns', nargs='*', required=True, help='The columns to use, ex: name:(1,str) pop:(14,int')
    parser.add_argument('-s', '--sep', default=',', help='File separator character')
    parser.add_argument('-q', '--query', help='Query term to search for')
    parser.add_argument('-f', '--field', help='Column to search within')

    args = parser.parse_args()
    args.sep = args.sep.encode('utf-8').decode('unicode_escape')   # allows for values like '\t'

    # the following converts --columns value into a dict of int:tuple values format...
    try:
        parsed_cols = {}
        for kv in args.columns:                                   # ex: name:(1,str)
            key, value = kv.split(':')                            # ex: name, (1,str)
            col, typ = value.strip('(').strip(')').split(',')     # ex: 1, str
            parsed_cols[key] = (int(col), conversions[typ])       # less secure, replace conversions[typ] with eval(typ)
        args.columns = parsed_cols

    except Exception as err:
        print(f'Check column formatting.  No extra spaces are allowed. \n{err}', file=sys.stderr)
        sys.exit(1)

    return args


args = get_args()

search.read_data(args.filename, args.columns, args.sep)
search.search(args.query, args.field)
