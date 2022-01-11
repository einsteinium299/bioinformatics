def input_user():
    input_file = input('Input genbank file: ')
    output_file = input_file.replace(".gb", "_features.txt")
    
    if input("separated[1] or uppercased[2]\n>") == "2":
        uppercased = True
    else:
        uppercased = False

    return input_file, output_file, uppercased


def origin_seq(sequence):
    '''Makes from the ORIGIN sequence a pure sequence'''
    # Removes the ORIGIN section header
    sequence = sequence[1::]

    final_seq = ''

    for line in sequence:
        line = line.split()
        for split in line:
            if split.isalpha():
                final_seq += split
    return final_seq


def reading_file(input_file):
    genbank_file = open(input_file, 'r')

    # Setting loop variables to False
    origin_loop = False
    features_loop = False
    subsection = False
    definition_loop = False

    sequence = []
    features_list = []
    header = []

    for line in genbank_file:
        if line.startswith('DEFINITION'):
            definition_loop = True
        elif line.startswith('ACCESSION'):
            definition_loop = False
        elif line.startswith('FEATURES'):
            features_loop = True
        elif line.startswith('ORIGIN'):
            origin_loop = True
            features_loop = False
        elif line.startswith('//'):
            origin_loop = False

        if definition_loop:
            header.append(line)

        if features_loop:
            if not line[5:].startswith(' ') or subsection == True:

                features_list.append(line.strip())

                if not line[5:].startswith(' '):
                    subsection = True
                else:
                    subsection = False

        if origin_loop:
            sequence.append(line)

    # Removing section title
    features_list = features_list[1::]
    genbank_file.close()

    return sequence, features_list, header


def header_converter(header):

    final_header = ''
    for item in header:
        final_header += item.replace('DEFINITION', '').strip()
        if len(header) > 1:
            final_header += ' '

    final_header = final_header.strip()

    return final_header


def features_list_converter(features_list):
    new_list = []
    final_list = []

    for i in range(0, len(features_list), 2):
        combi = features_list[i] + features_list[i+1]
        new_list.append(combi)

    for line in new_list:
        line = line.split('/')
        header1, positions = line[0].split()
        header2 = line[1]

        list_item = header1 + ' /' + header2 + '--' + positions
        final_list.append(list_item)

    return final_list


def writing_file(final_seq, final_list, final_header, output_file, uppercased):
    writing_file = open(output_file, 'w')

    print(final_header, file=writing_file)

    for item in final_list:

        item = item.split('--')
        header = item[0]
        positions = item[1]
        print('\n>' + header, file=writing_file)
        coordinate = positions.split('..')

        #uppercase file
        if uppercased:

            if coordinate[0] == "1":
                if len(coordinate) == 1:
                    sequence = final_seq[0].upper() + final_seq[1:]
                else:
                    sequence = final_seq[int(coordinate[0])-1:int(coordinate[1])].upper()
            else:
                if len(coordinate) == 1:
                    sequence = final_seq[:int(coordinate[0])-1] + final_seq[int(coordinate[0])-1].upper()
                else:
                    sequence = final_seq[0:int(coordinate[0])-1] + final_seq[int(coordinate[0])-1:int(coordinate[1])].upper()

        #seperate file
        else:
            if len(coordinate) == 1:
                sequence = final_seq[int(coordinate[0])-1]
            else:
                sequence = final_seq[int(coordinate[0])-1:int(coordinate[1])]

        writing_sequence(sequence, writing_file)

    print('\n', file=writing_file)

    writing_file.close()


def writing_sequence(sequence, writing_file):
    print_seq = ''
    for letter in sequence:
        print_seq += letter
        if len(print_seq) == 60:
            print(print_seq, file=writing_file)
            print_seq = ''
    print(print_seq, file=writing_file)


def main():
    # Getting input files from user
    input_file, output_file, uppercased = input_user()

    # Reading through genbank file 
    sequence, features_list, header = reading_file(input_file)

    # Converting ORIGEN and FEATURES
    final_header = header_converter(header)
    final_seq = origin_seq(sequence)
    final_list = features_list_converter(features_list)

    # Writing out to file
    writing_file(final_seq, final_list, final_header, output_file, uppercased)

    print('File written to', output_file)

main()
