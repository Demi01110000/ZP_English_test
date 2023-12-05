import csv

# importing the csv file into a list of lists so that 
# we can manipulate with the data inside
file = open("TestQs.csv", "r")
matrix = list(csv.reader(file, delimiter=","))

#print(matrix)

# printing only the questions in the list and the options
y=0
x=0
q=1 #question num
for row in matrix:
    print("Question", q)
    print(matrix[y][x])
    print(matrix[y][x+2])
    correct_answer = matrix([y][x+1])
    print(correct_answer)
    #print(matrix[y][x+1])
    #user_answer = input('type your answer here')
    #if user_answer == correct_answer:
       # print("Correct! +1 point for you")
    #else:
        #print("nope :(")
    
    y +=1
    q +=1

    
