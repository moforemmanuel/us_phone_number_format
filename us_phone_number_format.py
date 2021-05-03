def phone(n):
    num=[]
    s=''

    print("Enter numbers : ")
    for i in range(n):
        num.append(int(input()))

    for i in range(n):
        s += str(num[i])

    return f"({s[0:3]}) {s[3:6]}-{s[6:n]}"


print(phone(10))

