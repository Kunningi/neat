from AxelrodCulture import Axelrod
import time

Enable_CC = True
Size = 20
Features = 2
Traits = 4
epc = 20000 / (10*10)    #ratio of events per cell in Axelrod's results


def time_sim():    #plots similarity and feature 0 every e steps
    
    start = time.time()
    t = Axelrod(Enable_CC, Size, Features, Traits)
    e = int(epc * Size * Size)
    
    for i in range(5):
        
        t.show_similarity()
        t.show_feature(0)
        t.steps(e)

    print('========  %s sec elapsed  ========' % (time.time()-start))
    return


def cc_test():    #this should be changed to plot the same graph under n different features, traits
    
    start = time.time()
    c = Axelrod(Enable_CC, Size, Features, Traits)
    e = int(epc * Size * Size)

    for i in range(5):
        
        c.show_similarity()
        c.show_feature(0)
        c.steps(e)

    print('========  %s sec elapsed  ========' % (time.time()-start))
    return


def neighborhood_sim():
    
    start = time.time()
    n = Axelrod(Enable_CC, Size, Features, Traits)
    e = int(epc * Size * Size)
    n.steps(e * 4)
    
    for f in range(n.nf):
        n.show_feature(f)
        
    n.show_similarity()
    print('========  %s sec elapsed  ========' % (time.time()-start))

    return


def rep_sim():

    start = time.time()
    r = Axelrod(Enable_CC, Size, Features, Traits)
    e = int(epc * Size * Size)

    #populate model with actual data from Axelrod 1997
    r.grid[0][0] = [7,4,7,4,1]
    r.grid[1][0] = [0,1,9,4,8]
    r.grid[2][0] = [4,9,4,4,7]
    r.grid[3][0] = [2,2,7,8,1]
    r.grid[4][0] = [0,9,5,8,1]
    r.grid[5][0] = [5,6,3,5,2]
    r.grid[6][0] = [4,6,2,3,8]
    r.grid[7][0] = [8,8,1,3,6]
    r.grid[8][0] = [3,5,6,8,2]
    r.grid[9][0] = [5,7,8,1,6]
    r.grid[0][1] = [8,7,2,5,4]
    r.grid[1][1] = [0,9,2,3,4]
    r.grid[2][1] = [4,6,0,1,2]
    r.grid[3][1] = [8,5,5,4,1]
    r.grid[4][1] = [8,9,8,0,0]
    r.grid[5][1] = [3,4,4,9,0]
    r.grid[6][1] = [3,8,0,3,2]
    r.grid[7][1] = [2,1,5,9,3]
    r.grid[8][1] = [1,9,2,3,2]
    r.grid[9][1] = [5,5,2,8,5]
    r.grid[0][2] = [8,2,3,3,0]
    r.grid[1][2] = [6,7,7,3,0]
    r.grid[2][2] = [4,2,6,2,8]
    r.grid[3][2] = [5,1,5,8,5]
    r.grid[4][2] = [7,2,0,3,1]
    r.grid[5][2] = [4,8,4,1,6]
    r.grid[6][2] = [3,4,2,3,5]
    r.grid[7][2] = [7,7,4,0,4]
    r.grid[8][2] = [8,0,1,7,3]
    r.grid[9][2] = [6,6,3,2,9]
    r.grid[0][3] = [1,7,9,9,3]
    r.grid[1][3] = [8,9,1,3,0]
    r.grid[2][3] = [8,6,6,3,6]
    r.grid[3][3] = [8,4,4,6,8]
    r.grid[4][3] = [1,9,8,5,6]
    r.grid[5][3] = [5,5,4,5,5]
    r.grid[6][3] = [4,5,6,0,2]
    r.grid[7][3] = [1,7,0,4,3]
    r.grid[8][3] = [8,1,4,4,7]
    r.grid[9][3] = [3,0,4,6,2]
    r.grid[0][4] = [2,2,9,7,8]
    r.grid[1][4] = [3,4,2,1,0]
    r.grid[2][4] = [2,7,4,0,5]
    r.grid[3][4] = [1,8,1,2,2]
    r.grid[4][4] = [0,8,0,7,1]
    r.grid[5][4] = [8,8,6,0,0]
    r.grid[6][4] = [3,9,8,9,1]
    r.grid[7][4] = [3,9,2,3,8]
    r.grid[8][4] = [2,2,8,8,4]
    r.grid[9][4] = [3,6,7,2,9]
    r.grid[0][5] = [8,2,7,6,2]
    r.grid[1][5] = [8,5,4,0,3]
    r.grid[2][5] = [3,9,7,4,7]
    r.grid[3][5] = [6,0,0,9,4]
    r.grid[4][5] = [9,7,7,4,4]
    r.grid[5][5] = [7,8,2,9,5]
    r.grid[6][5] = [8,4,8,6,6]
    r.grid[7][5] = [8,1,4,5,4]
    r.grid[8][5] = [5,8,2,6,0]
    r.grid[9][5] = [1,3,3,4,1]
    r.grid[0][6] = [8,7,4,7,6]
    r.grid[1][6] = [6,9,4,1,1]
    r.grid[2][6] = [9,7,4,5,0]
    r.grid[3][6] = [7,1,8,1,9]
    r.grid[4][6] = [4,2,5,3,3]
    r.grid[5][6] = [6,9,8,9,6]
    r.grid[6][6] = [3,8,4,5,6]
    r.grid[7][6] = [2,9,4,6,4]
    r.grid[8][6] = [5,3,4,3,6]
    r.grid[9][6] = [4,3,9,8,6]
    r.grid[0][7] = [2,6,7,5,7]
    r.grid[1][7] = [8,1,6,7,7]
    r.grid[2][7] = [7,1,8,3,3]
    r.grid[3][7] = [5,1,9,1,2]
    r.grid[4][7] = [3,3,7,2,3]
    r.grid[5][7] = [9,6,7,7,5]
    r.grid[6][7] = [7,8,0,0,8]
    r.grid[7][7] = [7,4,5,7,6]
    r.grid[8][7] = [1,3,6,2,3]
    r.grid[9][7] = [4,5,5,7,8]
    r.grid[0][8] = [9,9,3,1,3]
    r.grid[1][8] = [0,6,7,8,9]
    r.grid[2][8] = [0,7,1,9,2]
    r.grid[3][8] = [3,2,0,9,5]
    r.grid[4][8] = [2,4,6,5,9]
    r.grid[5][8] = [8,6,7,1,4]
    r.grid[6][8] = [2,7,1,3,6]
    r.grid[7][8] = [4,1,9,2,4]
    r.grid[8][8] = [0,5,7,2,9]
    r.grid[9][8] = [6,4,5,8,5]
    r.grid[0][9] = [3,2,0,0,9]
    r.grid[1][9] = [2,4,0,4,2]
    r.grid[2][9] = [8,7,4,2,6]
    r.grid[3][9] = [1,1,3,1,8]
    r.grid[4][9] = [0,3,8,4,7]
    r.grid[5][9] = [0,2,9,3,2]
    r.grid[6][9] = [5,0,1,5,3]
    r.grid[7][9] = [4,3,9,8,7]
    r.grid[8][9] = [4,3,3,7,8]
    r.grid[9][9] = [4,7,3,3,0]

    for i in range(5):
    
        r.show_similarity()
        r.show_feature(0)
        r.steps(e)

    print('========  %s sec elapsed  ========' % (time.time()-start))
    return

#--------------------------CALLS------------------------------------------------
        
time_sim()