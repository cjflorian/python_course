contacts = {
    'number':5,
    'students':
        [
            {'name':'Sara Holderness', 'email':'sara@example.com'},
            {'name':'Harry Potter', 'email':'harry@example.com'},
            {'name':'Hermione Grnger', 'email':'hermione@example.com'},
            {'name':'Ron Weasley', 'email':'ron@example.com'},
            {'name':'Voldemort', 'email':'voldemor@example.com'},   
        ]
}

print('stundes emails')
for student in contacts['students']:
    print(student['email'])