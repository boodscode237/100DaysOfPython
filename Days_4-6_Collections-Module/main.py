from collections import namedtuple

user = ('boods', 'coder')

print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')

user = User(name="abel", role="coder")

print(user.name, user.role)
