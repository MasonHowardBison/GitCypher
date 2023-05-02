import sys

preCypher = []
for line in sys.stdin:
    preCypher.append(line)

print(preCypher)

singleText=""
for line in preCypher:
    if(not(isinstance(line,str))):
        pass
    for char in line:
        if(char.upper()!=char.lower()):
            singleText+=char
print(singleText)
singleText=singleText.upper()

key=sys.argv[0]
key=int(key)
if(key<0 or key>25):
    raise ValueError("Key must be between 0 and 25.")


postCypher=""
for char in singleText:
    outChar=char+key
    if(outChar.lower()!=outChar.upper()):
        outChar-=26
    postCypher+=outChar
print(postCypher)
