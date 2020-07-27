"""

f = open("myfile.txt", "x")

f1 = open("myfile1.txt", "w")
"""
import os
if os.path.exists("myfile1.txt"):
  os.remove("myfile1.txt")
else:
  print("The file does not exist")