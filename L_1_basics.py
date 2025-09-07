# Python is case-sensitive too, like Java

print("hello world 1 ", end="")   # works like System.out.print (no new line)
print("hello world 2")            # works like System.out.println (prints with new line)
print("hello world 1 ", end="")   # again, print without new line

"""
In Python:
- print("text") → prints with a newline (like println in Java)
- print("text", end="") → prints without newline (like print in Java)
- '\n' can also be used inside strings for new lines

Hence the output will be:
hello world 1 hello world 2
hello world 1 
"""
