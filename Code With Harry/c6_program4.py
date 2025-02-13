ban1 = "Make a lot of money"
ban2 = "buy now"
ban3 = "subscribe this"
ban4 = "click this"

message = input("Comment: ")
if((ban1 in message) or (ban2 in message) or (ban3 in message) or (ban4 in message)):
    print("Spam")
else:
    print("Message")
