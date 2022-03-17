def computegrade(score):
    try:
        score = float(score)
    except:
        return "Bad score"
    if score < 0 or score > 1:
        return "Bad score"
    if score >= 0.9:
        return "A"
    elif score > 0.8:
        return "B"
    elif score > 0.7:
        return "C"
    elif score > 0.6:
        return "D"
    elif score <= 0.6:
        return "F"


score = input("Enter score")
print(computegrade(score))
