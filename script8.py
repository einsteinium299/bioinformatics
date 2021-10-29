# Solution to script8
# Date: 01-11-2021

# SOURCES:
# https://www.ncbi.nlm.nih.gov/protein/NP_000483.3?report=fasta
# https://www.ncbi.nlm.nih.gov/Structure/pdb/5UAK

def shorten_amino(line, sequence_list, count, amino_string, return_string):
    ''''
    Shortens three letter aminoacid name to it's single letter companion.
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
        return_string += multi_to_single[item]    
        if len(amino_string) >= 70:
            print('Line:' , str(count+1))
            print('PDB ⇾ ', amino_string[:70])
            print('SEQ ⇾ ', sequence_list[count])
            if sequence_list[count] == amino_string[:70]:
                print('🟢 Equal 🟢\n')
            else:
                print('🔴 NOT EQUAL 🔴\n')
            count += 1
            amino_string = amino_string[70:]  

                 
    return count, amino_string, return_string

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

def reading_file(sequence):
    ''' Storing fasta file in list '''
    sequence_list = []
    for sequence_line in sequence:
        sequence_line = sequence_line.strip()
        if sequence_line.isalpha():
            sequence_list.append(sequence_line)
    return sequence_list

def input_user():
    # pdbfile = open(input('Your .pdb file\n> '), 'r')
    # sequence = open(input('Your .fasta file\n> '), 'r')

    pdbfile = open('mmdb_5UAK.pdb', 'r')
    sequence = open('sequence.fasta', 'r')
    outfile = open('helix_sheet.fasta', 'w')
    return pdbfile, sequence, outfile

# def writing_file
# def reading_file

def main():
    print(".---------.\n| script8 |\n'---------'")
    print('Script 8 is now running!\n')

    pdbfile, sequence, outfile = input_user()

    # Declaring start variables
    weight = 0
    amino_string = ''
    count = 0
    return_string = ''
    sequence_list = reading_file(sequence)
    helix_amino_startpos = ''
    helix_amino_endpos = ''
    final_helix = ''
    sheet_amino_startpos = ''
    sheet_amino_endpos = ''
    final_sheet = ''
    title = []

    #put this in read file
    for line in pdbfile:
        if line.startswith('ATOM'):
            weight += weight_atom(line)

        elif line.startswith('SEQRES'):
            count, amino_string, return_string = shorten_amino(line, sequence_list, count, amino_string, return_string)

        elif line.startswith('HELIX'):
            helix_amino_startpos = line[21:25]
            helix_amino_endpos = line[33:37]
            final_helix += return_string[int(helix_amino_startpos)-1:int(helix_amino_endpos)-1]
        
        elif line.startswith('SHEET'):
            sheet_amino_startpos = line[22:26]
            sheet_amino_endpos = line[33:37]
            final_sheet += return_string[int(sheet_amino_startpos)-1:int(sheet_amino_endpos)]
        elif line.startswith('TITLE'):
            title.append(line)


    # This part is for the last line
    print('Line:', str(count+1))          
    print('PDB ⇾ ', amino_string)
    print('SEQ ⇾ ', sequence_list[-1])
    
    if amino_string == sequence_list[-1]:
        print('🟢 EQUAL 🟢\n')
    else:
        print('🔴 NOT EQUAL 🔴\n')
    # -------------------------

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

    pdbfile.close()
    sequence.close()
    outfile.close()

    print('⚛ Atomic weight ⇾', round(weight),'u')
    print('Script has finished!')
main()
