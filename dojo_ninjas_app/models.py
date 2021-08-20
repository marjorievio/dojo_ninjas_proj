from django.db import models


# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Name: {self.name} | Descripcion: {self.desc} | Ciudad: {self.city} | Estado: {self.state}>"



class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return f"<First Name: {self.first_name} | Last Name: {self.last_name} | Dojo: {self.dojo}>"

# python manage.py shell
# from dojo_ninjas_app.models import *
# new_dojo=Dojo.objects.create(name="haru",city="Los Angeles",state="CA")
# new_dojo.save()
# new_dojo=Dojo.objects.create(name="Hokusai",city="Washington",state="DC")
# new_dojo.save()
# new_dojo=Dojo.objects.create(name="Kun",city="Atlanta",state="GA")
# new_dojo.save()
# dojo_del=Dojo.objects.get(name="haru")
# dojo_del.delete()
# dojo_del=Dojo.objects.get(name="Hokusai")
# dojo_del.delete()
# dojo_del=Dojo.objects.get(name="Kun")
# dojo_del.delete()
# new_dojo=Dojo.objects.create(name="haru",city="Los Angeles",state="CA")
# new_dojo.save()
# new_dojo=Dojo.objects.create(name="Hokusai",city="Washington",state="DC")
# new_dojo.save()
# new_dojo=Dojo.objects.create(name="Kun",city="Atlanta",state="GA")
# new_dojo.save()

# this_dojo=Dojo.objects.get(name="haru")
# new_ninja=Ninja.objects.create(first_name="Carlos",last_name="Rozas",dojo=this_dojo)                              
# new_ninja.save()
# new_ninja=Ninja.objects.create(first_name="Rodrigo",last_name="Feliu",dojo=this_dojo)                              
# new_ninja.save()
# new_ninja=Ninja.objects.create(first_name="Gustavo",last_name="Lopez",dojo=this_dojo)                              
# new_ninja.save()


# this_dojo=Dojo.objects.get(name="Hokusai")     
# new_ninja=Ninja.objects.create(first_name="Christian",last_name="Sarmiento",dojo=this_dojo)      
# new_ninja.save()    
# new_ninja=Ninja.objects.create(first_name="Loreto",last_name="Ormeño",dojo=this_dojo)       
# new_ninja.save()
# new_ninja=Ninja.objects.create(first_name="Alejandro",last_name="Cofre",dojo=this_dojo)              
# new_ninja.save()

# this_dojo=Dojo.objects.get(name="Kun")        
# new_ninja=Ninja.objects.create(first_name="Mauricio",last_name="Abarca",dojo=this_dojo)         
# new_ninja.save()
# new_ninja=Ninja.objects.create(first_name="Carolina",last_name="Correa",dojo=this_dojo)         
# new_ninja.save()
# new_ninja=Ninja.objects.create(first_name="Macarena",last_name="Brown",dojo=this_dojo)          
# new_ninja.save()

# this_dojo=Dojo.objects.get(name="haru")
# this_dojo.ninjas.all()
# Ninja.objects.filter(dojo=this_dojo)

# this_dojo=Dojo.objects.last()
# Ninja.objects.filter(dojo=this_dojo)

# last_ninja=Ninja.objects.last()
# last_ninja.name       
# Ninja.objects.filter(first_name=last_ninja)

# python manage.py makemigrations
# python manage.py migrate

# new_dojo=Dojo.objects.create(name="Cobrakai",desc="Dojo del Karate Kid",city="Miami",state="FL")
# new_dojo.save()
