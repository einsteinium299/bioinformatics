# Solution to script8
# Date: 01-11-2021

def shorten_amino(line, sequence_list, count, amino_string):
    ''''Shortens three letter aminoacid name to it's single letter companion.
    Single aminoacid letters will be concatinated 
    and printed to the terminal at a lenght of 70.
    When the length does not reach 70 the line and count will be returned.
    '''

    multi_triplet = line[19:70]
    seperate_triplet = multi_triplet.split()

    multi_to_single = {
        'ALA':'A', 'ARG':'R', 'ASN':'N', 'ASP':'D',
        'CYS':'C', 'GLU':'E', 'GLN':'Q', 'GLY':'G', 
        'HIS':'H', 'ILE':'I', 'LEU':'L', 'LYS':'K',
        'MET':'M', 'PHE':'F', 'PRO':'P', 'SER':'S',
        'THR':'T', 'TRP':'W', 'TYR':'Y', 'VAL':'V'}

    for item in seperate_triplet:
        amino_string += multi_to_single[item]    
        if len(amino_string) >= 70:
            print('Line:' , str(count+1))
            print('PDB -> ', amino_string[:70])
            print('SEQ -> ', sequence_list[count])
            count += 1
            amino_string = amino_string[70:]       
    return count, amino_string

def weight_atom(line):
    '''Counts the weight all atoms in a given line'''
    weight = 0
    atom = ''
    dic_atom_weight = {
        'C ':12.011, 'N ':14.007,
        'O ':15.999, 'S ':32.06}

    atom = line[77:79]
    weight += dic_atom_weight[atom]
    return weight

def reading_file(sequence):
    ''' Storing fasta file in list '''
    sequence_list = []
    for sequence_line in sequence:
        sequence_line = sequence_line.strip()
        if sequence_line.isalpha():
            sequence_list.append(sequence_line)
    return sequence_list

def input_user():
    #names: mmdb_5UAK.pdb sequence.fasta

    pdbfile = open(input('Your .pdb file\n> '), 'r')
    sequence = open(input('Your .fasta file\n> '), 'r')
    return pdbfile, sequence


def main():
    print('Script 8 is now running!\n')
    pdbfile, sequence = input_user()
    # Declaring start variables
    weight = 0
    amino_string = ''
    count = 0

    sequence_list = reading_file(sequence)

    ### 

    #put this in read file
    for line in pdbfile:
        if line.startswith('ATOM'):
            weight += weight_atom(line)

        elif line.startswith('SEQRES'):
            count, amino_string = shorten_amino(line, sequence_list, count, amino_string)

#        elif line.startswith('HELIX'):
#        elif line.startswith('SHEET'):

    print('Line:', str(count+1))          
    print('PDB -> ', amino_string)
    print('SEQ -> ', sequence_list[-1], '\n')
    print('Atom weight:', round(weight),'u')
    
    ###

    pdbfile.close()
    sequence.close()

main()
