from django.db import models

# Create your models here.


JOB_TYPE = (
    ("FULL TIME ","FULL TIME"),
    ("PART TIME ", "PART TIME "),
    
)

# job 
class job(models.Model): #table 
    #title 
    title=models.CharField(max_length=100)

    # loaction 
     
    #jobe type 
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)

    #DISCRABTIONS 
    discraption = models.TextField(max_length=1000)

    #puplish at 
    puplish_at = models.DateTimeField(auto_now=True)

    #vacancy 
    vacancy  = models.IntegerField(default=1)

    #salary
    salary = models.IntegerField(default=0)

    #experience 
    experience = models.IntegerField(default=1)



    def __str__(self) :
        return self.title




