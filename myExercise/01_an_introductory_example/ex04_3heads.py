from random import uniform

N = 10 #number of coin flipping

x = []
payout = 0
for i in range(N):
    x.append(uniform(0,1))
    if i-2>=0:
        if x[i]>0.5:
            if x[i-1]>0.5:
                if x[i-2]>0.5:
                    payout = 1
                    break
                
x = [round(y,2) for y in x]

print('Trials:', x)
print('Payout:', payout)
        