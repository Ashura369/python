name = input("ENTER NAME : ")
rollNo = int(input("ENTER ROLL NO : "))
cls = int(input("ENTER CLASS NO : "))
subjects = int(input("ENTER THE TOTAL NO. OF SUBJECTS YOU WANT TO ENTER : "))



stud = {
    'NAME' : name,
    'ROLL.NO.' : rollNo,
    'CLASS' : cls,
    'SUBJECTS' : {

    }
}


# assinging new dictionary to the "SUBJECTS"
for i in range(1, subjects + 1):
    subject = input(f"ENTER SUBJECT {i} : ")
    stud['SUBJECTS'][f'SUBJECT {i}'] = subject


""" 
        stud = {
            'name' : name,
            'rollNo' : rollNo,
            'class' : cls,
            'subjects' : {
                subject 1 : xxx
                subject 2 : yyy
                subject 3 : zzz    
            }
        }

"""


print(f"\n {stud}")







