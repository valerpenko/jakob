home=list(input().split())
home_done=list(input().split())
for el in home_done:
    home.pop(home.index(el))
print(home)