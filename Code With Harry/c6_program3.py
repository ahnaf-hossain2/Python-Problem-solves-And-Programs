english = int(input("Enter marks for English: "))
ip = int(input("Enter marks for IP: "))
ipLab = int(input("Enter marks for IP LAB: "))

print("Pass in English" if english >= 33 else "Fail in English")
print("Pass in IP" if ip >= 33 else "Fail in IP")
print("Pass in IP LAB" if ipLab >= 33 else "Fail in IP LAB")

overall = (english + ip + ipLab)/3
print("Pass Overall" if overall >= 40 else "Fail Overall")
