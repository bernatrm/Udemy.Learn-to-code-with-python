college_courses = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Eisntein"
}

for key, value in college_courses.items():
    print(f"The coruse {key} is begin taught by {value}.")

print("or you can use more descriptive keys")

for course, professor in college_courses.items():
    print(f"The coruse {course} is begin taught by {professor}.")

# A common uses for a variable that you will not use, but you needs on your syntax is name it as "_"
for _, professor in college_courses.items():
    print(f"The next professor is {professor}")

print(college_courses.items())