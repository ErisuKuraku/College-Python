import pandas as pd

file = open('misspellings.txt', 'r')
string = file.read()
print(string)
string = string.replace("->", ",")
arr = string.split()
print(arr)
df = pd.DataFrame(arr)
df.to_csv('misspellings.csv')



