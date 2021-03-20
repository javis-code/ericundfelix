gefühl = input()

gut = ["gut", "schön"]
schlecht = ["schlecht", "scheisse"]

if gefühl.lower().strip() in gut:
    print("Das freut mich")
elif gefühl.lower().strip() in schlecht:
    print(":C")
else: 
    print("bruh")