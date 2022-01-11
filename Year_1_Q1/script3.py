newfile = True
file_output = open(input('How would you like to name your multi-fasta file? '), 'a')

while newfile == True:

    #Setting up all the variables needed in the script
    file_input = open(input('Input your fasta file: '), 'r')
    max_len_line = int(input('What would you like the sequence line length to be? (Must be an integer!): '))
    len_group = int(input('How big would you like your groups to be? : '))
    groupcounter = 0
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
            #writing the first line without any changes
            file_output.write(line)

        if not line.startswith('>'):
            line = line.strip()
            line = line.replace(" ", "")         

            for letter in line:
                #Counting the length a line until it has met the max line length.
                line_print += letter
                groupcounter += 1
                length_line_print = len(line_print)
                last_line = line_print
                if length_line_print == max_len_line:
                    last_line = ''

                #Making groups in each line.
                if groupcounter is len_group:
                    line_print = line_print + ' '
                    groupcounter = 0

                #When length_line_print has met max_len_line it will write the output
                #to the multi-fasta file and reset it's variables.        
                if length_line_print is max_len_line:
                    line_print = line_print.strip()
                    file_output.write(line_print + '\n')
                    line_print = ''
                    length_line_print = 0
                    groupcounter = 0

                #Checking if file COULD be an Aminoacid
                if letter in differ_DNA_P:
                    file_type = 'Aminoacid'
                #Checking the integrety of the file
                if not letter in char_DNA:
                    sequence_invalid_DNA = True        
                if not letter in char_P:
                    sequence_invalid_P = True
    
    #Printing the last line of the file that has not been fully filled
    file_output.write(last_line + '\n')

    print('File type of imported file:', file_type)

    #Checking weather the sequence only valid DNA fasta file characters
    if file_type == 'DNA':
        if sequence_invalid_DNA == True:
           print('Sequence is invalid!')

    #Checking weather the sequence only valid Aminoacid fasta file characters
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
            #writing a new line for between the fasta files
            file_output.write('\n')
        elif open_new_file == 'n':
            newfile = False
            new_file_loop = False
        else:
            print('Invalid character, must be y or n!')
            new_file_loop = True

file_output.close()
print('Script finished!')
