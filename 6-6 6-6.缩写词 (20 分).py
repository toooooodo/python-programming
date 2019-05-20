def acronym(phrase):
    phrase=phrase.title()
    lst=phrase.strip().split()
    str=''
    for i in lst:
        str+=i[0]
    return str

phrase=input()
print(acronym(phrase))