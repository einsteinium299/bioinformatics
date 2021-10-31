# Solution to script8
# Date: 01-11-2021

# SOURCES:
# https://www.ncbi.nlm.nih.gov/protein/NP_000483.3?report=fasta
# https://www.ncbi.nlm.nih.gov/Structure/pdb/5UAK


def input_user():
    '''Getting input files from user and opening files'''

    # pdbfile = open(input('Your .pdb file\n> '), 'r')
    # sequence = open(input('Your .fasta file\n> '), 'r')

    pdbfile = open('mmdb_5UAK.pdb', 'r')
    sequence = open('sequence.fasta', 'r')
    outfile = open('helix_sheet.fasta', 'w')

    return pdbfile, sequence, outfile


def reading_fasta_file(sequence):
    ''' Storing fasta file in list '''

    sequence_list = []
    for sequence_line in sequence:
        sequence_line = sequence_line.strip()
        if sequence_line.isalpha():
            sequence_list.append(sequence_line)
    sequence.close()

    return sequence_list


def weight_atom(line):
    '''Counts the weight all atoms in a given line'''

    weight = 0
    atom = ''
    dic_atom_weight = {
        'C ':12.011, 'N ':14.007,
        'O ':15.999, 'S ':32.06, 
        'Se':78.971}

    atom = line[77:79]
    weight += dic_atom_weight[atom]

    return weight


def shorten_amino(line, sequence_list, line_count, amino_string, return_string):
    ''''
    Shortens three letter aminoacid name to it's single letter companion.
    Single aminoacid letters will be concatinated 
    and printed to the terminal at a lenght of 70.
    When the length does not reach 70 the line and count will be returned.
    '''

    # Slicing amino code from line
    multi_amino_code = line[19:70]

    # Splitting multi amino code to list
    seperate_amino = multi_amino_code.split()

    # Dictionary for translating multiple letter code for amino acid to a single letter code
    multi_to_single = {
        'ALA':'A', 'ARG':'R', 'ASN':'N', 'ASP':'D',
        'CYS':'C', 'GLU':'E', 'GLN':'Q', 'GLY':'G', 
        'HIS':'H', 'ILE':'I', 'LEU':'L', 'LYS':'K',
        'MET':'M', 'PHE':'F', 'PRO':'P', 'SER':'S',
        'THR':'T', 'TRP':'W', 'TYR':'Y', 'VAL':'V'}

    # Loop for going through every amino acid
    for item in seperate_amino:

        # amino_string is purely for terminal output
        amino_string += multi_to_single[item]
        # return_string is storing the entire amino string
        return_string += multi_to_single[item]

        if len(amino_string) >= 70:
            terminal_output(line_count, amino_string, sequence_list)
            line_count += 1
            amino_string = amino_string[70:]

    return line_count, amino_string, return_string


def terminal_output(line_count, amino_string, sequence_list):
    print('Line:' , str(line_count+1))
    print('PDB ⇾ ', amino_string[:70])
    print('SEQ ⇾ ', sequence_list[line_count])
    if sequence_list[line_count] == amino_string[:70]:
        print('🟢 Equal 🟢\n')
    else:
        print('🔴 NOT EQUAL 🔴\n')


def reading_file(pdbfile, sequence_list):
    '''Reading a pdbfile'''
    # Declaring start variables

    # WEIGHT
    u_counter = 0

    # SHORTEN_AMINO
    line_count = 0
    amino_string = ''
    return_string = ''

    # HELIX
    helix_amino_startpos = ''
    helix_amino_endpos = ''
    final_helix = ''

    # SHEET
    sheet_amino_startpos = ''
    sheet_amino_endpos = ''
    final_sheet = ''

    # TITLE
    title = []

    for line in pdbfile:
        #WEIGHT_ATOM
        if line.startswith('ATOM'):
            u_counter += weight_atom(line)

        #SHORTEN_AMINO
        elif line.startswith('SEQRES'):
            # Starting variables are stored outside the function so these will not be overwritten for every new line
            line_count, amino_string, return_string = shorten_amino(line, sequence_list, line_count, amino_string, return_string)

        elif line.startswith('HELIX'):
            # Slicing start and end position for helix
            helix_amino_startpos = line[21:25]
            helix_amino_endpos = line[33:37]
            # Slicing the HELIX sequence from return_string
            final_helix += return_string[int(helix_amino_startpos)-1:int(helix_amino_endpos)-1]

        elif line.startswith('SHEET'):
            # Slicing start and end position for sheet
            sheet_amino_startpos = line[22:26]
            sheet_amino_endpos = line[33:37]
            # Slicing the SHEET sequence from return_string
            final_sheet += return_string[int(sheet_amino_startpos)-1:int(sheet_amino_endpos)]

        elif line.startswith('TITLE'):
            title.append(line)

    pdbfile.close()
    return u_counter, final_helix, final_sheet, line_count, amino_string, title


def writing_file(final_helix, final_sheet, title, outfile):

    # Making appropriate title for the HELIX sequence
    new_title = ''
    new_title = title[0].strip() + title[1].strip()
    new_title = new_title.replace('2', '')
    new_title = " ".join(new_title.split())
    print(new_title.replace('TITLE', '').strip(), '- Helix', file=outfile)

    line = ''
    for letter in final_helix:
        line += letter
        if len(line) == 70:
            print(line, file=outfile)
            line = ''
    print(line, file=outfile)

    print(file=outfile)
    print(new_title.replace('TITLE', '').strip(), '- Sheet', file=outfile)
    line = ''
    for letter in final_sheet:
        line += letter
        if len(line) == 70:
            print(line, file=outfile)
            line = ''
    print(line, file=outfile)
    outfile.close()


def main():
    print('Script 8 is now running!\n')

    # Getting input from user, pdb file, fasta file and output file.
    pdbfile, sequence, outfile = input_user()

    # Reading fasta file
    sequence_list = reading_fasta_file(sequence)

    # Reading the pdb file
    u_counter, final_helix, final_sheet, line_count, amino_string, title = reading_file(pdbfile, sequence_list)

    # Printing information for the last line
    terminal_output(line_count, amino_string, sequence_list)

    # Writing HELIX, SHEET and TITLE to output file
    writing_file(final_helix, final_sheet, title, outfile)

    print('⚛ Atomic weight ⇾', round(u_counter),'u')
    
    print('Script has finished!')

main()
