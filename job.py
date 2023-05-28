n = 3 
jobs = [['Job1', '2', '100'], ['Job2', '3', '450'], ['Job3', '3', '325']]
sorter = lambda job: int(job[2])
jobs = sorted(jobs, key=sorter, reverse=True)
scheduled = []
time = 0
for i in jobs:
    deadline =int(i[1])
    jobId=i[0]
    if time <=deadline :
        scheduled.append(jobId)
        time += 1

print("Jobs are scheduled as:")
print(scheduled)