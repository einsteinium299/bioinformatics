genbank_file = open('sequence_DNA.gb')
dict_sections = {}
whitespace_count = 0


for line in genbank_file:
    section = ''
    startline = True
    keyword = ''
    whitespace_count = 0

    line = line.rstrip()
    if not line.startswith(' '):
        for letter in line:            
            section += letter
            if letter == ' ':
                whitespace_count += 1
                
            if startline == True:
                if letter == ' ':
                    keyword = section.strip()
                    section = ''
                    startline = False
        

        #removing multiple whitespace from string                
        section = " ".join(section.split())
        
        dict_sections[keyword] = section            

print(dict_sections)
print(whitespace_count)
