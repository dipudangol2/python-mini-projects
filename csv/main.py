'''Python program that reads data from a CSV file containing information about students (eg:name, age, grade)
Calculates average age and average grade of the students. Creates a new CSV file that categorizes students into
age groups (eg:10-15,15-20,20-25)
'''

import csv


def cal_average(age_group, sum_age, sum_grade):
    with open("students.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        num_row = len(list(reader))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        # field_names = reader.fieldnames
        # for key in field_names:
        #     print(key)
        for row in reader:
            if row["age"].isdigit() and row["grade"].isdigit():
                sum_age += int(row["age"])
                sum_grade += int(row["grade"])
                if int(row["age"]) >= 15 and int(row["age"]) < 20:
                    age_group["15-20"].append(row)
                if int(row["age"]) >= 20 and int(row["age"]) < 25:
                    age_group["20-25"].append(row)
                if int(row["age"]) >= 25 and int(row["age"]) < 30:
                    age_group["25-30"].append(row)
                if int(row["age"]) >= 30 and int(row["age"]) < 35:
                    age_group["30-35"].append(row)
    return sum_age, sum_grade, age_group, num_row


def write_with_age_group(age_group):
    try:
        with open("age_group.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            header = ["name", "age-group", "grade"]
            writer.writerow(header)
            for group in age_group.keys():
                for lists in age_group[group]:
                    new_row = []
                    new_row.append(lists["name"])
                    new_row.append(group)
                    new_row.append(lists["grade"])
                    # print(new_row)
                    writer.writerow(new_row)
        print("Data has been categorized and written to file sucessfully.")
    except:
        print("Error occured while writing into the file.")
        


sum_age = 0
sum_grade = 0
age_group = {
    "15-20": [],
    "20-25": [],
    "25-30": [],
    "30-35": [],
}

sum_age, sum_grade, age_group, num_row = cal_average(age_group, sum_age, sum_grade)
average_age = sum_age / num_row
average_grade = sum_grade / num_row
print(f"The average age of students is {average_age} and the average grade is {average_grade}")
write_with_age_group(age_group)


"""
with open("students.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    num_row = len(list(reader))
    print(num_row)
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    # field_names = reader.fieldnames
    # for key in field_names:
    #     print(key)
    for row in reader:
        if row["age"].isdigit() and row["grade"].isdigit():
            sum_age += int(row["age"])
            sum_grade += int(row["grade"])
            if int(row["age"]) >= 15 and int(row["age"]) < 20:
                age_group["15-20"].append(row)
            if int(row["age"]) >= 20 and int(row["age"]) < 25:
                age_group["20-25"].append(row)
            if int(row["age"]) >= 25 and int(row["age"]) < 30:
                age_group["25-30"].append(row)
            if int(row["age"]) >= 30 and int(row["age"]) < 35:
                age_group["30-35"].append(row)
            print(row["name"], row["age"], row["grade"])
            
            print(age_group)
for group in age_group.keys():
    print(age_group[group])
    for lists in age_group[group]:
        print(lists)



with open("age_group.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    header = ["name", "age-group", "grade"]
    writer.writerow(header)
    for group in age_group.keys():
        for lists in age_group[group]:
            new_row = []
            new_row.append(lists["name"])
            new_row.append(group)
            new_row.append(lists["grade"])
            # print(new_row)
            writer.writerow(new_row)

"""
