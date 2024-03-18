"""

    08_argparse1.py

"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--greet', help='A howdya do.', required=True)
args = parser.parse_args()

print(args.greet)
