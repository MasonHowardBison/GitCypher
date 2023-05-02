import sys

preCypher = []
for line in sys.stdin:
    preCypher.append(line)
#Store stdin in preCypher


singleText=""
for line in preCypher:
    #Going line by line

    #Checking each line just to make sure the program only reads strings
    if(not(isinstance(line,str))):
        pass
    
    #Going char by char in line to check if it is a letter or not
    for char in line:
        if(char.upper()!=char.lower()):
            singleText+=char #Adding only letters to the singleText variable
    #Non-letters have no upper-case vs. lower-case so they will be the same
    #upper() or lower(), so those will be excluded.

#Uppercase all letters
singleText=singleText.upper()

#Assigning first argument (besides the file being run) to the var key.
try:
    key=sys.argv[1]
except:
    raise ValueError("Key is a required parameter.")
#Converting key to an int
key=int(key)

#Key must be between 0 and 25.
if(key<0 or key>25):
    raise ValueError("Key must be a number between 0 and 25.")


postCypher=""
for char in singleText:
    #Shifting each letter by key.
    outChar=chr(ord(char)+key)

    #If the resulting letter passes up Z, wrap around to the left by 26 values
    if(ord(outChar)>ord("Z")):
        outChar=chr(ord(outChar)-26)

    #Append the letter to postCypher
    postCypher+=outChar


outCypher=""
for i in range(len(postCypher)):
    #Append each letter to outCypher
    outCypher+=postCypher[i]
    #Every 50 letters (5 letters per block, 10 blocks per line), add a new line
    if((i+1)%50==0):
        outCypher+="\n"
    #Every 5 letters start a new block by adding a space
    elif((i+1)%5==0):
        outCypher+=" "
#Output the final encoded message.
print(outCypher)


