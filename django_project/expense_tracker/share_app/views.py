from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from share_app.forms import GroupForm,ExpenseTrackerForm,ExpenseForGroupForm
import pyodbc
# Create your views here.
 

def index(request):  
   template = loader.get_template('index.html')
   return HttpResponse(template.render())
   
def mainPage(request):  
   template = loader.get_template('mainPage.html')
   return HttpResponse(template.render())

    
def groupCreation(request):  
    if request.method == "POST":
        print("*******")
        form = GroupForm(request.POST)  
        if form.is_valid():
            form.save()
            groupName = form.cleaned_data['group']
            numberOfUsers = form.cleaned_data['numberofusers']
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-E24POCG1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO dbo.Groups (groupName, numberOfUsers) VALUES ('{groupName}', '{numberOfUsers}');")
            cursor.commit()

            try: 
                return redirect('mainpage')
                #return HttpResponse("Returning reponse")
            except:  
                pass  
    else:
        form = GroupForm()  
    return render(request,'groupcreation.html',{'form':form})
    
def addExpenses(request):
    if request.method == "POST":
        form = ExpenseTrackerForm(request.POST)  
        if form.is_valid():
            form.save()
            groupName = form.cleaned_data['group']
            howToSplit = form.cleaned_data['howtosplit']
            provideSplit = form.cleaned_data['provideSplit']
            print(f"groupName : {groupName} AND howToSplit : {howToSplit} AND provideSplit : {provideSplit}")
            
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-E24POCG1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
            query = f"Select * from dbo.Groups where groupName='{groupName}';"
            print(f"query : {query}")
            cursor = conn.cursor()
            cursor.execute(query)
            listObj = [ele for ele in cursor]
            groupid,numberOfUsers = listObj[0][0],listObj[0][2]
            
            #groupid = list(cursor)[0]
            #numberOfUsers = list(cursor)[2]
            print(f"groupid : {groupid} and numberOfUsers : {numberOfUsers}")
            
            expenseName = form.cleaned_data['expense']
            whoPaid = form.cleaned_data['whopaid']
            expenseAmount = form.cleaned_data['expenseAmount']
            amountowedbyother = [round(expenseAmount/numberOfUsers,2)]*(numberOfUsers-1)
            if howToSplit=='Eq':
                query = f"INSERT INTO dbo.ExpenseSharer (expenseName, expenseAmount, whopaid, amountOwedByOthers, groupid, howToSplit) VALUES ('{expenseName}',{expenseAmount},'{whoPaid}', '{amountowedbyother}',{groupid},'Equal');"
            elif howToSplit=='Ex':
                query = f"INSERT INTO dbo.ExpenseSharer (expenseName, expenseAmount, whopaid, amountOwedByOthers, groupid, howToSplit) VALUES ('{expenseName}',{expenseAmount},'{whoPaid}', '{provideSplit}',{groupid},'Exact');"
            elif howToSplit=='%':
                query = f"INSERT INTO dbo.ExpenseSharer (expenseName, expenseAmount, whopaid, amountOwedByOthers, groupid, howToSplit) VALUES ('{expenseName}',{expenseAmount},'{whoPaid}', '{provideSplit}',{groupid},'Percentage');"
            print(f"query : {query}")
            cursor.execute(query)
            cursor.commit()

            try: 
                return redirect('mainpage')
                #return HttpResponse("Returning reponse")
            except:  
                pass  
    else:
        form = ExpenseTrackerForm()  
    return render(request,'expenseDialer.html',{'form':form})
    
    
def showGroups(request):
    conn = pyodbc.connect('Driver={SQL Server};'
              'Server=LAPTOP-E24POCG1\SQLEXPRESS;'
              'Database=TestDB;'
              'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(f"Select * from dbo.Groups;")
    list_of_groups = [ele for ele in cursor]
    template = loader.get_template('showgroup.html')
    print(f"list_of_groups : {list_of_groups}")
    #return render(request,'showgroup.html',{'table_data':list_of_groups})
    return HttpResponse(template.render({'table_data':list_of_groups})) 
    
def showUserExpenses(request):
    if request.method == "POST":
        print("*******")
        form = ExpenseForGroupForm(request.POST) 
        if form.is_valid():
            groupName = form.cleaned_data['groupName']
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-E24POCG1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()
            
            query = f"Select * from dbo.Groups where groupName='{groupName}';"
            print(f"query : {query}")
            cursor.execute(query)
            listObj = [ele for ele in cursor]
            groupid,numberOfUsers = listObj[0][0],listObj[0][2]
            print(f"groupid : {groupid} and numberOfUsers : {numberOfUsers}")
            
            query = f"Select * from dbo.ExpenseSharer where groupid={groupid}"
            cursor.execute(query)
            
            listOfExpenses = [ele for ele in cursor]
            print(f"listOfExpenses : {listOfExpenses}")
            mainList = []
            string_list = []
            for ele in listOfExpenses:
                expenseName = ele[0]
                expenseAmount = ele[1]
                howToSplit = ele[5]
                whoPaid = ele[2]
                userWhoPaid = whoPaid[len(whoPaid)-1]
                if howToSplit=='Exact':
                    provideSplit = ele[3].split(',')
                    provideSplit = [tuple(ele.split(':')) for ele in provideSplit]
                    print(f"provideSplit : {provideSplit}")
                    mainList.append(provideSplit)
                    
                    string = 'For '+expenseName+' '
                    for k,v in provideSplit:
                        string = string+k+' owes '+v+', '
                    string = string + 'to '+ whoPaid + '.'
                    string_list.append(string)
                
                elif howToSplit=='Equal':
                    data = {}
                    amountList = str(ele[3]).replace('[','').replace(']','').split(',')
                    print(f"userWhoPaid : {userWhoPaid} AND amountList : {amountList} and numberOfUsers : {numberOfUsers}")
                    
                    string = 'For '+expenseName+' '
                    for i in range(numberOfUsers):
                        if userWhoPaid==i+1:
                            data['user'+str(userWhoPaid)] = ele[1]-float(amountList[0])
                        else:
                            data['user'+str(i+1)] = -(amountList[0])
                            string = string + 'user'+str(i+1) + ' owes ' + amountList[0] + ', '
                    string = string + 'to '+ whoPaid + '.'
                    string_list.append(string)
                    mainList.append(data)
                
                elif howToSplit=='Percentage':
                    data = {}
                    provideSplit = ele[3].split(',')
                    provideSplit = [tuple(ele.split(':')) for ele in provideSplit]
                    print(f"provideSplit : {provideSplit}")
                    
                    string = 'For '+expenseName+' '
                    for i,(k,v) in enumerate(provideSplit,1):
                        splitAmount = expenseAmount*(float(v)/100)
                        if userWhoPaid==i:
                            data['user'+str(userWhoPaid)] = None
                        else:
                            data['user'+str(i)] = -(splitAmount)
                            string = string + 'user'+str(i+1) + ' owes ' + str(splitAmount) + ', '
                    sumOfOwed = sum([float(v) for k,v in data.items()])
                    actuallyWhoPaid = expenseAmount + sumOfOwed
                    data['user'+str(userWhoPaid)] = actuallyWhoPaid
                    print(f"sumOfOwed : {sumOfOwed}")
                    
                    string = string + 'to '+ whoPaid + '.'
                    string_list.append(string)
                    mainList.append(data)
                    
                print(f"mainList : {mainList}")
                    
            
            try: 
                return render(request,'showExpenses.html',{'Data':string_list})
                #return redirect('mainpage')
                #return HttpResponse("Returning reponse")
            except:  
                pass  
    else:
        form = ExpenseForGroupForm()  
    return render(request,'showExpenseForGroups.html',{'form':form})
    
def aboutApp(request):
    pass
    