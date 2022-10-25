import itertools
from create_matrix import create_matrix
def brute_force(s,matrix):
    k=len(matrix)
    path=[i for i in range(k) if i!=s ]
    all_path=list(itertools.permutations(path))
    route_weight=[]
    for x in all_path:
        x=list(x)
        x.append(s)
        x.insert(0,s)
        weight=0
        for i in range(len(x)-1):
            weight+=matrix[x[i]][x[i+1]]
        route_weight.append(weight)
    min_weight=min(route_weight)
    min_index=route_weight.index(min_weight)
    best_route=list(all_path[min_index][:])
    best_route.append(s)
    best_route.insert(0,s)
    return min_weight,best_route
if __name__=='__main__':
    graph=[[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    s=2
    a,b=brute_force(s,graph)
    print(a,b)