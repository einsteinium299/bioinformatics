# Source: https://www.ncbi.nlm.nih.gov/gene/3043
input_filename = open("sequenceProtSCA.fasta")
output_filename = input("Please choose your output file name: ")
input_letter = input('What is your input letter? ')
output_letter = input('What is your output letter? ')
output_filename = open(output_filename, "w")

for lines in input_filename:
    lines = lines.rstrip()
    if not lines.startswith(">"):
        lines = lines.replace(input_letter, output_letter, 1)
    output_filename.write()
input_filename.close()
