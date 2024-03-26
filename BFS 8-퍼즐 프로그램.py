#BFS 8-퍼즐 프로그램

#상태 클래스
class State:
    def __init__(self, board,goal,depth=0):
        self.board = board
        self.depth = depth
        self.goal = goal
        
# i1과 i2 교환후 새로운 상태 반환
    def get_new_board(self,i1,i2,depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board,self.goal,depth)
    
#자식 노드를 확장해서 리스트에 저장해서 반환
    def expand(self,depth):
        result = []
        new_board = []
        i = self.board.index(0) #0의 위치를 i에 저장
        if not i in [0,3,6]: #왼쪽으로 이동할수 있다면 왼쪽이동
            result.append(self.get_new_board(i,i-1,depth))
        if not i in [0,1,2]: #위로 이동할수 있다면 위로 이동
            result.append(self.get_new_board(i,i-3,depth))
        if not i in [2,5,8]: #오른쪽으로 이동할수 있다면 오른쪽    이동 
            result.append(self.get_new_board(i,i+1,depth))
        if not i in [6,7,8]: #아래로 이동할수 있다면 아래로 이동
            result.append(self.get_new_board(i,i+3,depth))
        return result

    #객체 출력
    def __str__(self):
        return str(self.board[:3])+"\n"+\
        str(self.board[3:6])+"\n"+\
        str(self.board[6:])+"\n"+\
        "--------------------"

    #in연산자 작동시키기    
    def __eq__(self,other):
        return self.board == other.board

    def __ne__(self,other):
        return self.board != other.board
    
#초기상태
puzzle = [  2,8,3,
            1,6,4,
            7,0,5 ]
goal = [ 1,2,3,
         8,0,4,
         7,6,5]

#open List
open_queue = []
open_queue.append(State(puzzle,goal))

closed_queue =[]

depth = 0
count = 1

while len(open_queue) != 0:
    current = open_queue.pop(0) #닫을거니까 open에서 삭제
    print(count)
    count += 1
    print(current)
    if current.board == goal:
        print("탐색 끝!")
        break
    depth = current.depth+1
    closed_queue.append(current)
    if depth > 5: #편의상 제한한다
        continue
    for state in current.expand(depth):
        if (state in closed_queue) or (state in open_queue):
            continue
        else:
            open_queue.append(state)
