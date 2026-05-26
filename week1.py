
from typing import Dict, List

def cloud_inventory(*cloud_name, **cloud_services):
    """Prints the inventory of cloud services."""
    return f"Cloud Name: {cloud_name}, Cloud Services: {cloud_services}"

print(cloud_inventory("AWS", "Azure", "GCP", compute="EC2", storage="S3", database="RDS"))

cloud_services: dict = {
    "AWS": {"compute": "EC2", "storage": "S3", "database": "RDS"},
    "Azure": {"compute": "VM", "storage": "Blob Storage", "database": "SQL Database"},
    "GCP": {"compute": "Compute Engine", "storage": "Cloud Storage", "database": "Cloud SQL"}
}

# def hello(greeting, name = 'you'):
#     return '{}, {} from the function!'.format(greeting, name)

# #print(hello("Hi", name='John'))  # Output: Hi there!, John from the function!

# def student_info(*args, **kwargs):
#     """Prints the student's courses and personal information."""
    
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# courses = ["Computer Science", "Mathematics"]
# info = {"name": "John", "age": 20, "major": "bachelor of science", "gpa": 3.8}

# student_info(*courses, **info)
# Output:




# dictionaries learning

# student = {"name": "John", "age": 20, "major": ["Computer Science", "Mathematics"]} 
    # student.update({"gpa": 3.8})
    # student.update({"phone": "123-456-7890"})
    
    # for key, value in student.items():
    #     print(f"{key}: {value}")

    # print(f"")
    # print(student.keys())    # Output: dict_keys(['name', 'age', 'major', 'gpa', 'phone'])
    # print(student.values())  # Output: dict_values(['John', 20, ['Computer Science', 'Mathematics'], 3.8, '123-456-7890'])
    # print(student.items())   # Output: dict_items([('name', 'John'), ('age', 20), ('major', ['Computer Science', 'Mathematics']), ('gpa', 3.8), ('phone', '123-456-7890')])
    
    #  del student['age']
    # print(student.get('name', 'Unknown'))  # Output: John
    # print(student.get('age', 'Unknown'))   # Output: 20
    # print(student.get('major', 'Unknown')) # Output: ['Computer Science', 'Mathematics']    
    # print(student.get('gpa', 'Unknown'))   # Output: 3.8
    # print(student.get('phone', 'Unknown')) # Output: 123-456-7890 
    