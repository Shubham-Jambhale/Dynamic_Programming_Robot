def max_steps ( grid ) :
    dicti = {}
    count = 0
    if not grid:
        return 0
    reached=[]
#creating a grid for marking and storing the paths length from the nodes which we have already visited for reuse
    for i in range(len(grid[0])):
        reached.append([0] * len(grid))
    max_count=1
    #traveresing and finding the path
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_count = max(max_count, neighbour_find(grid,i,j,reached))
    return max_count-1

#this function is recursively called and is used for finding the path
def neighbour_find(grid, i, j,reached):
    #if found in the reached matrix return and dont compute further
    if reached[i][j]:
        return reached[i][j]          

    path1=0 
    path2=0 
    path3=0
    path4=0
    #traversing all the four sides of node
    if ((j-1)>=0 and grid[i][j-1]>grid[i][j]):
        path1 = neighbour_find(grid, i, j-1,reached)
    if ((i-1) >=0 and grid[i-1][j]>grid[i][j]):
        path2 = neighbour_find(grid, i-1, j,reached)
    if ((j+1) < len(grid) and grid[i][j+1]>grid[i][j]):
        path3 = neighbour_find(grid, i, j+1,reached)
    if ((i+1) < len(grid) and grid[i+1][j]>grid[i][j]):
        path4 = neighbour_find(grid, i+1, j,reached)
   
    #adding the found path to the reached matrix
    reached[i][j] = 1 + max(path1,path2,path3,path4)
    return 1 + max(path1,path2,path3,path4)
        

if __name__ == '__main__':
    
    print("----Output------")
    print("grid is :['c','d','c'],['a','a','a'],['a','a','a']")
    get_steps = max_steps([['c','d','c'],['a','a','a'],['a','a','a']])
    print("output :",get_steps)
    print()
    print("gris is: ['t', 'o', 'y'], ['c', 'a', 't'], ['t', 'o' , 'p'] ")
    get_steps = max_steps([['t', 'o', 'y'], ['c', 'a', 't'], ['t', 'o' , 'p']])
    print("output :",get_steps)
    print()
    print("grid is:['d','z'],['c','a']")
    get_steps = max_steps([['d','z'],['c','a']])
    print("output :",get_steps)
    print()
    print("grid is:['a','a','a'],['a','c','a'],['a','a','a']")
    get_steps = max_steps([['a','a','a'],['a','c','a'],['a','a','a']]) 
    print("output :",get_steps)
        