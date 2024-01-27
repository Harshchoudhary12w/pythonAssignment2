students_list = []

with open("f3.txt", 'r') as file:
 
    lines = file.readlines()

   
    student_info = {}
    for line in lines:
        line = line.strip()
        if line:
            key, value = map(str.strip, line.split(':', 1))
            student_info[key] = value
        else:
             if student_info:
                students_list.append(student_info)
                student_info = {}


print(students_list)

with open("f3.txt", 'w') as output_file:

    for student_info in students_list:
        for key, value in student_info.items():
            output_file.write(f"{key}: {value}\n")
        output_file.write("\n")