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


total_gp = 0
total_credit = 0

def take_subject(name, credit):
    global total_gp, total_credit
    ct = float(input(f"{name} CT: "))
    mid = float(input(f"{name} Mid: "))
    final = float(input(f"{name} Final: "))
    total = ct + mid + final
    gp = grade_point(total)
    total_gp += gp * credit
    total_credit += credit


dept = input("Enter Department (CSE / EEE / BBA / ENG / LAW): ").upper()

if dept == "CSE":
    take_subject("Programming", 3)
    take_subject("Data Structure", 3)
    take_subject("Discrete Math", 2)
    take_subject("OOP", 3)
    take_subject("Digital Logic", 2)

elif dept == "EEE":
    take_subject("Circuit", 3)
    take_subject("Electronics", 3)
    take_subject("Math", 3)
    take_subject("Signals", 2)
    take_subject("Physics", 2)

elif dept == "BBA":
    take_subject("Accounting", 3)
    take_subject("Management", 3)
    take_subject("Finance", 3)
    take_subject("Marketing", 2)
    take_subject("Economics", 2)

elif dept == "ENG":
    take_subject("Poetry", 3)
    take_subject("Drama", 2)
    take_subject("Novel", 3)
    take_subject("Linguistics", 2)
    take_subject("Composition", 3)

elif dept == "LAW":
    take_subject("Constitution", 3)
    take_subject("Criminal Law", 3)
    take_subject("Civil Law", 3)
    take_subject("Jurisprudence", 2)
    take_subject("International Law", 2)

else:
    print("Invalid Department")
    exit()

cgpa = total_gp / total_credit
print("CGPA:", round(cgpa, 2))
