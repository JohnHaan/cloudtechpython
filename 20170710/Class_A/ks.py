def profile():
    name = "Danny"
    age = 30
    return (name, age)

name, age = profile()
print("%s, %s" % (name, age))
