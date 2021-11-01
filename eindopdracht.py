def input_user():
    input_file = open('sequence.gb', 'r')
    return input_file

def reading_file(input_file):
    origen_loop = False
    features_loop = False

    sequence = []
    final_seq = ''

    for line in input_file:
        # print(line, end='')
        line.strip()
        
        if line.startswith('FEATURES'):
            features_loop = True
        elif line.startswith('ORIGIN'):
            origen_loop = True
            features_loop = False
        elif line.startswith('//'):
            origen_loop = False

        while features_loop == True:
            print(line, end='')
            break

        while origen_loop == True:
            sequence.append(line)
            break

    for line in sequence:
        line = line.strip().replace(' ', '')

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        for num in nums:
            line = line.replace(str(num), '')

        if line == 'ORIGIN':
            line = ''
        else:
            final_seq += line

    # print(final_seq)

def main():
    input_file = input_user()

    reading_file(input_file)
main()

