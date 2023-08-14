# banking_application
Object-Oriented Programming with the implementation of a banking application,
Create and initialize the User class.
In your week4 folder, create a new file and name it workshop4.py.
In this file, declare a class and give it the name User.
Give the User class three instance attributes: name, pin, and password.
Test Task 1 
For this assignment, you will write "driver code" for each task. Driver code is not a part of your application but is used to test parts of your application.
Write this driver code in the same file (workshop4.py), but keep it at the bottom of the file, separated from the rest of your code.
Add a comment above your driver code to separate it from the rest of your code, similar to this:
    """ Driver Code for Task 1 """
Then write your driver code for Task 1 underneath this comment.
For your driver code:
Write code to instantiate an object from the User class, providing the name, pin, and password as arguments.
For example, you could use "Bob" as the name, 1234 as the pin, and "password" as the password. 
Write a print statement to print the name, pin, and password attributes of this object. 
Save and run your code. The output should look similar to this:


After testing, comment out the driver code for this task.

Task 2: Add User class instance methods
Write three methods for the User class:
change_name() - Changes the name of the User.
change_pin() - Changes the PIN of the User.
change_password() - Changes the password of the User.
Test Task 2
Below the commented-out driver code for Task 1, add the driver code for Task 2.
You can add a comment such as:
    """ Driver Code for Task 2 """
...then write your driver code under this comment.
For your driver code:
Once again, instantiate an object from the User class, providing the name, pin, and password as arguments.
These can be the same code and arguments as in Task 1. For example, the arguments: "Bob", 1234, "password".
Again, print the object's attributes. 
Call each of the three methods you created to change the name, pin, and password. 
Print the updated attributes. 
Save your changes and run the updated code.
The output should look similar to this:


After testing, comment out the driver code for Task 2.


Task 3: Create BankUser subclass

Declare a class and give it the name BankUser.
Have the BankUser class inherit the User class. This means it should be child class/subclass of the User parent class/superclass.
It should inherit the instance attributes of name, pin, and password.
Use the super() function to initialize these inherited attributes using the superclass.
Give the BankUser class its own instance attribute as well, which the User class does not have: balance, initialized to a value of 0. 
This attribute is not passed in via the parameter list. 
Test Task 3
Add a comment similar to this under your commented-out driver code for Task 2:
""" Driver Code for Task 3"""
For your driver code:
Instantiate an object of the BankUser class, providing arguments for the name, pin, and password.  
Print the attributes of the BankUser object you created: name, PIN, password, and balance.
Save and run your code. The output should look similar to this:

The first three attributes printed (name, PIN, password) should match whatever arguments you supplied when instantiating the object. 
The fourth attribute printed (balance) should be 0.
After testing, comment out the driver code for Task 3.

Task 4: Add BankUser class instance methods
Write three methods for the BankUser class:
show_balance() - Prints the BankUser object's balance
withdraw() - Withdraws money, decreases the account balance
deposit() - Deposits money, increases the account balance
Test Task 4
Add a comment similar to this under your commented-out driver code for Task 3:
""" Driver Code for Task 4"""
For your driver code:
Instantiate an object of the BankUser class, providing arguments for the name, pin, and password.  
This can be a copy of the same code you used in Task 3. 
Call the show_balance() method of the object.
Call the deposit() method, depositing some positive number.
Call the show_balance() method once again.
Call the withdraw() method, withdrawing some number lower than what was deposited.
Call the show_balance() method again. 
Save and run the updated code. The output should look similar to this:


After testing, comment out the driver code for Task 4.

Task 5: Transfer and request money
Create two more methods for the BankUser class:
transfer_money() 
Transfers money to another User if
correct PIN is given for the transferring User. Also return a Boolean value of True. 
If an incorrect PIN is given, return a Boolean value of False. 
request_money() 
Will ask for the PIN of the User receiving the request for money.
If the credentials are correct,
Will ask for and validate the password of the User requesting money as well,
Then complete the transfer, removing money from one account and adding the same amount to the other.
If both the PIN and password requested are correct, return True. 
If either is incorrect, return False. 

Test Task 5: 
Add a comment similar to this under your commented-out driver code for Task 4:
""" Driver Code for Task 5"""
For your driver code:
Instantiate an object of the BankUser class, providing arguments for the name, pin, and password.  
This can be a copy of the same code you used in Task 4. 
Instantiate a second object of the BankUser class, providing different arguments. 
Deposit $5000 into the account of this second user using the deposit() method. 
Show the balance of the second user.
Show the balance of the first user.
Have the second user transfer $500 to the first user, using its transfer_money() method.
Again, show the balance of each user.
If the money transfer is successful, have the second user request some money from the first user, using its request_money() method (this means that there should be an if statement in your test code checking for the success of the first transaction).
Again, show the balance of both users.
Save and run your code. The output should look similar to this:
 
If the wrong PIN is given when a money transfer is requested, the result should look similar to this:


If when requesting money, the PIN is incorrect, the result should look similar to this:
 

If when requesting money, the PIN is correct but the password is incorrect, the result should look similar to this:

Added a Bonus Task
Bonus Task 2
Take Task 1 further and update the transfer_money() and request_money() methods so that no amount greater than what is available can be transferred from one account to another.


