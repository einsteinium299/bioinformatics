newfile = 'y'
print("Starting script2.py\n")
while newfile == 'y':
    file = open(input("Open file: "))
    print("")
    total = 0
    biggest = 0
    file_type = "Nucleotides"

    DNA = ['A', 'T', 'C', 'G']
    aminoacid_dic = {'A':0, 'R':0, 'N':0, 'D':0, 'C':0, 'E':0, 'Q':0, 'G':0, 'H':0, 'I':0, 'L':0, 'K':0, 'M':0, 'F':0, 'P':0, 'S':0, 'T':0, 'W':0, 'Y':0, 'V':0}

    for line in file:
        line = line.strip()
        if not line.startswith(">"):
            #counting the length of the file
            length = len(line)
            total += length
            #Protein or DNA
            for letter in line:
                aminoacid_dic[letter] += 1
                if letter not in DNA:
                    file_type = "Aminoacids"

    print('This file contains a total of', total, file_type)

    if file_type == "Nucleotides":
        nuc_dic = {'A':aminoacid_dic['A'], 'C':aminoacid_dic['C'], 'T':aminoacid_dic['T'],'G':aminoacid_dic['G']} 
        print('Counter:', nuc_dic)
        G = nuc_dic['G']
        T = nuc_dic['T']
        C = nuc_dic['C']
        A = nuc_dic['A']
        x = (G + C) / (A + T + G + C) * 100
        print('G-C Percentage:',round(x),'% (rounded)')

        #calculating the most common nucleotide
        for k, v in nuc_dic.items():
            if v > biggest:
                biggest = v
        
        smallest = biggest
        for k, v in nuc_dic.items():
            if v < smallest:
                smallest = v
                
        for k,v in nuc_dic.items():
            if v == biggest:
                print(k, round((((v * 100) / total)))*'#', "<-- biggest value")
            elif v == smallest:
                print(k, round((((v * 100) / total)))*'#', "<-- smallest value")
            else:
                print(k, round((((v * 100) / total)))*'#')



    if file_type == "Aminoacids":
        print('Counter:',aminoacid_dic)

        for k, v in aminoacid_dic.items():
            if v > biggest:
                biggest = v

        smallest = biggest
        for k, v in aminoacid_dic.items():
            if v < smallest:
                smallest = v

        for k,v in aminoacid_dic.items():
            if v == biggest:
                print(k, round((((v * 100) / total))*2.5)*'#', '<-- biggest value')
            elif v == smallest:
                print(k, round((((v * 100) / total))*2.5)*'#', '<-- smallest value')  
            else:
                print(k, round((((v * 100) / total))*2.5)*'#')
    

    file.close()
    print('')
    newfile = input('Open new file? [y][n]: ')
    print('')
    
print('Script Finished!')
