#! C:\Users\joris\AppData\Local\Programs\Python\Python38\python.exe


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

# Read file
def read_file(filename):
    filehandle = open(filename)
    for line in filehandle:
        if line.startswith('>'):
            header = line.rstrip()
            sequence = ''
        else:
            sequence += line.rstrip()
    filehandle.close()

    return sequence, header

def check_if_nuc(sequence):
    nuc_sequence = True
    for char in sequence:
        if char not in 'ATGC':
            nuc_sequence = False
            break
    return nuc_sequence

def make_protein(sequence, start_position):
    protein_str = ''
    for position in range(start_position, len(sequence), 3):
        triplet = sequence[position:position+3]
        if len(triplet) == 3:
            protein_str += dic_P[triplet]
    return protein_str

def write_outputfile(protein_str, outputfilehandle, header):
    print(header, file = outputfilehandle)
    for position in range(0, len(protein_str), 70):
        print(protein_str[position:position+70], file = outputfilehandle)
    print(' ', file=outputfilehandle)


def main():
    filename = input('Geef hier de filenaam weer gescheiden met een spatie: ')
    filelist = filename.split()

    outputfilename = input('Geef hier de naam van het outputbestand: ')
    outputfilehandle = open(outputfilename, 'w')

    start_position = input("Geef hier de startpositie van de eerste codon aan: ")
    start_position = int(start_position) - 1

    for filename in filelist:
        sequence, header = read_file(filename)
        nuc_sequence = check_if_nuc(sequence)
        if nuc_sequence == True:
            protein_str = make_protein(sequence, start_position)
            write_outputfile(protein_str, outputfilehandle, header)
        else:
            print('Warning!, one or multiple files contain no nucleotides and has not been writen to the outputfile.')
    outputfilehandle.close()

main()
