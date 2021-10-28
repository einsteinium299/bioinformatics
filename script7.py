genbank_file = open('sequence_DNA.gb')
dict_sections = {}

for line in genbank_file:
    section = ''
    startline = True
    keyword = ''

    line = line.rstrip()
    if not line.startswith(' '):
        for letter in line:            
            section += letter
            if startline == True:
                if letter == ' ':
                    keyword = section.strip()
                    section = ''
                    startline = False
        
        section = section.strip() 
        dict_sections[keyword] = section            

print(dict_sections)
