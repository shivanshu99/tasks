from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    message= models.TextField(max_length=1000, default="")
    name=models.CharField(max_length=50,default="")
    pub_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    class Meta:  
        db_table = "Blogpost"
    def __str__(self):
        return self.title

class Message(models.Model):
    name=models.CharField(max_length=50,default="")
    desc= models.TextField(max_length=1000, default="")
    pub_date = models.DateField(auto_now_add=True)
    commentId=models.IntegerField( default=0)
    def __str__(self):
        return self.name