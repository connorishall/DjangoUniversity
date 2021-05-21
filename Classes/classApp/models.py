from django.db import models
# Create your models here.
class djangoClasses(models.Model):
    Title=models.CharField(max_length=50, null=False)
    Course_Number=models.IntegerField()
    Instructor_Name=models.CharField(max_length=50, null=False)
    Duration=models.FloatField()

    classes=models.Manager()
    def __str__(self):
        return self.Title
# Object math with attributes Title, Course Number, Instructor name, and Duration
math = djangoClasses(
    1,"math",
    1,"kyle",
    2.0)
math.save()
math.__str__()

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
