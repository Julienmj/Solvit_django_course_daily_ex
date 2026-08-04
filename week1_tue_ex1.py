# #Q1
# student_profile = {

#     "full_name" , "email", "phone_number", "country",
# }

# print (student_profile)


# # Q2

# first_name = input("Enter first name : ")
# last_name = input("Enter second name: ")
# username = (first_name + last_name).lower()
# print ("USERNAME: ", username) 


# #Q3

# shopping = ["gucci","suit", "T-H","polo","mj" ]
# print ("first item ", shopping[0])
# print ("last item", shopping[4])
# shopping.append("alo")
# shopping.remove("T-H")
# print("updated list", shopping)

# #Q4

# student_marks = [84,73,49,64,0] 

# print (f"HISGHEST : {max(student_marks)}\n LOWEST: {min(student_marks)}\n TOTAL: {sum(student_marks)}\n AVG: {(sum(student_marks)/len(student_marks))}\n ")



# #Q5 

# dow = ("mon","tue","wed","thus","fri","sat","sun")

# print(f"First DAY: {dow[0]} \n Fourth DAY: {dow[3]} \n Last DAY: {dow[6]}")

# #Q6

# emp_rec = {
#     "emp_id" : 1001,
#     "name" : "Mugisha Julien",
#     "dep" : "IT",
#     "salary" : "3000$"

# }


# emp_rec["salary"] = "5000$"

# emp_rec["email"] = "julienmugisha1@gmail.com"

# print(emp_rec)

#Q7 

# lib_sy = {

#     "title" : "good to great",
#     "author" : " gim collins" ,
#     "yop" : "2020-02-02",
#     "price": 20000,
# }

# print (lib_sy)

# Q8

class_info = ["stu1","stu2","stu3"]

# stu1 = {
#     "name" : "Mj" ,
#     "age" : "22" ,
#     "course" : "Django",
# }

# stu2 = {
#     "name" : "iris" ,
#     "age" : "20" ,
#     "course" : "Django",
# }

# stu3 = {
#     "name" : "paccy" ,
#     "age" : "23" ,
#     "course" : "Django",
# }

# print ()

#Q9

name = "Mugisha Julie"
skills = ["c","c++","python","java"]
dob = ("2004","03","18")
cont = {
    "tel": "0780789636",
    "insta": "Julien_mj1",
    "ytb": "curio",
}

print ("FULL NAME : ",name)
print ("SKILLS: ", skills)
print (f"DOB : {dob[0]}-{dob[1]}-{dob[2]} ")
print (f"tel : {cont["tel"]} \ninstagram : {cont["insta"]}\nyoutube : {cont["ytb"]}\n")