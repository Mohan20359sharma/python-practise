person = {'Name':'Mohan', 'Age':25}
inverted_person = {v: k for k, v in person.items()}
print(inverted_person)