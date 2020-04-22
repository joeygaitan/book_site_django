from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=15)
    birth_date = models.DateField('Birthdate')

    def __str__(self):
        return f"Author name: {self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    

class Book(models.Model):
    title = models.CharField(max_length=25)
    num_pages = models.IntegerField(default=0)
    date_published = models.DateField('Date Published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"book title: {self.title}"