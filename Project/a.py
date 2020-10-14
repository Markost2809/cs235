cm = int(input("Enter Height:"))

feet = cm // 30.48

inches = (cm % 30.48) / 2.54

print(f"{feet} feet {inches} inches")
