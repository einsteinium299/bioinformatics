def input_user():
    input_file = open('sequence.gb', 'r')
    return input_file


def origin_seq(sequence):
    sequence = sequence[1::]
    final_seq = ''

    for line in sequence:
        line = line.split()
        for split in line:
            if not split.isdigit():
                final_seq += split

def reading_file(input_file):
    origen_loop = False
    features_loop = False
    subsection = False

    sequence = []
    features_list = []


    for line in input_file:
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

    return sequence, features_list

def printing_terminal_output(sequence, features_list):
    new_list = []

    features_list = features_list[1::]
    # print(len(features_list))

    new_line = ''
    count = 0

    for line in features_list:
        # print(line)
        new_line += line
        count += 1
        if count == 2:
            new_list.append(new_line)
            count = 0
            new_line = ''

    for line in new_list:
        print(line)


def main():
    input_file = input_user()

    sequence, features_list = reading_file(input_file)
    
    origin_seq(sequence)

    printing_terminal_output(sequence, features_list)

main()
