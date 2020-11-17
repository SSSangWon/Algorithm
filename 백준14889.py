from itertools import combinations

#값 받기
n = int(input())
board = list(list(map(int, input().split())) for i in range(n))

#팀이 될 수 있는 경우의 수
Team=[]
for i in combinations([i+1 for i in range(n)],int(n/2)):
    Team.append(i)

#팀 나누기
teamNum = len(Team)
halfTeamNum = teamNum//2
startTeam = [Team[i] for i in range(halfTeamNum)]
rinkTeam =  [Team[i] for i in range(teamNum-1, halfTeamNum-1, -1)]

#각 팀의 점수 구하기
minScore = 100

for i in range(halfTeamNum):
    startTeamScore = 0
    rinkTeamScore = 0

    for j in combinations(startTeam[i], 2):
        startTeamScore += board[j[0]-1][j[1]-1]
        startTeamScore += board[j[1]-1][j[0]-1]
    for j in combinations(rinkTeam[i], 2):
        rinkTeamScore += board[j[0]-1][j[1]-1]
        rinkTeamScore += board[j[1]-1][j[0]-1]

    if abs(startTeamScore-rinkTeamScore) < minScore:
        minScore = abs(startTeamScore-rinkTeamScore)

#출력
print(minScore)