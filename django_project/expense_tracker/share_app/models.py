from __future__ import unicode_literals  
from django.db import models  
  
class Group(models.Model):  
    numberofusers = models.IntegerField(blank=False)
    group = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return str(self.group)
    class Meta:  
        db_table = "Group"  


class ExpensesTracker(models.Model):  
    expense = models.CharField(max_length=20,blank=False)
    expenseAmount = models.IntegerField(default=0, blank=False)
    whopaid = models.CharField(max_length=20, blank=False)
    #amountowedbyother = model.CharField(max_length=100)
    howtosplit =  models.CharField(max_length=2, choices=(('eq','Equal'),('Ex','Exact'),('%','Percetage')),default="Select from below options", verbose_name="How to split?")
    provideSplit = models.CharField(max_length=50,blank=True,verbose_name="Provide split value only if it's not Equal",help_text="Provide amount or percentage value only if 'How to split?' is Exact OR Percetage. Note, The format should be user1:value,user2:value where value will be the amount owed by respective user")
    group= models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.group)
    class Meta:  
        db_table = "ExpensesTracker"  

class expesneForGroup(models.Model):
    groupName = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.groupName)