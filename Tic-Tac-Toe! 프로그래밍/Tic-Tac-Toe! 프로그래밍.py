#Tic-Tac-Toe! 프로그래밍

#필드구현
game_board =[   '','','',
                '','','',
                '','','']
            
#비어있는 칸을 따로 분리
def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == '':
            cells.append(x)
    return cells

#비어있는 칸에만 수를 놓는다
def valid_move(x):
    return x in empty_cells(game_board)

#위치에 X 놓기
def move(x,player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False
    
#현재 게임보드를 그린다
def draw(board):
    for i, cell in enumerate(board):
        if i%3 == 0:
            print('\n-------------')
        print('|',cell,'|',end='')
    print('\n-------------')
    
#보드의 상태를 평가
def evaluate(board):
    if check_win(board,'X'):
        score = 1
    elif check_win(board,'O'):
        score = -1
    else:
        score = 0
    return score
    
#Tic-Tac_Toe 규칙에 의거해서 확인한다
def check_win(board,player):
    win_conf = [
        [board[0],board[1],board[2]],
        [board[3],board[4],board[5]],
        [board[6],board[7],board[8]],
        [board[0],board[3],board[6]],
        [board[1],board[4],board[7]],
        [board[2],board[5],board[8]],
        [board[0],board[4],board[8]],
        [board[2],board[4],board[6]]
        ]
    return [player,player,player] in win_conf
    
#누군가가 승리하면 게임은 끝난다
def game_over(board):
    return check_win(board,'X') or check_win(board,'O')
    

#미니맥스 알고리즘 구현
#이 함수는 순환적으로 호출된다
def minimax(board,depth,maxPlayer):
    pos =-1
    #단말노드면 보드를 평가하여 위치와 평가값을 반환
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return evaluate(board)
    if maxPlayer:
        value = -10000 # - 무한
        #자식노드 평가후 최선의 수 찾기
        for p in empty_cells(board):
            board[p] = 'X'
            
            #경기자 교체
            x ,score = minimax(board,depth-1,False)
            board[p] = ''
            if score >value:
                value = score
                pos = p
    else:
        value = +10000 # + 무한
        #자식노드 평가후 최선의 수 찾기
        for p in empty_cells(board):
            board[p] = 'O'
            
            #경기자 교체
            x, score = minimax(board,depth-1,True)
            board[p] = ''
            if score < value :
                value = score
                pos = p
    return pos,value
    
player='X'

#main programm
while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
    i,v = minimax(game_board,9,player=='X')
    move(i,player)
    if player =='X':
        player = 'O'
    else:
        player='X'
        
if check_win(game_board,'X'):
    print('X 승리!')
elif check_win(game_board,'O'):
    print('O 승리!')
else:
    print('비겼습니다!')