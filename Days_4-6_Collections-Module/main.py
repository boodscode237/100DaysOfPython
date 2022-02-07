import random
import timeit
from collections import namedtuple, defaultdict, Counter, deque

user = ('boods', 'coder')

print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')

user = User(name="abel", role="coder")

print(user.name, user.role)

users = {"bob": "coder"}

print(users['bob'])
print(users.get('bob'), users.get('julien'))

challenges_done = [('mike', 10), ('Louis', 15), ('John', 18), ('Maka', 8), ('Gerard', 4)]

print(challenges_done)
#
# challenges = {}
#
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)

challenges = defaultdict(list)

for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges)

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
Ipsum. """.split()

print(words[:5])

common_words = {}

for word in words:
    if word in words:
        if word not in common_words:
            common_words[word] = 0
        common_words[word] += 1

for k, y in sorted(common_words.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(k, y)

print(Counter(words).most_common(5))

lst = list(range(10000000))

deq = deque(range(10000000))


def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)


starttime = timeit.default_timer()
print("The start time is :",starttime)
insert_and_delete(lst)
print("The time difference for list is :", timeit.default_timer() - starttime)


starttime = timeit.default_timer()
print("The start time is :",starttime)
insert_and_delete(deq)
print("The time difference for deq is :", timeit.default_timer() - starttime)

