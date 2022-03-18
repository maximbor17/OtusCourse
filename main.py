import json
import csv

# res={'users':[]}
user_list = []
with open("files/users.json", "r") as f:
    users = json.loads(f.read())

for user in users:
    user_list.append({'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'age': user['age'],
                      'books': []})

books = []
with open("files/books-133064-871075.csv", newline='') as f:
    for row in csv.DictReader(f):
        books.append(
            {'title': row['Title'], 'author': row['Author'], 'pages': int(row['Pages']), 'genre': row['Genre']}
        )
print(books)

result = []
for user, book in zip(user_list,books):
    result.append({'name':user['name'], 'gender':user['gender'], 'address':user['address'], 'books':[]})

counter = len(result)
counter_id = 0
for x in books:
    result[counter_id]['books'].append({'title':x['title'], 'author':x['author'], 'pages':int(x['pages']),
                                        'genre':x['genre']}

    )
    counter_id += 1
    if counter_id >= counter:
        counter_id = 0

with open('result.json', 'w') as result_json:
    result_data=json.dumps(result, indent=4)
    result_json.write(result_data)

