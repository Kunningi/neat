from AxelrodCulture import Axelrod


def basic_sim(enable_cc):
    
    basic = Axelrod(enable_cc, 10, 5, 10)
    
    for i in range(5):
        
        basic.show_similarity()
        basic.show_feature()
        basic.steps(20000)

    return




def rep_sim(enable_cc):

    rep = Axelrod(enable_cc, 10, 5, 10)
    
    #populate model with actual data from Axelrod 1997
    rep.grid[0][0] = [7,4,7,4,1]
    rep.grid[1][0] = [0,1,9,4,8]
    rep.grid[2][0] = [4,9,4,4,7]
    rep.grid[3][0] = [2,2,7,8,1]
    rep.grid[4][0] = [0,9,5,8,1]
    rep.grid[5][0] = [5,6,3,5,2]
    rep.grid[6][0] = [4,6,2,3,8]
    rep.grid[7][0] = [8,8,1,3,6]
    rep.grid[8][0] = [3,5,6,8,2]
    rep.grid[9][0] = [5,7,8,1,6]
    rep.grid[0][1] = [8,7,2,5,4]
    rep.grid[1][1] = [0,9,2,3,4]
    rep.grid[2][1] = [4,6,0,1,2]
    rep.grid[3][1] = [8,5,5,4,1]
    rep.grid[4][1] = [8,9,8,0,0]
    rep.grid[5][1] = [3,4,4,9,0]
    rep.grid[6][1] = [3,8,0,3,2]
    rep.grid[7][1] = [2,1,5,9,3]
    rep.grid[8][1] = [1,9,2,3,2]
    rep.grid[9][1] = [5,5,2,8,5]
    rep.grid[0][2] = [8,2,3,3,0]
    rep.grid[1][2] = [6,7,7,3,0]
    rep.grid[2][2] = [4,2,6,2,8]
    rep.grid[3][2] = [5,1,5,8,5]
    rep.grid[4][2] = [7,2,0,3,1]
    rep.grid[5][2] = [4,8,4,1,6]
    rep.grid[6][2] = [3,4,2,3,5]
    rep.grid[7][2] = [7,7,4,0,4]
    rep.grid[8][2] = [8,0,1,7,3]
    rep.grid[9][2] = [6,6,3,2,9]
    rep.grid[0][3] = []
    rep.grid[1][3] = []
    rep.grid[2][3] = []
    rep.grid[3][3] = []
    rep.grid[4][3] = []
    rep.grid[5][3] = []
    rep.grid[6][3] = []
    rep.grid[7][3] = []
    rep.grid[8][3] = []
    rep.grid[9][3] = []
    rep.grid[0][4] = []
    rep.grid[1][4] = []
    rep.grid[2][4] = []
    rep.grid[3][4] = []
    rep.grid[4][4] = []
    rep.grid[5][4] = []
    rep.grid[6][4] = []
    rep.grid[7][4] = []
    rep.grid[8][4] = []
    rep.grid[9][4] = []
    rep.grid[0][5] = []
    rep.grid[1][5] = []
    rep.grid[2][5] = []
    rep.grid[3][5] = []
    rep.grid[4][5] = []
    rep.grid[5][5] = []
    rep.grid[6][5] = []
    rep.grid[7][5] = []
    rep.grid[8][5] = []
    rep.grid[9][5] = []
    rep.grid[0][6] = []
    rep.grid[1][6] = []
    rep.grid[2][6] = []
    rep.grid[3][6] = []
    rep.grid[4][6] = []
    rep.grid[5][6] = []
    rep.grid[6][6] = []
    rep.grid[7][6] = []
    rep.grid[8][6] = []
    rep.grid[9][6] = []
    rep.grid[0][7] = []
    rep.grid[1][7] = []
    rep.grid[2][7] = []
    rep.grid[3][7] = []
    rep.grid[4][7] = []
    rep.grid[5][7] = []
    rep.grid[6][7] = []
    rep.grid[7][7] = []
    rep.grid[8][7] = []
    rep.grid[9][7] = []
    rep.grid[0][8] = []
    rep.grid[1][8] = []
    rep.grid[2][8] = []
    rep.grid[3][8] = []
    rep.grid[4][8] = []
    rep.grid[5][8] = []
    rep.grid[6][8] = []
    rep.grid[7][8] = []
    rep.grid[8][8] = []
    rep.grid[9][8] = []
    rep.grid[0][9] = []
    rep.grid[1][9] = []
    rep.grid[2][9] = []
    rep.grid[3][9] = []
    rep.grid[4][9] = []
    rep.grid[5][9] = []
    rep.grid[6][9] = []
    rep.grid[7][9] = []
    rep.grid[8][9] = []
    rep.grid[9][9] = []

    for i in range(5):
    
        rep.show_similarity()
        rep.show_feature()
        rep.steps(20000)


#--------------------------CALLS------------------------------------------------
        
#basic_sim(False)
#basic_sim(True)
rep_sim(False)
rep_sim(True)