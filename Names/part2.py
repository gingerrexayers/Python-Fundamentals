users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

for idx, name in users.items():
    print idx
    for i in enumerate(name):
        print i[0]+1, "-", i[1]['first_name'].upper(), i[1]['last_name'].upper(), "-", len(i[1]['first_name']) + len(i[1]['last_name'])
