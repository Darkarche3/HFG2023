from django.db import models

# Create your models here.

class Location(models.Model): #one-to-many relation
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)

    def __str__(self):
        return f"{self.name} ({self.address})"

class Category(models.Model): #one-to-many relation
    name = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.name}"

class Participant(models.Model):
    
    name = models.CharField(max_length = 200, default = "John Doe")
    email = models.EmailField(unique = True)
    
    def __str__(self): #many-to=many relation
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length = 200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    participants = models.ManyToManyField(Participant, blank = True, null = True)

    def __str__(self):
        return f"{self.title} - {self.slug}"



