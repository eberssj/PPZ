import random

vetor_1 = random.sample(range(100), 10)
vetor_2 = random.sample(range(100), 10)
vetor_3 = []
for n in range(10):
    vetor_3.append(vetor_1[n])
    vetor_3.append(vetor_2[n])

print("Vetor um: ", vetor_1)
print("Vetor dois: ", vetor_2)
print("Vetor três: ", vetor_3)