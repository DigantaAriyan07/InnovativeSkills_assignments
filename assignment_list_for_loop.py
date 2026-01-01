#task 1
readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]
print(f"Original Readings: {readings}")

for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i] = 0.0

print(f"\nReadings after replacement: {readings}")

#task 2
for i in range(len(readings)):
    readings[i] = readings[i] + (readings[i] * 0.1)

print(f"\nReadings after increase 10%: {readings}")

#task 3
low_quality_log = []
for i in range(len(readings)):
    if readings[i] < 15.0:
        low_quality_log.append(readings[i])

print(f"\nLow quality log: {low_quality_log}")

for i in range(len(readings)-1, -1, -1):
    if readings[i] < 15.0:
        readings.pop(i)

print(f"\nReadings after filtering: {readings}")
