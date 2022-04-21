[![unitTest](https://github.com/TobiasRothlin/DevOpsPipeline/actions/workflows/CodeTest.yml/badge.svg)](https://github.com/TobiasRothlin/DevOpsPipeline/actions/workflows/CodeTest.yml)

# DevOps Pipeline
For efficient development the build, test and deployment of a project needs to be automated. This is an attempt of doing this. The Ideas in this Repo are based on the Book [Python for DevOps](https://www.oreilly.com/library/view/python-for-devops/9781492057680/) 
and [Practical MLOps](https://www.oreilly.com/library/view/practical-mlops/9781098103002/)

## Folder Structure

### makefile
The makefile is the central part of the project. It automates different parts of the development process.

Open a terminal session in the repo folder.
###
```
make
```
will create a Virtual Environment and install all dependencies.
###
```
make setup 
```
same as make
###
```
make clean 
```
deletes the Virtual Environment and the __pycache__ folders.
###
```
make test 
```
```cmd
test_Add (__main__.TestBasicMathFunctions) ... ok
test_Multiply (__main__.TestBasicMathFunctions) ... ok
test_Sin (__main__.TestBasicMathFunctions) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
runs all tests for the Module BasicMathFunctions.
###
```
make style
```
```cmd
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

rates the code quality of the Module BasicMathFunctions.

### requirements.txt
This file contains all dependencies used in the project

### test_BasicMathFunctions.py
This file contains all test cases for the Module BasicMathFunctions

### BasicMathFunctions.py
This file contains the functions implemented