newfile = True
file_output = open(input('How would you like to name your fasta file? '), 'a')

while newfile == True:
    file_input = open(input('Input your fasta file: '), 'r')
    max_len_line = int(input('What would you like the sequence line length to be? (Must be an integer!): '))
    sequence_invalid_DNA = False
    sequence_invalid_P = False
    file_type = 'DNA'
    new_file_loop = True
    line_print = ''

    differ_DNA_P = ['*', 'E', 'F', 'J', 'O', 'P', 'Q', 'X']

    char_DNA = ['A','C','G','T','U','(i)','R','Y','K',
                'M','S','W','B','D','H','V','N','-']

    char_P = ['A','B','C','D','E','F','G',
              'H','I','J','K','L','M','N',
              'O','P','Q','R','S','T','U',
              'V','W','X','Y','Z','*','-']

    for line in file_input:
        if line.startswith('>'):
            file_output.write(line)
        if not line.startswith('>'):
            line = line.strip()
        #    line = line.replace(" ", "")
            for letter in line:
                #length of line
                line_print += letter
                length_line_print = len(line_print)
                if length_line_print == len(line_print):
                    last_line = ''
                else:
                    last_line = line_print

                if length_line_print is max_len_line:
                    file_output.write(line_print + '\n')

                    line_print = ''
                    length_line_print = 0
                
                #Checking if file COULD be an Aminoacid
                if letter in differ_DNA_P:
                    file_type = 'Aminoacid'
                #Checking the integrety of the file
                if not letter in char_DNA:
                    sequence_invalid_DNA = True        
                if not letter in char_P:
                    sequence_invalid_P = True
    
    file_output.write(last_line + '\n\n')
    print('File type of imported file:', file_type)

    if file_type == 'DNA':
        if sequence_invalid_DNA == True:
           print('Sequence is invalid!')

    if file_type == 'Aminoacid':
        if sequence_invalid_P == True:
            print('Sequence is invalid!')

    file_input.close()
    
    #loop for opening a new file where the only input can be y or n
    while new_file_loop == True:
        open_new_file = input('Would you like to open a new file? [y][n] ')
        if open_new_file == 'y':
            newfile = True
            new_file_loop = False
        elif open_new_file == 'n':
            newfile = False
            new_file_loop = False
        else:
            print('Invalid character, must be y or n!')
            new_file_loop = True

file_output.close()
