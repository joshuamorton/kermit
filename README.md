# kermit

Kermit is a tool to allows students, and anyone else wishing to do so, to
interactively explore and make queries about college courses. This currently
includes answering questions like 

 - What does a graph of all courses and prerequisites look like?
 - What prerequisites does a course have?
 - What is the longest chain of prerequisites that a course has, or in other
    words, how long will it take me to be able to take this course?

kermit is currently in development.

To download: `git clone`.

To test: `nosetests`

Dependencies:

 - Python3.4
 - graphviz
 - graphviz (the python module)
 - nosetests (for testing)
 - coverage (for testing)