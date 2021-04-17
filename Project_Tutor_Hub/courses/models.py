from django.db import models
from django.template.defaultfilters import slugify
from home.models import Tutor,Student
from django.db.models.signals import pre_save
#from tutor_hub.utils import unique_slug_generator
from courses.utils import unique_course_code_generator,unique_slug_generator,unique_lecture_id_generator
import os


def save_class_image(instance,filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    #get filename
    if instance.title:
        filename = 'Class_Pictures/{}.{}'.format(instance.title,ext)
    return os.path.join(upload_to, filename)

class Class(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    class_code = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=550,null=True,blank=True)
    image = models.ImageField(upload_to = save_class_image,blank=True,verbose_name ='class image')
    tutor = models.ForeignKey(Tutor, null=True, blank=True, on_delete=models.CASCADE,related_name='tutors')
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.title

def course_code_generator(sender,instance,*args,**kwargs):
    if not instance.class_code:
        instance.class_code = unique_course_code_generator(instance)

pre_save.connect(course_code_generator,sender = Class)

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender = Class)


def save_lecture_files(instance,filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    #get filename
    if instance.lecture_id:
        filename = 'lecture_files/{}/{}/{}.{}'.format(instance.class_content.slug,instance.lecture_id,instance.lecture_id ,ext)
        if os.path.exists(filename):
            new_name = str(instance.lecture_id) + str('1')
            filename = 'lecture_files/{}/{}/{}.{}'.format(instance.class_content.slug,instance.lecture_id, new_name,ext)
    return os.path.join(upload_to, filename)

class Lecture(models.Model):
    lecture_id = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=150)
    class_content= models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    description = models.TextField(max_length=550,null=True,blank=True)
    created_by = models.ForeignKey(Tutor,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.PositiveSmallIntegerField(verbose_name= 'Lecture No')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lecture_files,verbose_name='video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lecture_files,verbose_name='ppt',blank=True)
    notes = models.FileField(upload_to=save_lecture_files,verbose_name='notes',blank=True)

    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    #def get_absolute_url(self):
        #return reverse("curriculum:lesson_list", kwargs={'slug':self.subject.slug, 'standard':self.standard.slug})

def lecture_id_generator(sender,instance,*args,**kwargs):
    if not instance.lecture_id:
        instance.lecture_id = unique_lecture_id_generator(instance)

pre_save.connect(lecture_id_generator,sender = Lecture)