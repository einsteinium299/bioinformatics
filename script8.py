def counting_atoms():
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
            print(atom)
            count += dic_atom_weight[atom]
    print(count)
    
    myfile.close()
    outfile.close()

def main():
    counting_atoms()
main()
