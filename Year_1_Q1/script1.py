newfile = 'y'
print("Starting script1.py")
while newfile == 'y':
    aminoacids = open(input("Input your file: "))
    total = 0
    accurate = 0
    aminoacid_dalton_weight= {'A':89,'R':174,'N':132,'D':133,'C':121,'E':146,'Q':147,'G':75,'H':155,'I':131, 'L': 131,'K':146,'M':149,'F':165,'P':115,'S':105,'T':119,'W':204,'Y':181,'V':117}
    #Source: http://fortiusbio.com/Aa_MW.html

    #counting the characters in the file
    for line in aminoacids:
        line = line.strip()
        if not line.startswith(">"):
            length = len(line)
            total = total + length
            #counting accurate weight
            for letter in line:
                value = aminoacid_dalton_weight[letter]
                accurate = value + accurate

    print("Total aminoacids:", total)
    #calculation molecular weight
    molecular_weight = total * 110
    print("Total inaccurate molecular weight:", molecular_weight, "Dalton")
    print('Total accurate molecular weight:', accurate, "Dalton")
    #calculating weight water
    weight_water = (total - 1) * 18.0153
    #calculating weight without water
    print('Total accurate molecular weight', "without H2O:", round((accurate - weight_water)), 'Dalton\n')
    aminoacids.close()
    newfile = input('open new file? [y][n]: ')

print('Script finished!')



