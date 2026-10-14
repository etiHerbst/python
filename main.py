
def print_arg_kwarg(*arg,**kwarg):
 for item in arg:
  print (item)
 for key, value in kwarg.items():
  print (f"{key}, {value}")

my_tuple = ("תפוח", "בננה", "תפוז")
my_dict = {"שם": "ישראל", "גיל": 30, "עיר": "ירושלים"}
print_arg_kwarg(*my_tuple, **my_dict)



def find_student(my_dict, my_key):
 for key, value in my_dict.items():
  if key == my_key:
   return value
 print("didnt found")

students_dict = {
 "אברהם": {"גיל": 12, "כיתה": "ו'"},
 "משה": {"גיל": 10, "כיתה": "ד'"},
 "דוד": {"גיל": 11, "כיתה": "ה'"}
}
student_info = find_student(students_dict,"משה")
print(student_info)

student_info = find_student(students_dict, "יעקב")


