fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)

student_heights = [180, 124, 165, 173, 189, 169, 164]

print(sum(student_heights))
sum = 0
counter = 0

for n in range(0, len(student_heights)):
  sum += student_heights[n]
  counter += 1

print(f"Average of student heights is {round(sum / counter)}")

# look for the highest score in the student_heights
# replicate these 2 functions below
print(max(student_heights))
print(min(student_heights))

max = student_heights[0]
for i in student_heights:
  if max < i:
    max = i
print(f"The tallest student height is {max}")

#range
for number in range(1, 10): #in JS it would look like for (let i = 1; i < 10; i++)...
  print(number) #prints number from 1-9. does not include the last digit (10)

#get the sum of all even numbers from 1-100
even_sum = 0
for number in range(1, 101):
  if number %2 == 0:
    even_sum += number
print(even_sum)

#you can do it this way as well. This will increment by 2 numbers
for number in range(2, 101, 2):
  even_sum += number
print(even_sum)

#FizzBuzz
for number in range(1, 101):
  if number %15 == 0:
    print("FizzBuzz")
  elif number %3 == 0:
    print("Fizz")
  elif number %5 == 0:
    print("Buzz")
  else:
    print(number)