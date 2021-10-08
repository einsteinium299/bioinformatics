# Haemoglobin S Coding strand mutation: GAG is replaced by GTG
# This replaces the aminoacid E with V
# This replaces mRNA CTC with CAC

def replacements(file_name, replacement, replacer):
    for line in file_name:
        line = line.strip()
        if line.startswith('>'):
            print(line, 'mutated!!')
        if not line.startswith('>'):
            line = line.replace(replacement, replacer)
            print(line)

#inputfile, startpos, endpos, letter = input('Input your inputfile, startposition, endposition and codon each divided by a space: ').split()
#output_file = open(input('How would you like to call your output file? '), 'w')

inputfile = 'sequence_DNA_codingseq.txt'
#startpos = 4
#endpos = 10
#letter = "XXXXXX"
#looper = True
#line_count = 0

HBB_seq = open(inputfile, 'r')
HBB_P = open('sequence_P.fasta', 'r')
#HBB_seq_mutated = open('sequence_mutated.fasta', 'w')

print('Nuc replacements')
replacements(HBB_seq, 'GAG', 'GTG')

print('Amino replacements')
replacements(HBB_P, 'E', 'V')

#for line in HBB_seq:
#    line = line.strip()
#    if line.startswith('>'):
#        print(line, 'mutated!', file=output_file)
#    else:
#        while looper:
#            replace = line[:int(startpos)] + letter + line[int(endpos):]
#            print(replace, file=output_file)
#            looper = False
#        print(line, file=output_file)

#HBB_seq.close()
#HBB_seq_mutated.close()
