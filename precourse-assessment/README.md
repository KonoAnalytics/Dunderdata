# Precourse Assessment

This repository contains a test of the material covered throught the precourse.

### Getting Started
Open the file `assessment.py` in a text editor. This file contains many functions that need to be completed. They currently use the keyword `pass` as a placeholder. Delete it and write the body of the function.

### Checking Correctness
To check your solutions you will run the file `assessment_unittest.py` from the command line.

```
>>> python assessment_unittest.py
```
### Assessment output
After running the above command, you will get a message informing you of your performance. If any of the functions produced an incorrect result you will see:

```
 FAILED (failures=m, errors=n)
 ```
 where m is the number of failures and n is number of errors. A failure is when your code runs without an error but produces a result that does not match the expected output. An error is a normal Python error (syntax error, attribute error, etc...). 

 The output also tells you which functions are failing the test. Look back up to see the exact names of the functions that are failing. Correct functions produce no output.

 When all functions return the correct answer, the output from the test will simply be `OK`.

 ### More on unit testing
 This test uses the [`unittest`](https://docs.python.org/3/library/unittest.html) package in Python. Pandas uses a similar testing tool called nose and runs many thousands of tests. All tests must pass before any code can be changed. See [test driven development](https://en.wikipedia.org/wiki/Test-driven_development) for more on testing. 
