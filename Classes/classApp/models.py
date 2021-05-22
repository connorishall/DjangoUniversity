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
english = djangoClasses(
    1,"American English",
    1,"caiden",
    1.0)
english.save()
english.__str__()
# Object history with attributes Title, Course Number, Instructor name, and Duration
history = djangoClasses(
    1,"world history",
    1,"chris",
    3.0)
history.save()
history.__str__()
