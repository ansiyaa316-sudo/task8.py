file =open("data.txt","w")
file.close()
name = input("enter your name: ")
age =input("Enter your age: ")
file =open("data.txt","w")
file.write(f" Name:  {name}  \n")
file.write(f" Age:  {age} \n")
file.close()
file =open("data.txt","r")
content =file.read()
print(content)
file.close
email = input("enter your email: ")
file =open("data.txt","a")
file.write(f"email : {email}\n")
file.close()
try:
    file=open("data.txt","r") 
    print(file.read())
    file.close()
except FileNotFoundError:
 print("file not found")
import csv
file =open("students.csv","w", newline="")
writer =csv.writer(file)
writer.writerow(["Name","Age","Branch"])
writer.writerow(["Anu",20,"CSE"])
writer.writerow(["Rahul",21,"ECE"])
file.close()
import csv
file =open("students.csv","r")
reader =csv.reader(file)
for row in reader:
 print(row)
file.close()
with open("data.txt","r") as file:
 print(file.read())