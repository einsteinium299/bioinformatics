def input_user():
    input_file = 'sequence.gb'
    return input_file


def origin_seq(sequence):
    sequence = sequence[1::]
    final_seq = ''

    for line in sequence:
        line = line.split()
        for split in line:
            if not split.isdigit():
                final_seq += split
    # print(final_seq.upper())
    return final_seq

def reading_file(input_file):
    genbank_file = open(input_file, 'r')

    origen_loop = False
    features_loop = False
    subsection = False

    sequence = []
    features_list = []


    for line in genbank_file:
        # print(line, end='')
        
        if line.startswith('FEATURES'):
            features_loop = True

        elif line.startswith('ORIGIN'):
            origen_loop = True
            features_loop = False
        
        elif line.startswith('//'):
            origen_loop = False

        if features_loop == True:
            if not line[5:].startswith(' ') or subsection == True:
                # print(line.strip())
                features_list.append(line.strip())

                if not line[5:].startswith(' '):
                    subsection = True
                else:
                    subsection = False

        if origen_loop == True:
            sequence.append(line)

    features_list = features_list[1::]
    genbank_file.close()

    return sequence, features_list

def printing_terminal_output(sequence, features_list, final_seq):
    new_list = []
    # print(len(features_list))

    new_line = ''
    count = 0

    for line in features_list:
        # print(line)
        new_line += line
        count += 1
        if count == 2:
            new_list.append(' ' + new_line)
            count = 0
            new_line = ''

    for line in new_list:
        line = line.split('/')
        header1, header2 = line[0].split()
        header3 = line[1]
        newlist = header1, header2, header3
        # line = line[0].split().append(line[1])
        # print(newlist)
        header = '>' + newlist[0] + ' /' + newlist[2]
        # print(header)

        positions = newlist[1]
        print(header)

        if '..' in positions:

            pos1, pos2 = positions.split('..')
            print(pos1, pos2)
            print(final_seq[int(pos1)-1:int(pos2)])

        else:
            pos1 = positions
            print(pos1)
            print(final_seq[int(pos1)-1::])

def main():
    input_file = input_user()

    sequence, features_list = reading_file(input_file)

    final_seq = origin_seq(sequence)

    printing_terminal_output(sequence, features_list, final_seq)

main()
