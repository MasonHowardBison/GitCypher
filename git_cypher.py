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

singleText=singleText.upper()
print(singleText)

key=sys.argv[1]

key=int(key)
if(key<0 or key>25):
    raise ValueError("Key must be between 0 and 25.")


postCypher=""
for char in singleText:
    outChar=chr(ord(char)+key)
    if(outChar.lower()==outChar.upper()):
        print(outChar)
        outChar=chr(ord(outChar)+26)
    postCypher+=outChar
print(postCypher)

outCypher=""
for i in range(len(postCypher)):
    outCypher+=postCypher[i]
    if(i+1%50==0):
        outCypher+="\n"
    elif(i+1%5==0):
        outCypher+=" "
print(outCypher)


