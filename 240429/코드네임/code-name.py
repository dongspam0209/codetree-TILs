class Agent:
    def __init__(self,code_name,score):
        self.code_name=code_name
        self.score=score
Agents=[]
for _ in range(5):
    code_name,score=input().split()
    score=int(score)
    Agents.append(Agent(code_name,score))

min_agent=''
min_score=100
for agent in Agents:
    if min_score>agent.score:
        min_score=agent.score
        min_agent=agent.code_name

print(min_agent,min_score)