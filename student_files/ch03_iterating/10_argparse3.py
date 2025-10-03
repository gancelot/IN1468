"""

    Run as follows:

    python 10_argparse3.py (--start | --stop)

"""
import argparse

parser = argparse.ArgumentParser(description='Personal characteristics')
mutual_group = parser.add_mutually_exclusive_group()
mutual_group.add_argument('--start', action='store_true')
mutual_group.add_argument('--stop', action='store_true')
args = parser.parse_args()
print(args)
