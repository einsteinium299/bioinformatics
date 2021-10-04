# Source : https://www.ncbi.nlm.nih.gov/protein/?term=Haemophilia+A+factor+Viii+human

file = open('sequence_DNA.fasta')
newfile = open('new.fasta', 'w')

for line in file:
    line = line.strip()
    print(line, file=newfile)

file.close()
newfile.close()
test
