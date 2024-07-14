import random 

temp=[]
for i in range (7):
	temp.append(random.randint(26,41))
days_of_the_week=["sunday","monday","tuesday","wednsday","thirsday","friday","saturday"]

good_days_count=0
good_days=[]
even_days=[]

for i in range (len(temp)):
	if temp[i]%2==0:
		good_days_count+=1
		even_days.append(days_of_the_week[i])

max_temp=max(temp)
min_temp=min(temp)
max_temp_day=days_of_the_week[temp.index(max_temp)]
min_temp_day=days_of_the_week[temp.index(min_temp)]

avg_temp= sum(temp)/len(temp)
above_avg=[temp for temp in temp if temp>avg_temp]

print("the weather report of the week:" temp)
print("shelly had", even_days , "good days")
print("the hotest temp was:", max_tempt,"on", max_temp_day)
print("the coldest temp was:", min_tempt,"on", min_temp_day) 
print("days that were above the average temps:", above_avg)



