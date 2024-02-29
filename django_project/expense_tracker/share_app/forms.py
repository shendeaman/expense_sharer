from django import forms  
from share_app.models import Group,ExpensesTracker, expesneForGroup
  
class GroupForm(forms.ModelForm):  
    class Meta:  
        model = Group  
        fields = "__all__"  
        
class ExpenseTrackerForm(forms.ModelForm):
    class Meta:  
        model = ExpensesTracker  
        fields = ['expense','expenseAmount','whopaid','howtosplit','provideSplit','group']

class ExpenseForGroupForm(forms.ModelForm):
    class Meta:  
        model = expesneForGroup  
        fields = ['groupName']
        