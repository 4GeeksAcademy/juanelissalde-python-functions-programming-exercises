# Your code goes here:
def render_person(name, born, color, age, sex):
    txt = name+" is a "+str(age)+" years old "+sex+" born in "+born+" with "+color+" eyes"
    return txt
#Bob is a 23 years old male born in 05/22/1983 with green eyes


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))