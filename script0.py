capitalisation = ''

files = ['seq1.fna', 'seq2.fasta']

for file in files:
    cftr_gene = open(file)
    print("printing file:", file)
    for nucleotides in cftr_gene:
        if capitalisation == 'lowercase':
            nucleotides = nucleotides.strip()
            print(nucleotides.lower())
        elif capitalisation == 'uppercase':
            nucleotides = nucleotides.strip()
            print(nucleotides.upper())
        elif capitalisation == 'unchanged':
            print(nucleotides)
        else:
            print("You've entered a wrong value for capitalisation.")
            break

#Sources CFTR gene with mutations.

#seq1.fna = https://www.ncbi.nlm.nih.gov/gene/1080
#seq2.fasta = https://www.ebi.ac.uk/ena/browser/view/KU325498

