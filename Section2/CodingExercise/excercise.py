 # Input names and add them in a list. After all, show the list

user_prompt = 'Enter different names(DONE to finish): '
allNames = []

while True:
    names = input(user_prompt)
    print(names.capitalize())
    
    if names.upper() == 'DONE':
        break
    allNames.append(names.capitalize())

print(allNames)