genbank_file = open('sequence_DNA.gb')
dict_sections = {}
list_sections = []
section = ''
startline = True

for line in genbank_file:
    section = ''
    startline = True
    line = line.rstrip()
    if not line.startswith(' '):
        for letter in line:            
            section += letter
            if startline == True:
                if letter == ' ':       
                    list_sections.append(section)
                    section = ''
                    startline = False
        
        section = section.strip()            
        print(section)

for section2 in list_sections:
    dict_sections[section2] = ''

print(list_sections)
print('')
print(dict_sections)
