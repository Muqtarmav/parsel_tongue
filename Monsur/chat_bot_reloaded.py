dictionary = {
    "love":  ["yes, I love you!", "No, I don't love you!", "Nah!", "Love is wicked"],
    "age": ["number for number in range(18, 50)"],
    "country": ["France", "UK", "Nigeria"],
    "siblings": ["number for number in range(1, 6)"],
    "crazy": ["A lil", "Not at all", "Sometimes"],
    "relationships": ["Wow, even the gods do not know", "Yes, I am single", "It is complicated"]
    }
while True:
    user = input()
    for keys, value in dictionary.item():
        if user in keys:
            print(random.choice(value))





