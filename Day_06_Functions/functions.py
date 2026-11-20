
# 1. Simple Function
def greet_student():
    print("Welcome to The Sadaquat's!")


# 2. Function with Parameters
def student_info(name, department):
    print("Student Name:", name)
    print("Department:", department)


# 3. Function with Default Parameter
def course_info(course="Python Programming"):
    print("Course:", course)


# 4. Function with Return Value
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average


# 5. Function with Multiple Arguments
def calculate_total(*marks):
    return sum(marks)


# Function Calls
greet_student()

student_info("Sadaquat", "Data Science")

course_info()

average = calculate_average(70, 80, 75)
print("Student Average:", average)

total = calculate_total(70, 80, 75)
print("Total Marks:", total)
