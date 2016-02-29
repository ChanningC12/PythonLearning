1+1
"1"+1

a=1
class(a)
b="1"
class(b)

# User Defined Functions
my_function = function(name) {
    return(cat("Have a nice day", name))
}
my_function("CC")

# List
things = c("Thing One", "Thing Two")
class(things)
length(things)
things[-2]

# Dictionary-like
my_dict = list(something_unique=1,something_else_unique=2)
my_dict
my_dict$something_unique

# anomymous functions
square = function(x){
    m=x**2
    return(m)
}
square(4)












