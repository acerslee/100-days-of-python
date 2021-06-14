#creating dictionaries
# {key: Value}

# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over and over again."
# }

# #retrieve an item
# print(programming_dictionary["Bug"])

# #adding new items
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# # #create an empty dictionary
# # empty_dictionary = {}

# # #wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #edit an item in a dictionary
# programming_dictionary["Bug"] = "There's an ant on my computer!!"

# for thing in programming_dictionary:
#   print(thing) #prints key
#   print(programming_dictionary[thing]) #prints values

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62
}

#TODO1 - Create an empty dictionary called student_grades
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_grades = {}

for student in student_scores:
  if student_scores[student] > 90 and student_scores[student] <= 100:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 81 and student_scores[student] <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 71 and student_scores[student] <= 80:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
print (student_grades)

#nested loops
capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

#nesting a list in a dictionary
# travel_log = {
#   "France": {
#     "cities visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#   },
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

#nesting dictionary in a list
travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijoin"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 12
  }
]

#write a function to add a new entry for Russia in the travel log
def add_new_country(country, visits, cities):
  new_country = {"country": country, "cities_visited": cities, "total_visits": visits}
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)