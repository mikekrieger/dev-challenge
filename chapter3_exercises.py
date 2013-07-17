# Name: Michael Krieger

# Exercise 3.1
repeat_lyrics()
def print_lyrics(): 
	print "I'm a lunberjack, and I'm okay." 
	print "I sleep all night and I work all day"
def repeat_lyrics(): 
    print_lyrics() 
    print_lyrics()

#result: >>> repeat_lyrics()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'repeat_lyrics' is not defined
#>>> def print_lyrics(): print "I'm a lunberjack, and I'm okay." print "I sleep all night and I work all day"
#  File "<stdin>", line 1
    def print_lyrics(): print "I'm a lunberjack, and I'm okay." print "I sleep all night and I work all day"
                                                                    ^
#SyntaxError: invalid syntax
#>>> def repeat_lyrics(): print_lyrics() print_lyrics()

#Exercise 3.2
def repeat_lyrics(): 
	print_lyrics() 
	print_lyrics()
def print_lyrics(): 
	print "I'm a lunberjack, and I'm okay." 
	print "I sleep all night and I work all day"
repeat_lyrics()

#result: SyntaxError: invalid syntax

#Exercise 3.3
str = "allen"
print str.rjust(65, ' ');

#Exercise 3.4.1
def do_twice(f):
     f()
     f()

def print_spam():
     print 'spam'

do_twice(print_spam)
g

#Exercise 3.4.2
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_spam(arg):
    print 'spam'

do_twice(print_spam, 'spam')

#Exercise 3.4.3
def do_twice(f):
    f()
    f()
 

def do_twice(f):
    f()
    f()

def print_twice():
    print 'spam'

do_twice(print_twice)

# Exercise 3.4.4
def print_twice(f, arg):
    f(arg)
    f(arg)

def print_spam(arg):
    print arg

print_twice(print_spam, 'spam')

#Exercise 3.4.5
do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')
print ''

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')
print ''