# IEG_MachineLearning
Installation and configuration of virtual environment and flask libraries

1. create a folder called flasktutorial
2. open the folder flasktutorial inside the visual studio code
3. go to terminal and run the command "python -m venv virtual"
4. you can see the virtual folder is created
5. To activate the virtual environment "cd virtual\Scripts => do it again
6. Type "activate"
7. You can see (virtual) current working folder path
8. Let us install flask libraries inside the virtual environment
9. Type cd .. and again cd ..
10. Now you will be inside the flasktutorial
11. Now you type pip install flask
12. the previous command will install all the necessary libraries inside the virtual\Lib\site-packages folder
13. type cd virtual
14. type cd Scripts
15. type deactivate

Developing web application using Flask

1. create a python program called app.py
2. in the terminal make sure you are inside the 



In Python, @staticmethod is a decorator used inside a class to define a method that doesn't operate on an instance of the class (no self parameter), but rather behaves like a regular function. This means:

No Instance Needed: Static methods don't need an instance of the class to be created. They can be called directly on the class itself.

Independent of Instance State: They don't access or modify instance state (attributes or methods) and hence don't require self as the first parameter.

Utility Functions: They are often used for utility functions that are related to the class in some way, but don't depend on specific instance data.