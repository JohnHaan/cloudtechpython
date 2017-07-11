def profile():
    name = "Danny"
    age=30
    return (name,age)
    
profile_data = profile()
print(profile_data[0])
print(profile_data[1])

name,age = profile()
print("%s, %s" % (name,age))