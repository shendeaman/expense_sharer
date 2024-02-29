**Expense sharing application:**

_1. What is the purpose of the application?_
The application's primary purpose is to track the expenses shared amongst users in a group. A group can have any number of members and they may share the bills,
Our application keeps track of these expenses.
   
_2. How does the application work?_
Presently, the application is divided into a few sections. The first one deals with creating a group for which one needs to click on 'Add groups', which tries to fulfill       the objective that an application can have many users as each group can further have a certain set of users, I found there's a need to create separate groups where we'll       further have a certain number of users who'll share the expenses amongst them. Once we're done creating groups, you can see the groups available by clicking on the             'Existing groups'. Second, you can add the corresponding details for the groups created by clicking on 'Add expenses', It'll allow us to add the necessary details for the respective groups. Once the details are added, we can further
check the expense status shared amongst various users in a group by clicking on 'Expense tracking status'.
   
_3. What are the dependencies that come with the application?_
Here, I'm connecting with the local database named 'TestDB'available at the MS SQL Server. It has 2 tables, named dbo.ExpenseSharer which stores the expense details of         various users in a group and dbo.Groups that store the information related to the name of the group & number of users available in that group. The key point to remember is that Django officially supports PostgreSQL, MariaDB, MySQL, Oracle, and SQLite so to connect with MS SQL Server I needed to use the PyODBC module of Python.

_4. Functionalities that need to be added_
As of now, I'm yet to implement a simplified view of the expenses. Also, need to create a scheduler that will additionally send emails once a new expense is added to a        group.
   
