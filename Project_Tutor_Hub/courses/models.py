from django.db import models
from django.template.defaultfilters import slugify
from home.models import tutor,student
from django.db.models.signals import pre_save
class Class(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    class_code = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=550,null=True,blank=True)
    tutor = models.ForeignKey(tutor, null=True, blank=True, on_delete=models.CASCADE,related_name='tutors')
    students = models.ManyToManyField(student, blank=True)

    def __str__(self):
        return self.title

def slug_generator(sender,instance,*aegs,**kwargs):
    if not instance.slug:
        instance.slug = 'Course-Title'

pre_save.connect(slug_generator,sender = Class)