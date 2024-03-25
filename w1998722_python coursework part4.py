# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221086
# UOW num: w1998722
# Date: 19.04.2023
# W L A S C B Weerasuriya

#part4
#variables used
l=[0,20,40,60,80,100,120]
progress=0
trailer=0
retreiver=0
exclude=0
option=0
total=0

#https://www.w3schools.com/python/python_lists.asp (python lists related for part 2)
progress_list=[]
progress_trailer_list=[]
module_retreiver_list=[]
exclude_list=[]
my_dict={}
 
def function(lists,outputs):  #https://www.w3schools.com/python/python_functions.asp(how to work with def function)
    for i in range(len(lists)):
        print(outputs,lists[i])
        
def mychoice (prompt):
    while True:  #https://stackoverflow.com/questions/3947055/whats-the-point-of-using-while-true
        user = input(prompt)
        if user.lower() == "student" or user.lower() == "staff":
            return user
        else:
            True

user = mychoice("student or staff: ")
while True:
    try:
        student_id=input("enter student id :")
        if len(student_id)==8:
            print(student_id)
        else:
            print("enter a valid student id")
            continue
        p=int(input('please enter your credits at pass: '))
        if p not in l :
            print('out of range')
            continue
        d=int(input('please enter your credits at defer: ')) 
        if d not in l :
            print('out of range')
            continue   
        f=int(input('please enter your credits at fail: '))
        if f not in l :
            print('out of range') 
            continue
        if p+d+f != 120:
            print('Total incorrect')
            continue
    
        
        if 100<p<=120:
            print('progress')
            print()
            print("-"*50)
            progress+=1
            my_dict[student_id]= (f"progress-{p},{d},{f}")
            progress_list.append((p,d,f)) #data was appended to a list -but in part 4 lists are not printed since part 4 is related to dictionries
        elif p==100:
            print('progress(module trailer)')
            print()
            print("-"*50)
            trailer+=1
            my_dict[student_id]= (f"module trailer-{p},{d},{f}")
            progress_trailer_list.append((p,d,f))
        elif 60<=(p+d)or 60<=p<=80:
            print('do not progress- module retreiver')
            print()
            print("-"*50)
            retreiver+=1
            my_dict[student_id]= (f"module retreiver-{p},{d},{f}")
            module_retreiver_list.append((p,d,f))
        else:
            print('exclude')
            print()
            print("-"*50)
            exclude+=1
            my_dict[student_id]= (f"exclude-{p},{d},{f}")
            exclude_list.append((p,d,f))
            
        if user.lower() == "student":
            exit()
        
        if user.lower() =="staff":
            while True: # program will only run if y or q is entered
                option=str(input("would you like to enter another set of data?\n Enter 'q'to quit or Enter 'y' for yes and view results :"))
                print("-"*50)
                if option.lower()in ("y","q"):
                    break
                else:
                    print('enter a valid option')
                    
               
            if option.lower()=='y':
                continue
            elif option.lower()=='q':
                break
            
    except ValueError:
        print('integer required')

#text files
with open('text_file.txt', 'w') as output_texts: #https://stackoverflow.com/questions/7485458/python-reading-text-file
    output_texts.write("part 3:\n")              #https://www.youtube.com/watch?v=Uh2ebFW8OYM
    output_texts.write("\n")                     #https://learning.westminster.ac.uk/ultra/courses/_89622_1/outline/edit/document/_4299464_1?courseId=_89622_1&view=content
    output_texts.write("progress \n")            #(sd1 week6 lecture slide)
    for samples in progress_list:
        output_texts.write(str(samples)+"\n" "")
    output_texts.write("module trailer \n")
    for samples in progress_trailer_list:
        output_texts.write(str(samples)+"\n" "")
    output_texts.write("module_retreiver \n")
    for samples in module_retreiver_list:
        output_texts.write(str(samples)+"\n" "")
    output_texts.write("exclude \n")
    for samples in exclude_list:
        output_texts.write(str(samples)+"\n" "")

        


print("-"*50)
print('histogram')
print("progress", progress, ":", progress*'*')
print("module trailer",trailer,":",trailer*'*')
print("module retreiver",retreiver,":",retreiver*'*')
print("Exclude",exclude,":",exclude*'*')
total=progress+trailer+retreiver+exclude
print("outcomes in total:",total)
print("-"*50)

print('part4 \n')#Dictionary  #https://learning.westminster.ac.uk/ultra/courses/_89622_1/outline/edit/document/_4299472_1?courseId=_89622_1&view=content
for key, value in my_dict.items(): #https://www.w3schools.com/python/python_dictionaries.asp
    print(f"{key}: {value}", end=" ") #https://stackoverflow.com/questions/40071006/python-2-7-print-a-dictionary-without-brackets-and-quotation-marks

#further references- https://www.youtube.com/watch?v=_uQrJ0TkZlc- python tutorial         

   
           
