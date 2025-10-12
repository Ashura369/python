# IMP

name = input("NAME : ")
age = int(input("AGE : "))
id = int(input("ID : "))
total_subjects = ['math', 'english', 'science', 'physics', 'chemestry', 'sociology', 'economics']


std = {
    'name' : name,
    'age' : age,
    'ID' : id,
    'total subjects' : {

    }
}

# taking the subjects as lists
print(f"CHOOSE THE SUBJECTS YOU WANT IN Y OR N (Y = YES, N = NO) \n")
for i, j in enumerate(total_subjects):
   a = (input(f"DO YOU WANT {j} ? (Y/N) : ") ).strip().upper()
   if (a == "Y"):
      std['total subjects'][f'subject {i+1}'] = j


print(std)



