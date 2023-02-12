# Provide fn for interacting with the os such as reading ,writing files

import os
if(not os.path.exists("data")):
    os.mkdir("data")   # A data directory will be formed(A folder will be formed name data)
for i in range(0,20):    # in data folder 10 folder will be formed
    os.mkdir(f"data/Day{i+1}")