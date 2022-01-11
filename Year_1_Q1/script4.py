# Haemoglobin S Coding strand mutation: GAG is replaced by GTG
# This replaces the aminoacid E with V
# This replaces mRNA CTC with CAC

def replacement(startpos, string, out):
    endpos = int(startpos) + len(string)
    replace = line[:int(startpos)] + string + line[int(endpos):]
    output_file.write(replace + '\n')
    
inputfile, begin, letters, linenum = input('Input your inputfile, startposition, string and linenumber each divided by a space: ').split()
output_file = open(input('How would you like to call your output file? '), 'w')

line_to_write = int(linenum) -1
line_count = 0
looper = False

HBB_seq = open(inputfile, 'r')

for line in HBB_seq:
    line = line.strip()
    if line.startswith('>'):
        output_file.write(line + ' MUTATED!' + '\n')
    else:
        if line_count == line_to_write:
            looper = True
        if looper == False:
            output_file.write(line + '\n')
        line_count += 1

        while looper:
            replacement(begin, letters, output_file)
            looper = False
            
HBB_seq.close()
output_file.close()
