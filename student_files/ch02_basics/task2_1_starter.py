"""

      task2_1_starter.py   -   Python Basics Overview

      Reads elevation and population data from resources/cities15000.txt (a tsv file).


      Helpful hints:
      1. Examine the file cities15000.txt.  We will use a sequence to hold City typed NamedTuples
         Create the City typed NamedNuple definition such that it contains a name, population, elevation, and country.
         The population and elevation types will be treated as int types.

      2. Before reading from the file, create a Path() object to the file.

         Do this by wrapping the working_dir in a Path() object and then set city_data to the Path() / filename.
         (e.g., working_dir / 'cities15000.txt')

         Read from the data file into this data structure.  Be sure to use proper error handling
         as discussed in the materials.  The columns you should read are as follows: 1=name, 8=country (2-ltr code),
         14=population, 16=elevation (digital elevation model).  Column 0 is the geonameid.

         Use a 'with' control to open and close the file.

         Read lines from the file.  Each line will become a City typed NamedTuple.
         NOTE: you will need to split on a TAB ('\t') since this file is a tab-separated value file.

         Once complete, you should have a list of City typed NamedTuples.

      3. Verify you have read the file by checking the length of the list of City typed NamedTuples.
"""
from typing import NamedTuple
from pathlib import Path
import sys

working_dir = '../resources'
city_data = 'cities15000.txt'
cities = []

# Perform Part 1 here...