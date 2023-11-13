###this script will turn bedgraphs from CnR normaliztion into bed files
###that can be accurately used for making tag directories in homer
###the premise is that we will round our bedgraph score to a whole number
###and then print each row n times where n is the score for that row
###this will give a rough version of a bed file that accounts for all the enrichment in the genome
###this is my first time coding in python so we are learning!

import	sys
import numpy as np
import pandas as pd

f = pd.read_table(sys.argv [1], header=None)
f.columns = ['chr', 'start', 'end', 'score']
f.score=round(f.score)
f.insert(3, 'strand', '+')
f.to_csv(sys.argv [2], header=False, index=False, sep='\t')
