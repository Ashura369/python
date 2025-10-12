# print how many even nums in the file 

file = r'D:\THE CODE\python\python practice\P_10_3.txt'

with open(file, 'w+') as f:
    f.write('10,12,12,24,6,85,9,8,4,2,65,22')
    f.seek(0)
    print(f.read())




# ****************************************************************************
print('*'*90)

def even():
    with open(file, 'r') as f:
        data = f.read()
        nums = [int(x) for x in data.split(',')]
        print('Numbers: ', nums)

        evens = [n for n in nums if n%2==0]
        print('Even nums: ', evens)
        print('Total even nums: ', len(evens))

even()

# ****************************************************************************
print('*'*90)

def count_evens(file):
    with open(file, 'r') as f:
        data = f.read()

    # Convert to integers
    nums = []
    for x in data.split(','):
        nums.append(int(x))

    print('Numbers:', nums)

    # Collect even numbers
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    print('Even nums:', evens)
    print('Total even nums:', len(evens))


count_evens(file)
