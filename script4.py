 Source: https://www.ncbi.nlm.nih.gov/gene/3043
input_filename = open("sequenceprot.fasta.fasta")
output_filename = input("Please choose your output file name: ")
replacing_letter = input('What is your output letter? ')
spot = input("What is the position of your input letter? ")
output_filename = open(output_filename, "w")
# Replaces one letter with the other, but you can not choose a line yet.
def replacer(replaced_lines, letter, position):
        return replaced_lines[:position] + letter + replaced_lines[position+1:]

for lines in input_filename:
    lines = lines.rstrip()
    if not lines.startswith(">"):
        print(replacer(lines, replacing_letter, int(spot)))
        output_filename.write(lines)

input_filename.close()
output_filename.close()
