instructor = {'name':'Jordan','age':22,'job':'programmer','list':['coock', 'dog']}

instructor['names'] = instructor['name']
list = instructor.get('name')
print(list)
list = instructor.get('list')
print(list)
instructor.pop('name')
print(instructor)
instructor['list'].pop(1)
print(instructor)
instructor.popitem()
print(instructor)
instructor.clear()
print(instructor)
