# printing different print strings for different words


magicians = ['alice', 'david', 'carolina']
messages = [
    "your card trick was amazing!",
    "your levitation trick was mind-blowing!",
    "your disappearing act was incredible!"
]

for magician, msg in zip(magicians, messages):
    print(f"{magician.title()}, {msg}")         # even if you add a new word to the list, it will only print 3 words only