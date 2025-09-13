list = [1,2,3,4,5,6,7,8,4,86,55,9,62,64,10,62,47,5662,65,7,5415,15,41,2,254,8,51,54,84,15,8]

# these below are the example of for else loop

for i in list:
    if i >= 100:
        print('This number ',i, 'is greater then 100')
        continue        # It skips the rest of the current loop iteration, and move on to the next item
    
    print(i)
else:
    print('END OF THE LOOP')


print('******************************************************************')

for i in list:
    if i % 2 == 0:
        print(i, 'is an even')
    else:
        print(i, 'is an odd')

else:
    print('END OF THE LOOP')    # So "END OF THE LOOP" will always print unless you 'break' out of the loop.

print('******************************************************************')

# searching for a number

x = 8

for idx, i in enumerate(list):
    if i == x:
        print('the number',x,'is at index', idx)
        continue

else:
    print('THE NUMBER YOU ARE LOOKING FOR IS NOT PRESENT IN THE LIST')





