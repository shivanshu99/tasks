from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=False)
    message= models.TextField(max_length=1000, blank=False)
    pub_date = models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to='shop/images',blank=False)
    class Meta:  
        db_table = "Blogpost"
    def __str__(self):
        return self.name

class Phone(models.Model):
    phone = models.BigIntegerField(max_length=10, blank=False)
    def __str__(self):
        return str(self.phone)

class New(models.Model):
    newmessage=models.CharField(max_length=500,blank=False)
    def __str__(self):
        return self.newmessage