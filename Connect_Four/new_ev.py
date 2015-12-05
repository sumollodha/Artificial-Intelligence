score = 0
k =4
>>> board = [[0 for i in range(5)] for j in range(5)]
        for row in range(6):
            for col in range(7 - k + 1):
                st  = 0
                for start in xrange(col,col+k-2,1):
                    #print start
                    if(board.get_cell(row, start) == board.get_other_player_id()):
                        continue
                    else:
                        st=start
                        break
                if(st != col+k-2):
                    continue;        
                elif(col-1 >=0 and board.get_cell(row, col-1) == board.get_current_player_id()):
                    score += ((k)*10)
                elif(st+1 < 7 and board.get_cell(row, st+1) == board.get_current_player_id()):
                    score += ((k)*10)