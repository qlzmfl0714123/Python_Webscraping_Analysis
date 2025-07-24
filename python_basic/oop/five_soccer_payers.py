#이차원 리스트를 사용하여 여러명의 player 정보 저장하기
names = ["Jin", "Sungchul", "Ronaldo", "Hong", "Seo"]
positions = ["MF","DF", "CF", "WF", "GK"]
numbers = [10, 15, 20, 3, 1]

players = [[name, position, number ]for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

#Class로 선언하여 여러명의 player 정보 저장하기
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center " % (self.name, self.position)

player1 = SoccerPlayer('dooly','MF',10)
print(player1)
player1.change_back_number(20)
print(player1)


player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_objects[0])
print('--------5명 선수정보 출력')
for player in player_objects:
    print(player)