# Dunder Data Pre-course Assignment
This repository contains a pre-course assignment that is intended to get everyone on the same page upon entering the class so we can quickly dive into the material. It will cover...  

1. Installation and basics of git/github
1. Installation of Anaconda
1. Intro to Jupyter notebooks
1. Intro to the Python programming language
1. Intro to the pandas and numpy libraries.

# Course Assumptions
There is virtually no pre-requisite knowledge assumed for this course other than a desire to get better at making sense of data. That said, this pre-course will cover quite a lot of material and it is expected that all students come to class with a good understanding of it. There will be an assessment given to you a few days before class to test you on the skills you learn during this pre-course assignment.

# Course Objective
Welcome to the universe of 'making sense of data'. It spans a gigantic amount of academic disciplines and careers and would take many lifetimes to ingest into a human brain. There are many starting places for an introductory course such as this one. If we can divide this universe into three major sections (osbscuring tremendous detail) that encompass all that happens within a data analysis, we might come up with:

1. Obtaining data
2. Exploring data
3. Analyzing data

All the sections have both theory (or convention/heuristics) and tools (software) that deliver the resutls. This class will cover just a small corner of exploring data by concentrating on a specific tool (pandas) to manipulate data. While there are many, many tools that can be used to explore data, it is vital (in my opinion) to become an expert in at least one so that any data exploratory task is within your capabilities. Put another way, it is more valuable to become 90% capable in one tool than 30% capable in 10 tools. Once you go deep with one tool, you can easily obtain the same skill level in another as usually (for the high-level data science tools), there are only small differences in syntax and functionality and a tremendous amount of overlap.

Becoming a pandas expert in one week is a difficult task. The library has seemingly endless capabilities and we attempt to cover much of it. The main objective of this course is to introduce you to the core features and functionality of the pandas library through examples and exercises. By the end of this course you should be able to:

1. Have command of basic Python
2. run basic git commands to manage changes to your code
3. Feel comfortable exploring the pandas API to meet any data exploration need
4. Have a basic grasp on how to visualize data using matplotlib

# Installing Anaconda
We will be using the excellent and free Anaconda Python distribution to install all the popular data exploration libraries (along with hundreds more other popular ones). Python has been undergoing an agonizingly slow change from version 2 to 3 though Python 3 came out 8 years ago. Currently, nearly all major libraries have Python 3 support so please [download Anaconda for python 3.6](https://www.continuum.io/downloads). Use command `conda install <packagename>` to get new packages and `conda update --all` to update all packages. There is of course plenty more you can do [with conda](http://conda.pydata.org/docs/using/using.html) including setting up different environments for python 2 and 3 separately.

# Git
Since you have access to this repository you have already successfully created a github account. To get the most out of this course you will need to install [git](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics), a very popular open-source version control system that takes snapshots in time of what your current project looks like. Git itself can be very complex and there are many books written on just how to use git but we don't need anything except the very basics for our purposes. 

## Git vs Github 
Github is a private company that hosts your git repositories online for others to view and collaborate with. Git is your local version control system that keeps track of all local file changes. In this course you will be using github to bring our online repositories to your local machines where you will make changes(i.e. complete the assignments) and push those changes back to us where we will be able view and comment on your assignments.  

### Let's get started with git!
1. [Download git.](https://git-scm.com/download) I believe both mac and linux machines should have git pre-installed.
1. If you've never set-up git before, you need to set your username and email. [Go here](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#Your-Identity) and follow the short instructions.
1. Fork this repository by going to the top right corner of this page and clicking fork.
1. Clone this repository to your local computer. Above the file listings towards the top of this page you will see a green button with the words 'clone or download' in it. Click that button and click the small clipboard icon with the url of this repo with .git appended to it. This will copy the url.
1. Open a terminal and `cd` into a directory that you'd like to save all your work for this class. Perhaps call it `Dunder Data Python Class`
1. Once in that directory, type in `git clone https://github.com/<your username>/precourse-assignment.git`. Use your copied url here. This will pull all the files down into your local file system. You now have an exact replica of what you are reading here on github.

### Submitting your first assignment on github

1. For this pre-course assignment, you will be modifying only the `.ipynb` files.
1. As you are making changes to your files locally, it is a good idea to be continually committing your changes and pushing them to github.
1. Run `git add <filename>.ipynb` to tell git this is the file you would like to be committing
1. If you have edited multiple .ipynb files you can simply write `git add *.ipynb` to add all the .ipynb files to the index (index is a term for the staging area - the area right before you commit and take the snapshot)
1. Run `git commit -m "I have finished the section on lists"` to commit your file locally and 'take a snapshot'. Always add messages to your commits with `-m "<your message here>"`
1. Run `git push origin master` to push your changes to your remote repository on github. Check github to make sure the remote files were changed
1. repeat steps 3-6 several times during the pre-course assignment to ensure you don't lose your changes

# Repository Files
 As you can see at the top of this page, there are multiple files in this repository. 

1. The README file that you are reading right now
1. The `.ipynb` files where all the magic happens
1. A resources section with lots of places to get help and learn more
1. A section on getting started on spaced repitition - a proven method to help retain knowledge for longer periods of time.

# The Actual Assignment!
OK, so you've installed Anaconda and git and are ready for your pre-course assignment. To begin learning...

1. Open a terminal (cmd prompt for windows users)
1. `cd` into the directory where this file is located (the place you cloned this repository)
1. Run command `jupyter notebook`
1. A new browser tab will open up located at `localhost:8888` with a listing of all the files in your directory. 
1. Click on `1. Intro Jupyter Notebook.ipynb` and an Jupyter notebook will open that will walk you through the entire assignment.
1. Complete each numbered notebook
1. Check your answers as you go by opening the precourse solutions notebook only AFTER you have attempted the problems on your own
1. There are 80 practice problems. It is mandatory that you complete the precourse. We will immediate begin learning pandas on day 1.
1. Check out the resources and spaced repititon pages as well.

Remember to always be committing. Please finish the assignment before the start of the course. Answers will be provided a few days prior to the course.

# Extra
Since there is an incredible and often times intimidating amount of material to cover, the next two sections can be immensely helpful for finding resources for a specific topic and for internalizing as much previous material as possible.

## Resources
https://github.com/tdpetrou/precourse-assignment/blob/master/resources.md

## Spaced Repitition
https://github.com/tdpetrou/precourse-assignment/blob/master/spaced-repetition.md
