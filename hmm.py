import numpy as np
import csv
import pandas as pd
from numpy import asarray
from numpy import save


hidden = []
observables = []

f = open("DadosFoneticosOFICIAL.txt","r+")

Lines = f.readlines()

count = 0
# Strips the newline character
for line in Lines:
	count += 1
	print("{}".format(line.strip()))

	if count % 2 == 0:
		token = line.strip().split(".")
		hidden += token
	else:
		token = line.replace("-","·").strip().split("·")
		observables += token



print("counting.....")
hidden_dict = pd.DataFrame(hidden, columns=["x"]).groupby('x').size().to_dict()
observable_dict = pd.DataFrame(observables, columns=["x"]).groupby('x').size().to_dict()
print("done!!!")
observables = list(dict.fromkeys(observables))
hidden = list(dict.fromkeys(hidden))

#generate the matrices
A = np.zeros((len(observables), len(hidden)))
B = np.zeros((len(observables), len(observables)))
pi = np.zeros(len(observables))
f.close()


# redo again
f = open("DadosFoneticosOFICIAL.txt","r+")

while True:

	line1 = f.readline()
	line2 = f.readline()
	if not line2: break

	emission_states = line1.replace("-","·").strip().split("·")
	hidden_states = line2.strip().split(".")

	for i in range(0, len(emission_states)):


		if i == 0:
			index = observables.index(emission_states[i])
			pi[index] += 1

		a = observables.index(emission_states[i])
		b = hidden.index(hidden_states[i])
		
		A[a][b]+=1

		if i < (len(emission_states) - 1):

			a= observables.index(emission_states[i])
			b = observables.index(emission_states[i+1])

			B[a][b] += 1




#print(observables)
#print(observable_dict)

#print(A+1)
#print(B+1)



for i in range(0, A.shape[0]):

	symbol = observables[i]
	value = observable_dict[symbol]
	A[i] = (A[i])/(value)


B = B+1

for i in range(0, B.shape[0]):
	B[i] = B[i]/np.sum(B[i])


#print(np.count_nonzero(pi == 0))
finalInitialVector = (pi)/((len(Lines)/2))
#print(np.sum(pi))
#print(finalInitialVector)

print(B)


#Validation A
#validationA = list(map(sum,A))
#print(validationA)
#print(len(validationA))

#Validation B:
validationB = list(map(sum,B))
print(validationB)
print(len(validationB))


#print(len(observable_dict))
#print(A.shape[0])
#print(len(Lines))
#print(hidden_dict)
#print(observable_dict)


######################  saving the model  ##############################
output = []

output.append(observables)
output.append(hidden)
output.append(finalInitialVector)
output.append(A)
output.append(B)

data = asarray(output)
save('model.npy', data)

