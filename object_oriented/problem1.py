class programmer:
    company="Microsoft"
    # role= "developer"
    # salary= 1200000
# rohan = programmer()
# rohan.name = "Rohan"
# print(rohan.name, rohan.company, rohan.role, rohan.salary)
# harsh = programmer()
# harsh.name= "Harsh"
# harsh.role= "UI / UX designer"
# print(harsh.name,harsh.company, harsh.role, harsh.salary)

# better way
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

p = programmer("harry", 1500000, 24)
print(p.name, p.salary, p.age)

k = programmer("kavya", 1200000, 21)
print(k.name, k.salary, k.age)
