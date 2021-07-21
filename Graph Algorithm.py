# Yong Zi Ying: 30885027
# assignment 4: Graph Algorithm
# Grade: 18/20 HD
#%% Task 1: Bellman Ford
def best_trades(prices, starting_liquid, max_trades, townspeople): 
    ''' This method is to find the maximum values that can be earned by trading water with local people.
    :Input: prices is an array of length n, where n is the number of vertices (prices[i] is the value of 1L of 
            the liquid with ID i.). starting_liquid is the source of the graph. max_trades is the number of columns 
            (Bellman Ford). townspeople are the edges of the graph.  
    :Output: The maximum values that can be earned after trading water for at most max_trades trades. 
    :Time Complexity: Best and Worst time complexity will be the same which is O (T*M), where T is the 
                      total number of trades available (the length of townspeople) and M is the number 
                      of max_trades (number of columns). 
    :Auxiliary Space Complexity: O(2V + 2E) = O (V + E), where V is the number of vertices (length of prices) and 
                                 E is the number of edges (length of townspeople). There are 2 arrays that represent the 
                                 columns (current_volume_column and pre_volume_column) both arrays have the same size as 
                                 the prices O (2V). There are two more arrays which are v_value and edges_list. Both arrays 
                                 have the same size as the townspeople O(2E).      
    :Space Complexity: O (3V + 3E) = O (V + E), space complexity is input space + extra space.
                       The input space is O (V + E), where V is the number of vertices (length of prices) and 
                       E is the number of edges (length of townspeople).
                       The extra space is O (V + E), where V is the number of vertices (length of prices) and 
                       E is the number of edges (length of townspeople) as well (explained above). 
    :Explanation: First, initialize the graph with V number of vertices (length of price) into both 
                  columns/arrays (current_volume_column and pre_volume_column) then set the source to 1 as 
                  default volume of water and the rest of the element is set it to negative infinity. Reusing 2 arrays 
                  instead of creating max_trades number of columns with V*E auxiliary space. Both arrays will store 
                  the volume of the water in every trades. Townspeople is a list in list and the interior list contain 3 
                  element tuples. Loop it and append all tuples into an edges_list array. Loop the edges_list to append
                  all the second element of the tuples which is v (destination) into v_value, v_value array is used to 
                  determine which prices is used to calculate the values for the volume of water that was traded 
                  successfully. Now, Bellman Ford algorithm is used to complete this trading. The maximum value of 
                  the trade will be returned. More details explanation is commented at the code.
    '''
    vertices_size = len(prices)
    current_volume_column = [None] * vertices_size       
    pre_volume_column= [None] * vertices_size

    # initialise the graph: len(prices) = num of vertices
    for i in range(vertices_size):
        if i == starting_liquid:            # source
            current_volume_column[i] = 1    # default volume = 1
            pre_volume_column[i] = 1
        else:                               # set all vertices as -inf
            pre_volume_column[i] = float('-inf') 
            current_volume_column[i] = float('-inf') 
    
    # add_edges: tuples from list in list
    edges_list = []                         # for townspeople
    for person in townspeople:              # add directed && weighted edge
        for trade in person:                # edges = townspeople = trades
            edges_list.append(trade)

    # to get price with v index
    v_value = []
    for edges in edges_list:                # O (T)           
        v = edges[1]                
        v_value.append(v)

    # relax_edges:       
    for _ in range(max_trades):             # O (M)
        for edges in edges_list:            # O (T)           
            u = edges[0]                    # start: depart
            v = edges[1]                    # end: destination
            w = edges[2]                    # weight: ratio
            if pre_volume_column[u]*w > current_volume_column[v]:
                current_volume_column[v] = pre_volume_column[u]*w    # update   
        # switch column
        tem_switch_column = pre_volume_column        
        pre_volume_column = current_volume_column     
        current_volume_column = tem_switch_column
    
    # find maximum value: price*ratio*volume
    max_value = 0
    for i in range(len(pre_volume_column)):
        if (prices[v_value[i]]*pre_volume_column[v_value[i]]) > max_value:
            max_value = prices[v_value[i]]* pre_volume_column[v_value[i]]
    
    # no path exits
    if max_value == 0:  
        max_value = prices[starting_liquid]

    return max_value               

# %% Task 2: Dijkstra 
import heapq
def opt_delivery(n, roads, start, end, delivery):
    ''' This method is used to find the minimum cost to travel from one city to another.
    :Input: n is the vertices (number of cities), roads is edges (a list of tuples), start is the source, 
            end is the destination and delivery is a tuple containing 3 values. 
    :Output: A tuple containing the cost of travelling from start to end and a list of integer that 
             represent the path to travel from source to destination. 
    :Time Complexity: Best and Worst time complexity will be the same which is O (R log(N)), 
                      where R is the number of edges (roads) and N is the number of vertices (cities). 
                      Multiple Dijkstra will be used = 4(R log(N)) = (R log(N)). 
    :Auxiliary Space Complexity: O (M + N), where M is length of return_path list and N is the length of 
                                 discovering_source_destination list (number of vertices). O (V), 
                                 where V is the length of finalized_path list from dijkstraAlgo method 
                                 will be same length or smaller than the length of return_path list.  
    :Space Complexity: O (R + 2N + M), space complexity is input space + extra space.
                       Input space is O (R + N), where R is the number of edges (roads) and 
                       N is the number of vertices (cities).
                       Extra space is O (M + N), where M is length of return_path list and 
                       N is the length of discovering_source_destination list (explained above). 
    :Explanation: First, initialize the graph then add edges for all vertices. 
                  Four Dijkstra algorithm will run for start to end, start to pickup, 
                  pickup to delivery and delivery to end. If the cost from start to end without pickup and 
                  delivery is smaller than the cost from start to end with pickup and delivery, 
                  the cost for start to end without pickup and delivery will be prioritized (be lazy); 
                  else the cost for start to end with pickup and delivery will be used. 
                  The smallest cost to travel from start to end will be prioritized. 
                  More details explanation is commented at the code.
    '''
    # initialize graph 
    vertices = [None] * n           # n = num of vertices
    for i in range(n):
        vertices[i] = Vertices(i) 

    # add edges: undirected
    for edge in roads:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        # one way: u to v
        current_edge = Edges(u,v,w)
        current_vertex = vertices[u]
        current_vertex.add_edges(current_edge)
        # two way: v to u
        current_edge = Edges(v,u,w)
        current_vertex = vertices[v]
        current_vertex.add_edges(current_edge)

    # for pickup and delivery
    pickup_u = delivery[0]
    delivered_v = delivery[1]
    delivery_profit = delivery[2]

    # perform multiple dijsktra 
    start_to_end = dijkstraAlgo(start, end, vertices)
    reverse_start_to_end = list(reversed(start_to_end[1]))
    reset(vertices)
    start_to_pickup = dijkstraAlgo(start, pickup_u, vertices)
    reset(vertices)
    pickup_to_delivered = dijkstraAlgo(pickup_u, delivered_v, vertices)
    reset(vertices)
    delivered_to_end = dijkstraAlgo(end, delivered_v, vertices)
    total_profit = start_to_pickup[0] + pickup_to_delivered[0] + delivered_to_end[0] - delivery_profit
    
    return_path = []
    # start_to_pickup
    reverse_start_to_pickup = list(reversed(start_to_pickup[1]))    # append during backtracking
    for startpickup in range(len(reverse_start_to_pickup)-1):       
        return_path.append(reverse_start_to_pickup[startpickup])

    # pickup_to_delivered
    reverse_pickup_to_delivered = list(reversed(pickup_to_delivered[1]))
    for pickupdeliver in range(len(reverse_pickup_to_delivered)-1):
        return_path.append(reverse_pickup_to_delivered[pickupdeliver])

    # delivered_to_end
    for deliverend in delivered_to_end[1]:
        return_path.append(deliverend)

    output = ""
    yes_pick_up = False         # for start to end that passby pickup vertex (point)
    yes_delivered = False       # for start to end that passby delivery vertex (point)
    better_profit = 0
    for node in start_to_end[1]:
        # start to end path include pickup and delivery vertex 
        if node == pickup_u:
            yes_pick_up = True

        if yes_pick_up == True:
            if node == delivered_v:
                yes_delivered = True
                better_profit = start_to_end[0] - delivery_profit

        if yes_delivered == True:
            # smaller cost after delivery
            if better_profit < start_to_end[0]:
                output = (better_profit, reverse_start_to_end)  
            elif better_profit >= start_to_end[0]:
                output = (start_to_end[0], reverse_start_to_end)

    if yes_pick_up == True and yes_delivered == True:   
        return output
    elif start_to_end[0] < total_profit:     # smaller cost without delivery
        return (start_to_end[0], reverse_start_to_end)
    else:
        return (total_profit, return_path)
                
def dijkstraAlgo(source, destination, vertices):
    ''' To perform Dijkstra Algorithm to get the best path from source to destination.
    :Input: source is the starting vertex, destination is the ending vertex, vertices is the list of vertices in the graph 
    :Output: A tuple with minimum cost and a list of integer that represent the path to travel from source to destination. 
    :Time Complexity: Best and Worst time complexity will be the same which is O (R log(N)), 
                      where R is the number of edges (roads) and N is the number of vertices (cities). 
    :Auxiliary Space Complexity: O (V + N), where  V is the length of finalized_path list and
                                 N is the length of discovering_source_destination list.  
                                 discovering_source_destination list is used to store the discovered vertices. 
                                 finalized_path list is used to store the path to travel from source to destination. 
    :Space Complexity: O (V + 2N) = O (V + N), space complexity is input space + extra space. 
                       Input space is O (N), where N is the length of vertices from the graph.
                       Extra space is O (V + N), where V is the length of finalized_path list
                       and N is the length of discovering_source_destination list. (Explained above)
    :Explanation: Built in heapq is used to create MinHeap. Choose the smallest cost to move (Greedy).
                  More details explanation is commented at the code.
    '''
    discovering_source_destination = []             # convert list into heap
    vertices[source].cost = 0                       # initialize the cost for source
    discovering_source_destination.append([source, vertices[source].cost])      # 2 elements tuple = [node, cost]
    heapq.heapify(discovering_source_destination)   # create minHeap
    finalised_path = []        
    
    while len(discovering_source_destination) > 0:
        u = heapq.heappop(discovering_source_destination)   # serve it = cost is finalised
        vertices[u[0]].visited = True  
        if vertices[u[0]] == vertices[destination]:         # reached destinatino
            finalised_path = backtracking(vertices[source],vertices[u[0]], finalised_path)
            return (vertices[u[0]].cost, finalised_path)
        # edge relaxation
        for edge in vertices[u[0]].edges:                   # check neighbour
            v = edge.v               
            w = edge.w
            if vertices[v].discovered == False:         
                vertices[v].discovered = True   
                vertices[v].cost = vertices[u[0]].cost + w 
                vertices[v].previous = vertices[u[0]]          # for backtracking
                discovering_source_destination.append([v, vertices[v].cost])
                heapq.heapify(discovering_source_destination)    # update the minHeap
            elif vertices[v].visited == False:                   # discovered, adding it to queue
                if vertices[v].cost > vertices[u[0]].cost + w:      # shorter path found, change it
                    vertices[v].cost = vertices[u[0]].cost + w      
                    vertices[v].previous = vertices[u[0]]
                    discovering_source_destination = update_heap(discovering_source_destination, v, vertices)
                    heapq.heapify(discovering_source_destination)
            
def backtracking (initial, exit, best_path):
    ''' To backtrack the path from source to destination.
    :Input: initial is the source, exit is the destination
            best_path is the list of the path to travel from source to destination.       
    :Output: Updated best_path list.
    :Time Complexity: Best and Worst time complexity will be the same which is O (E), 
                      where E is the number of edges to travel from source to destination. 
    :Auxiliary Space Complexity: No extra space is needed for backtracking. 
    :Space Complexity: O (M), space complexity is input space + extra space. 
                       Input space is O (M), where M is the length of best_path 
                       before updating it and no extra space needed. 
    :Explanation: Appending the vertex ID into best_path list by backtracking it.
    '''
    best_path = [exit.id]
    prev = exit
    while best_path[-1] != initial.id:
        prev = prev.previous
        best_path.append(prev.id)
    return best_path

def update_heap(heap, nodeToUpdate, vertexToUpdate):
    ''' Smaller cost is found, update the cost for the particular vertex.
    :Input: heap is the list of discovered vertices, nodeToUpdate is the integer v value, 
            vertexToUpdate is the vertices list.
    :Output: Updated discovered vertices list.
    :Time Complexity: Best and Worst time complexity will be the same which is O (V), 
                      where V is the length of discovered vertices list.  
    :Auxiliary Space Complexity: No extra space is needed for updating cost. 
    :Space Complexity: O (V), space complexity is input space + extra space. 
                       Input space is O (V), where V is the length of discovered vertices 
                       list and no extra space needed. 
    :Explanation: Update the cost of the particular vertex if smaller cost is found.
    '''
    for i in range(len(heap)):
        if heap[i][0] == nodeToUpdate:
            heap[i] = [nodeToUpdate, vertexToUpdate[nodeToUpdate].cost]
    return heap

def reset(node):
    ''' Multiple Dijkstra is used, so reset is required before invoking a new Dijkstra.
    :Input: node is the vertices from the graph.
    :Output: No output required.
    :Time Complexity: Best and Worst time complexity will be the same which is O (V), 
                      where V is the number of vertices of the graph. 
    :Auxiliary Space Complexity: No extra space is needed for initialization. 
    :Space Complexity: O (V), space complexity is input space + extra space. 
                       Input space is O (V), where V is the number of vertices of the graph and no extra space needed. 
    :Explanation: Reset all Boolean for discovered vertices and visited vertices from True to False.
    '''
    for vertex in node:     
        vertex.discovered = False
        vertex.visited = False 

class Vertices:
    ''' This class is used to determine the vertices of the graph.
    '''
    def __init__(self, id):
        ''' Constructor for Vertices class.
        :Input: id is the index of the vertex.
        :Output: No output required.
        :Time Complexity: Best and Worst time complexity will be the same which is O (1). 
                          Normal initialization only. 
        :Auxiliary Space Complexity: No extra space is needed for initialization. 
        :Space Complexity: O (1), space complexity is input space + extra space. 
                           Input space is O (1) and no extra space needed.
        '''
        self.id = id                # index of the vertex
        self.edges = []             # edge list
        self.cost = 0               # cost/distance
        self.discovered = False     # for traversal
        self.visited = False
        self.previous = None        # backtracking

    def add_edges(self, edge):      
        ''' To add the edges for specific vertices.
        :Input: edge is the path that need to be added for the specific vertex.
        :Output: No output required.
        :Time Complexity: Best and Worst time complexity will be the same which is O (1). 
                          Each edge is added in O (1) time. 
        :Auxiliary Space Complexity: No extra space is needed to append element. 
        :Space Complexity: O (1), space complexity is input space + extra space. 
                           Input space is O (1) and no extra space needed. 
        '''
        self.edges.append(edge)

class Edges:
    ''' This class is used to determine the u (start), v (end), w (cost)
    '''
    def __init__(self, u, v, w):
        ''' Consructor of Edges class.
        :Input: u is the starting, v is the ending, w is the weight of the edge.
        :Output: No output required 
        :Time Complexity: Best and Worst time complexity will be the same which is O (1). 
                          Normal initialization only. 
        :Auxiliary Space Complexity: No extra space is needed for initialization. 
        :Space Complexity: O (1), space complexity is input space + extra space. 
                           Input space is O (1) and no extra space needed.
        '''
        self.u = u
        self.v = v
        self.w = w
