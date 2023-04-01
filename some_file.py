data1 = ['Desktop', 'Notes', 'Commands', 'React', 'Classified', 'General', 'Excel File.doc']
data2 = ['desktop', 'notes', 'commands', 'react', 'classified', 'general', 'excelFile']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()
assert data1 == data2