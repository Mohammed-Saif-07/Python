age = int(input())

def check(age):
    if(age>=18 and age <= 60):
        return "YES"
    else:
        return "NO"
    
print(check(age))