# printing both num and letter 20 times


letters = ['A', 'B', 'C', 'D', 'E', 'F']
cycles = 4
output = {
    'num' : [],
    'letter' : []
}


for i in range(cycles * len(letters)):
    output['num'].append(i+1)
    output['letter'].append(letters[i % len(letters)])

print(output)


