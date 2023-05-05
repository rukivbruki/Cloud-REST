# Python REST API using Flask, Google App Engine and Google Datastore

## Description:

This challenge has 2 tasks:

Getting to know the Google App Engine & creating a basic “Hello, World” app (following the instructions).
Creating a very simple Database app which has a limited command set using the Google App Engine.

### Task I
Create Hello World app using the instructions below (Please use Standard Environment with Python 3)
https://cloud.google.com/appengine/docs/standard/python3/quickstart

Make sure the app is working, send us back all the code you’ve written & a full URL link to your application (http://_
your-app-id.appspot.com/).

### Task II
Your task is to create a very simple database using the Google App Engine.

Your app will receive commands over HTTP requests from the network, all the commands are going to be handled one request
at a time by the server. For simplicity's sake you should ignore multi clients communications issues.

Your App should write appropriate responses to the browser.

Here are the commands you need to handle:

SET – [http://_your-app-id_.appspot.com/set?name={variable_name}&value={variable_value}]
Set the variable_name to the value variable_value, neither variable names nor values will contain spaces. Print the
variable name and value after the change.

GET – [http://_your-app-id_.appspot.com/get?name={variable_name}
Print out the value of the variable_name or “None” if the variable is not set.

UNSET – [http://_your-app-id_.appspot.com/unset?name={variable_name}]
Unset the variable_name, making it just like the variable was never set.

NUMEQUALTO – [http://_your-app-id_.appspot.com/numequalto?value={variable_value}]
Print to the browser the number of variables that are currently set to variable_value. If no variables equal that value,
print 0.

UNDO – [http://_your-app-id_.appspot.com/undo]
Undo the most recent SET/UNSET command. If more than one consecutive UNDO command is issued, the original commands
should be undone in the reverse order of their execution. Print the name and value of the changed variable (after the
undo) if successful, or print NO COMMANDS if no commands may be undone.

Example: If you set the variable name x to the value 13 via request, then you set the variable name x to the value 22
via request, the undo request will undo the assignment of the value 22 to the variable x and will revert it’s value to
13, if then another undo request will be issued it will unset the variable.

REDO – [http://_your-app-id_.appspot.com/redo]
Redo the most recent SET/UNSET command which was undone. If more than one consecutive REDO command is issued, the
original commands should be redone in the original order of their execution. If another command was issued after an
UNDO, the REDO command should do nothing. Print the name and value of the changed variable (after the redo) if
successful, or print NO COMMANDS if no commands may be re-done.

END – [http://_your-app-id_.appspot.com/end]
Exit the program. Your program will always receive this as its last command. You need to remove all your data from the
application (clean all the Datastore entities). Print CLEANED when done.

Here are some example sequences that will help you in debugging your app:

Sequence 1:

1.     Input: http://_your-app-id_.appspot.com/set?name=ex&value=10
   Output: ex = 10
2.     Input: http://_your-app-id_.appspot.com/get?name=ex
   Output: 10
3.     Input: http://_your-app-id_.appspot.com/unset?name=ex
   Output: ex = None
4.     Input: http://_your-app-id_.appspot.com/get?name=ex
   Output: None
5.     Input: http://_your-app-id_.appspot.com/end
   Output: CLEANED

Sequence 2:

1.     Input: http://_your-app-id_.appspot.com/set?name=a&value=10
   Output: a = 10
2.     Input: http://_your-app-id_.appspot.com/set?name=b&value=10
   Output: b = 10
3.     Input: http://_your-app-id_.appspot.com/numequalto?value=10
   Output: 2
4.     Input: http://_your-app-id_.appspot.com/numequalto?value=20
   Output: 0
5.     Input: http://_your-app-id_.appspot.com/set?name=b&value=30
   Output: b = 30
6.     Input: http://_your-app-id_.appspot.com/numequalto?value=10
   Output: 1
7.     Input: http://_your-app-id_.appspot.com/end
   Output: CLEANED

Sequence 3:

1.     Input: http://_your-app-id_.appspot.com/set?name=a&value=10
   Output: a = 10
2.     Input: http://_your-app-id_.appspot.com/set?name=b&value=20
   Output: b = 20
3.     Input: http://_your-app-id_.appspot.com/get?name=a
   Output: 10
4.     Input: http://_your-app-id_.appspot.com/get?name=b
   Output: 20
5.     Input: http://_your-app-id_.appspot.com/undo
   Output: b = None
6.     Input: http://_your-app-id_.appspot.com/get?name=a
   Output: 10
7.     Input: http://_your-app-id_.appspot.com/get?name=b
   Output: None
8.     Input: http://_your-app-id_.appspot.com/set?name=a&value=40
   Output: a = 40
9.     Input: http://_your-app-id_.appspot.com/get?name=a
   Output: 40
10.     Input: http://_your-app-id_.appspot.com/undo
    Output: a = 10
11.     Input: http://_your-app-id_.appspot.com/get?name=a
    Output: 10
12.     Input: http://_your-app-id_.appspot.com/undo
    Output: a = None
13.     Input: http://_your-app-id_.appspot.com/get?name=a
    Output: None
14.     Input: http://_your-app-id_.appspot.com/undo
    Output: NO COMMANDS
15.     INPUT: http://_your-app-id_.appspot.com/redo
    Output: a = 10
16.     INPUT: http://_your-app-id_.appspot.com/redo
    Output: a = 40
15.     Input: http://_your-app-id_.appspot.com/end
    Output: CLEANED

**Important notes (Task II):**

1. When working on the Google App Engine each request is a new task, so you will have to use GAE Datastore to save data
   between requests. Please use the Google App Engine.
   Datastore: (https://cloud.google.com/appengine/docs/standard/python3/building-app/storing-and-retrieving-data)
2. Use the following handlers defined in your main file:
   /get
   /set
   /unset
   /numequalto
   /undo
   /redo
   /end
3. You may assume the following datastore access methods are O(1):
   key-based fetch of an entity value-based query (without sorting) which returns a single entity saving an entity Given
   these assumptions, all commands except END should have an average-case runtime of O(1).
4. Make sure END command will erase all the database data.
