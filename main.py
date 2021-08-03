import mysql.connector

db = mysql.connector.connect(
    host='chimpvine.com',
    user='chimpvin_dareadonly',
    passwd='yAn)[0?1S.S(',
    database='chimpvin_dataanalytics',
    )
mycursor = db.cursor()

user_name = input("Enter the Name: ")
user_course = input("Enter the course: ")
user_quiz = input("Enter the quiz: ")
print("")
print("Loading.")
print("Loading..")
print("Loading...")
print("")
#Query 1
mycursor.execute("select count(*) as Total_Quizes from mdl_quiz_attempts inner join mdl_quiz on mdl_quiz_attempts.quiz = mdl_quiz.id inner join mdl_course on mdl_quiz.course = mdl_course.id inner join mdl_course_categories on mdl_course.category = mdl_course_categories.id inner join mdl_user on mdl_quiz_attempts.userid = mdl_user.id where mdl_user.firstname = %s and fullname=%s and mdl_quiz.name = %s",(user_name,user_course,user_quiz,))
for i in mycursor:
    print(i[0], " quizzes attempted in total in the ", user_course ," by ", user_name)


#query 2
mycursor.execute("select count(*) from mdl_quiz_attempts  inner join mdl_user on mdl_quiz_attempts.userid = mdl_user.id where mdl_user.firstname = %s  and state = %s",(user_name,"inprogress",))
for newcolumn in mycursor:
    print(newcolumn[0], " quizes attempted but not finished by ", user_name)
   

#query 3 & 4
mycursor.execute("select sec_to_time(timefinish - timestart) as Time_Taken, mdl_quiz_grades.grade as Grade, mdl_quiz.name as Quiz_Name, DATE_FORMAT(from_unixtime(mdl_quiz_attempts.timestart),'%m-%d-%Y') start_date  from mdl_quiz_attempts inner join mdl_quiz on mdl_quiz_attempts.quiz = mdl_quiz.id inner join mdl_course on mdl_quiz.course = mdl_course.id inner join mdl_course_categories on mdl_course.category = mdl_course_categories.id inner join mdl_user on mdl_quiz_attempts.userid = mdl_user.id inner join mdl_quiz_grades on mdl_quiz_attempts.userid = mdl_quiz_grades.userid where mdl_user.firstname = %s and mdl_course.fullname = %s and mdl_quiz.name = %s and state = %s",(user_name,user_course,user_quiz,"finished",))
for column in mycursor:
    print("Score: ", column[1])
    print("Quiz Taken: ", column[2])
    print("Time Taken: ", column[0],"(hh:mm:ss)")
    print("Date When Attempted: ", column[3])
