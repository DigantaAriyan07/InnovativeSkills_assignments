def grade_point(total):
    if total >= 80: return 4.0
    elif total >= 75: return 3.75
    elif total >= 70: return 3.5
    elif total >= 65: return 3.25
    elif total >= 60: return 3.0
    elif total >= 55: return 2.75
    elif total >= 50: return 2.5
    elif total >= 45: return 2.25
    elif total >= 40: return 2.0
    else: return 0.0


dept = input("Enter Department (CSE / EEE / BBA / ENG / LAW): ").upper()

total_gp = 0
total_credit = 0

def take_subject(name):
    global total_gp, total_credit
    ct = float(input(f"{name} CT: "))
    mid = float(input(f"{name} Mid: "))
    final = float(input(f"{name} Final: "))
    total = ct + mid + final
    gp = grade_point(total)
    total_gp += gp * 3
    total_credit += 3


if dept == "CSE":
    take_subject("Programming")
    take_subject("Data Structure")
    take_subject("Discrete Math")
    take_subject("OOP")
    take_subject("Digital Logic")

elif dept == "EEE":
    take_subject("Circuit")
    take_subject("Electronics")
    take_subject("Math")
    take_subject("Signals")
    take_subject("Physics")

elif dept == "BBA":
    take_subject("Accounting")
    take_subject("Management")
    take_subject("Finance")
    take_subject("Marketing")
    take_subject("Economics")

elif dept == "ENG":
    take_subject("Poetry")
    take_subject("Drama")
    take_subject("Novel")
    take_subject("Linguistics")
    take_subject("Composition")

elif dept == "LAW":
    take_subject("Constitution")
    take_subject("Criminal Law")
    take_subject("Civil Law")
    take_subject("Jurisprudence")
    take_subject("International Law")

else:
    print("Invalid Department")
    exit()

cgpa = total_gp / total_credit
print("CGPA:", round(cgpa, 2))
