graph = {
        "A" : ['B', 'C'],
        "B" : ['A', 'C', 'D'],
        "C" : ['A', 'B', 'D', 'E'],
        "D" : ['A', 'C', 'E', 'F'],
        "E" : ['C', 'D', 'F'],
        "F" : ['D', 'E'],
}
graph = {
        "0" : ['1','2','3'],
        "1" : ['4'],
        "2" : ['5'],
        "3" : ['5','6','7'],
        "4" : ['8','11'],
        "5" : ['9'],
        "6" :[],
        "7" :['6'],
        "8" :[],
        "9" :['10'],
        "10" :['12'],
        "11" :['12'],
        "12" :[]
}

visited = []
# A b C d e f 

def bfs(graph , start):
        queue= graph['0']
        while queue :
                print("Queue is %s " % queue)
                s = queue.pop(0)
                visited.append(s)
                print("processing %s " % s)
                
                for v in graph[s]:
                        if v not in queue and v not in visited: 
                                queue.append(v)

bfs(graph, 'A')

