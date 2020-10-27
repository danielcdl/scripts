people = {}
count = 1
while count <= 10:
    name = input('Name: ').strip().title()
    try:
        people[name] = float(input('Height: '))
        count += 1
    except ValueError:
        print('Numbers. Try again.')

#como pode existir uma ou mais pessoas com a mior altura, busco primeiro a maior altura
max_height = max(people.values())
#agora vejo as pessoas que tem a maior altura
tallest = []
for person in people:
    if people[person] == max_height:
        tallest.append(person)
print(people)

print("The tallest are:", ", ".join(tallest))
