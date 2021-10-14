# https://www.ncbi.nlm.nih.gov/gene/

dic_P_counter = {
                'ATA':0, 'ATC':0, 'ATT':0, 'ATG':0,
                'ACA':0, 'ACC':0, 'ACG':0, 'ACT':0,
                'AAC':0, 'AAT':0, 'AAA':0, 'AAG':0,
                'AGC':0, 'AGT':0, 'AGA':0, 'AGG':0,                
                'CTA':0, 'CTC':0, 'CTG':0, 'CTT':0,
                'CCA':0, 'CCC':0, 'CCG':0, 'CCT':0,
                'CAC':0, 'CAT':0, 'CAA':0, 'CAG':0,
                'CGA':0, 'CGC':0, 'CGG':0, 'CGT':0,
                'GTA':0, 'GTC':0, 'GTG':0, 'GTT':0,
                'GCA':0, 'GCC':0, 'GCG':0, 'GCT':0,
                'GAC':0, 'GAT':0, 'GAA':0, 'GAG':0,
                'GGA':0, 'GGC':0, 'GGG':0, 'GGT':0,
                'TCA':0, 'TCC':0, 'TCG':0, 'TCT':0,
                'TTC':0, 'TTT':0, 'TTA':0, 'TTG':0,
                'TAC':0, 'TAT':0, 'TAA':0, 'TAG':0,
                'TGC':0, 'TGT':0, 'TGA':0, 'TGG':0}

dic_P = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

file1 = open('sequence_N.fasta', 'r')
fileout = open('out.fasta', 'w')


codon=''
aminoacids=''
x = ''

for line in file1:
    line = line.strip()
    if not line.startswith('>'):
        for letter in line:
            codon += letter
            if len(codon) == 3:
                dic_P_counter[codon] += 1
                for codon1, aminoacid1 in dic_P.items():
                    for codon2, aminoacid2 in dic_P.items():
                        if aminoacid1 == aminoacid2:
                            x += [codon]
            codon = ''
print(x)
                #aminoacids += dic_P[codon]
                # if len(aminoacids) == 70:
                    # print(aminoacids, file=fileout)
                    # aminoacids = ''
                
               

file1.close()



# maxi = 0

# amino = 'A'
# for k, v in dic_P_counter.items():
#     for codon2, amino in dic_P.items():     
#         if v > maxi:
#             if k in ['GCA', 'GCC', 'GCG', 'GCT']:
#                 maxi = v

# print(maxi)

# print(dic_P_counter)

# for k1, v1 in dic_P_counter.items():
#     for codon, aminoacid in dic_P.items():
#     for codon2, aminoacid2 in dic_P.items():
#         if 
#             if aminoacid == aminoacid2:


#print(dic_P_counter)


#voor elk aminozuur:
#   loop door de codontabel:
#       als amino uit de codontabel hetzelfde is als:

