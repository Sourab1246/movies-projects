from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxLengthValidator,MinValueValidator
from datetime import timedelta

# Create your models here.
class Movies(models.Model):
     Action='Action'
     Drama='Drama'
     Comedy='Comedy'
     Funny='Funny'
     Sad='Sad'
     Thriller='Thriller'
     Horror='Horror'
     Romantic='Romantic'
     Action_Drama='Action/Drama'
     Action_Drama_Thriller='Action/Drama/Thriller'
     Action_Comedy='Action/Comedy'
     Horror_Romantic='Horror/Romantic'
     Drama_funny=" Drama/funny"
     id=models.AutoField(primary_key=True)
     movies_name=models.CharField(max_length=20)
     visual_type_choices=[('2D','2D'),('3D','3D'),('IMAX','IMAX'),('ICE 3D','ICE 3D'),('4DX 3D','4DX 3D')]
     visual_type=models.CharField(choices=visual_type_choices,max_length=10)
     type_choices=[(Action,'Action'),(Romantic,'Romantic'),(Sad,'Sad'),(Drama,"Drama"),(Horror,'Horror')
                   ,(Funny,"Funny")
                   ,(Thriller,"Thriller"),(Comedy,"Comedy"),(Action_Drama,'Action/Drama')
                   ,(Action_Drama_Thriller,'Action/Drama/Thriller'),
                   ( Action_Comedy,'Action/Comedy'),
                   ( Horror_Romantic,'Horror/Romantic'),
                   (Drama_funny,"Drama/funny")
                   ]
     types=models.CharField(choices=type_choices,max_length=50,default="Action")
     duration=models.DurationField(default="0h 0min",verbose_name="Duration")
     ratings=models.PositiveIntegerField(default='00:00:00',choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
     release_date=models.DateField(default="12/08/23",verbose_name="In cinemas")
     about=models.CharField(max_length=2000,verbose_name="About The Movie",default="about the movies")
     def __str__(self):
         return self.movies_name
     
class Cast(models.Model):
    name=models.CharField(max_length=20)
    nick_name=models.CharField(max_length=20,verbose_name="Also known as" )
    occupation=models.CharField(max_length=200)
    born=models.DateField(default="10-12-23",verbose_name="Born")
    birth_palace=models.CharField(max_length=20,verbose_name="Birth_palace")
    spouse=models.CharField(max_length=20,default="Savita")
    children=models.PositiveIntegerField()
    about=models.CharField(max_length=2000,verbose_name="About The Actor",default="about the actor")
    def __str__(self):
        return self.name

class MoviesCast(models.Model):
    movies=models.ForeignKey(Movies,on_delete=models.CASCADE)
    cast=models.ForeignKey(Cast,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.movies
    
    
    
         
