# slice works on both list and array
# for how it works on arrays, plz refer jupyter workspace practice folder


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[:])
print(players[2:])
print(players[:3])

# looping through slice
print()
for i in players[:]:        # looping through first to last index of the list
    print(i)


# WHEN PRINTING A SLICE DIRECTLY: PRINTS AS A LIST
# WHEN LOOPING THROUGH A SLICE WITH FOR-LOOP: PRINTS ELEMENT-WISE
# ELEMENT-WISE PRINTING IS MORE APPROPRIATE IF YOU WANT TO MANIPULATE ELEMENTS

# copying
new_players = players
print(new_players)

