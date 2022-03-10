# -----------------------------------------STAGE 1------------------------------------------------------

import os
import sys

args = sys.argv
if len(args) == 1:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(args[1]):
        for name in files:
            print(os.path.join(root, name))
