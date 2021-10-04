# Source : https://www.ncbi.nlm.nih.gov/protein/?term=Haemophilia+A+factor+Viii+human

file = open('sequence_DNA.fasta')
newfile = open('new.fasta', 'w')

for line in file:
    line = line.strip()
    print(line, file=newfile)

file.close()
newfile.close()

amino_acids = "0123456789"

for characters in file_in_open:
    characters_stripped = characters.strip()
    if not characters_stripped.startswith(">"):
        if amino_acids in characters_stripped:
            print("Not correct")
            break
