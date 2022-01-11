def counter(files):
    codon_dict = {
            'ATA': 0, 'ATC': 0, 'ATT': 0, 'ATG': 0,
            'ACA': 0, 'ACC': 0, 'ACG': 0, 'ACT': 0,
            'AAC': 0, 'AAT': 0, 'AAA': 0, 'AAG': 0,
            'AGC': 0, 'AGT': 0, 'AGA': 0, 'AGG': 0,
            'CTA': 0, 'CTC': 0, 'CTG': 0, 'CTT': 0,
            'CCA': 0, 'CCC': 0, 'CCG': 0, 'CCT': 0,
            'CAC': 0, 'CAT': 0, 'CAA': 0, 'CAG': 0,
            'CGA': 0, 'CGC': 0, 'CGG': 0, 'CGT': 0,
            'GTA': 0, 'GTC': 0, 'GTG': 0, 'GTT': 0,
            'GCA': 0, 'GCC': 0, 'GCG': 0, 'GCT': 0,
            'GAC': 0, 'GAT': 0, 'GAA': 0, 'GAG': 0,
            'GGA': 0, 'GGC': 0, 'GGG': 0, 'GGT': 0,
            'TCA': 0, 'TCC': 0, 'TCG': 0, 'TCT': 0,
            'TTC': 0, 'TTT': 0, 'TTA': 0, 'TTG': 0,
            'TAC': 0, 'TAT': 0, 'TAA': 0, 'TAG': 0,
            'TGC': 0, 'TGT': 0, 'TGA': 0, 'TGG': 0,
            }

    triplet = ""
    for file in files:
        opend_file = open(file)
        for line in opend_file:
            line = line.strip()
            if not line.startswith('>'):
                for character in line:
                    triplet += character
                    if len(triplet) == 3:
                        codon_dict[triplet] +=1
                        triplet = ""
        opend_file.close()
    print('\nTotal count triplets:')
    print(codon_dict)
    
    return codon_dict

def amino_to_nuc(inputfile, outputfile, dictionary):
    '''Translating aminoacid to nucleotide'''
    nucs = ''
    for line in inputfile:
        line = line.rstrip()
        if line.startswith('>'):
            print(line, '- Nucleotide translation', file=outputfile)
        else:
            for char in line:
                nucs += dictionary[char]
                if len(nucs) >= 70:
                    print(nucs, file=outputfile)
                    nucs = ''
    print(nucs, file=outputfile)

def most_common(dictionary_max):
    '''Making dictionary with most common'''
    final_dic = {}
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

    for nuc1 in dictionary_max.keys():
        for nuc2, amino in dic_P.items():
            if nuc1 == nuc2:
                final_dic[amino] = nuc1
    return final_dic

def dictionary_most_common(counter_dictionary):
    ''' 'ATA ATC ATT' : 'I' door de codonnen zo op te stellen kan er
    een list worden gemaakt met .split(), van de codonnen die gelijk staan aan
    een aminozuur'''
    codon_table = {
                    'I':'ATA ATC ATT', 'M':'ATG' ,
                    'T':'ACA ACC ACG ACT',
                    'N':'AAC AAT', 'K':'AAA AAG' ,
                    'S':'AGC AGT' , 'R':'AGA AGG' ,
                    'L':'CTA CTC CTG CTT',
                    'P':'CCA CCC CCG CCT',
                    'H':'CAC CAT', 'Q':'CAA CAG',
                    'R':'CGA CGC CGG CGT',
                    'V':'GTA GTC GTG GTT' ,
                    'A':'GCA GCC GCG GCT',
                    'D':'GAC GAT' , 'E':'GAA GAG' ,
                    'G':'GGA GGC GGG GGT' ,
                    'S':'TCA TCC TCG TCT' ,
                    'F':'TTC TTT' ,  'L':'TTA TTG',
                    'Y':'TAC TAT' ,  '_':'TAA TAG TGA',
                    'C':'TGC TGT' ,  'W':'TGG'
        }  
        
    #puts aminoacids into list
    keys = codon_table.keys()
    key_list = list(keys)


    max_dic = {}
    for item in key_list:
        #Codon frequencies from aminoacids, if triplets are higher than the maximum, then the highest triplet frequences will be determined.
        top_count = 0
        top_codon = ''
        codon = codon_table[item]
        codon = codon.split()
        for characters in codon:
            if counter_dictionary[characters] > top_count:
                top_count = counter_dictionary[characters]
                top_codon = characters
                max_dic[characters] = top_count

    return max_dic

def main():
    input_nuc = input('Import nucleotide files to count most common triplets\n> ').split()
    open_amino = input('Aminoacid file to translate\n> ')
    input_amino = open(open_amino, 'r')

    #Automatic new output file handle
    new_file_handle = open_amino.split('.')
    final_file_handle = new_file_handle[0] + '_reversed_mRNA.fasta'
    output_file = open(final_file_handle, 'w')

    #Counting frequency of nucleotides
    codon_dict = counter(input_nuc)

    #Most common nuceotide connected with aminoacid
    max_dic = dictionary_most_common(codon_dict)

    #Most common nucleotide
    final_dic = most_common(max_dic)

    #Writing & translating aminoacid file to a nucleotide file
    amino_to_nuc(input_amino, output_file, final_dic)

    input_amino.close()
    output_file.close()
    print('\nScript finished!')
main()
