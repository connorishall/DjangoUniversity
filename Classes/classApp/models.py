# Create your models here.
class djangoClasses:
    Title: str = "Django University"
    Course_Number: str = "1234567"
    Instructor_Name: str = "Mike"
    Duration = "2.0"


# Object math with attributes Title, Course Number, Instructor name, and Duration
math = djangoClasses()
math.Title = "Algebra"
math.Course_Number = '4959'
math.Instructor_Name = "Kyle"
math.Duration = "3.0"
print(math.Course_Number, math.Duration, math.Title, math.Instructor_Name)

# Object english with attributes Title, Course Number, Instructor name, and Duration
english = djangoClasses()
english.Title = "American English"
english.Course_Number = '2452'
english.Instructor_Name = "Caiden"
english.Duration = "2.0"
print(english.Instructor_Name, english.Duration, english.Course_Number, english.Title)

# Object history with attributes Title, Course Number, Instructor name, and Duration
history = djangoClasses()
history.Title = "World History"
history.Course_Number = '5937'
history.Instructor_Name = "Emily"
history.Duration = "1.0"
print(history.Duration, history.Instructor_Name, history.Course_Number, history.Title)
