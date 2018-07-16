import unittest
def bfs_get_path(graph, start_pointart_node, end_node):
    start_point = graph.setdefault(start_pointart_node, None)
    end_point = graph.setdefault(end_node, None)
    if(start_point == None or end_point == None):
        raise Exception
    marked = []
    dictionary = {}
    list_queue = []
    flag = False
    list_queue.append(start_pointart_node)
    while(len(list_queue)>0 and flag == False):
        node = list_queue.pop(0)
        if(node not in marked):
            marked.append(node)
            temp = graph[node]
            for x in temp:
                if (x!=end_node and x not in marked):
                    dictionary[x]=node
                    list_queue.append(x)
                elif(x==end_node):
                    list_queue.append(x)
                    dictionary[x]=node
                    flag = True
                    break
    val = dictionary.setdefault(end_node,None)
    
    if (val == None):
        return None
    else:
        temp = []
        current = end_node
        while(current != start_pointart_node):
            temp.append(current)
            current = dictionary[current]
        temp.append(current)
        temp.reverse()
        return temp
 
# Testart_points

class Testart_point(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def testart_point_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expectend_point = ['a', 'c', 'e']
        self.assertEqual(actual, expectend_point)

    def testart_point_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expectend_point = ['d', 'a', 'c']
        self.assertEqual(actual, expectend_point)

    def testart_point_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expectend_point = ['a', 'c']
        self.assertEqual(actual, expectend_point)

    def testart_point_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expectend_point = ['f', 'g']
        self.assertEqual(actual, expectend_point)

    def testart_point_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expectend_point = ['g', 'f']
        self.assertEqual(actual, expectend_point)

    def testart_point_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expectend_point = ['a']
        self.assertEqual(actual, expectend_point)

    def testart_point_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expectend_point = None
        self.assertEqual(actual, expectend_point)

    def testart_point_start_pointart_node_not_ptempent(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def testart_point_end_node_not_ptempent(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)