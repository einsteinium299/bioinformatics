def counting_atoms():
    '''Counting the total weight of all atoms in a pdb file'''
    
    myfile = open('mmdb_5UAK.pdb', 'r')

    dic_atom_weight = {
        'C ':12.011,
        'N ':14.007,
        'O ':15.999,
        'S ':32.06,
    }

    outfile = open('output.pdb', 'w')
    atom = ''
    lst = []
    count = 0
    for line in myfile:
        if line.startswith('ATOM'):
            atom = line[77:79]
            count += dic_atom_weight[atom]
        elif line.startswith('SEQRES'):
            shorten_amino(line)

    myfile.close()
    outfile.close()


def shorten_amino(text):
    ''''Shortens amino names'''
    multi_triplet = text[19:70]
    print(multi_triplet)


def main():
    counting_atoms()
main()
