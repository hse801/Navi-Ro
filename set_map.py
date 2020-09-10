import math
import cv2
#from navi_ocr_stt import stt_result
from aws_tts import tts
class set_node:
    def name(self):
        num = {"LOTTERIA":"n1", "BEANPOLE":"n2","LACOSTE":"n3","STARBUCKS":"n4","IKEA":"n5","ZARA":"n6","SUBWAY":"n7","TOMBROWN":"n8"}
        return num[self]

class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class navi:

    def path(start,fin):
        maze = [[0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 1],
                [0, 1, 1, 1, 0, 1]]
        SMN,FMN = navi.maze_node(start, fin)

        return navi.astar(maze, SMN,FMN)

    #없애도 됨
    def maze_node(start,fin):
        # maze = [[0, 1, 1, 1, 0, 0],
        #         [1, 0, 0, 0, 1, 1],
        #         [0, 1, 1, 1, 0, 1]]

        maze_dict = {"n1":(2,4),"n2":(0,4),"n3":(1,3),"n4":(1,2),"n5":(1,1),"n6":(0,0),"n7":(2,0),"n8":(0,5)}
        #bb = {v: k for k, v in maze_dict.items()}

        return maze_dict[start], maze_dict[fin]


    def astar(maze, start, end):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""

        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path

            # Generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1),
                                 (1, 1)]:  # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                            (child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

class link:
    #경로 노드에 해당하는 좌표값을 구해서 노드 사이의 거리들 따로 계산 ? 아니면 총 거리로 계산하는게 나은가?
    # def locat(self):
    #     f_node = {v: k for k, v in navi.maze_node.maze_dict.items()}
    #     f_node.get(self)
    #
    #     num2 = {"n1":[30,-5],"n2":[50,10],"n3":[30,10],"n4":[10,10],"n5":[0,10],"n6":[0,17],"n7":[0,0]}
    #
    #     return num2[self]

    def dist(path):
        sum = 0
        maze_dict = {"n1": (2, 4), "n2": (0, 4), "n3": (1, 3), "n4": (1, 2), "n5": (1, 1), "n6": (0, 0), "n7": (2, 0),"n8":(0,5)}
        bb = {v: k for k, v in maze_dict.items()}
        path_node = []

        for i in range(len(path)):
            path_node.append(bb.get(path[i]))

        #print("path_node =", path_node)

        num2 = {"n1": [22,0], "n2": [36,15], "n3": [22,15], "n4": [7,15], "n5": [0,15], "n6": [0,27],
                "n7": [0, 4],"n8":[36,25]}
        locat = []
        for i in range(len(path_node)):
            locat.append(num2[path_node[i]])

        print("locat =", locat)

        sum = []
        for i in range(len(locat)-1):
            sum.append(int(math.sqrt((locat[i][0] - locat[i+1][0])**2 +(locat[i][1]-locat[i+1][1])**2)))

        return sum, path_node


    def direction(path):

        direct = {"L13": ["N", 15], "L43": ["E", 15], "L56": ["N", 12],
                  "L31": ["S", 15], "L34": ["W", 15], "L65": ["S", 12],
                  "L23": ["W", 14], "L45": ["W", 7], "L75": ["N", 11],
                  "L32": ["E", 14], "L54": ["E", 7], "L57": ["S", 11],
                  "L28": ["N",10],"L82":["S",10]}

        # position = {"L13": ["n1", "n3"], "L43": ["n4", "n3"], "L56": ["n5", "n6"],
        #             "L31": ["n3", "n1"], "L34": ["n3", "n4"], "L65": ["n6", "n5"],
        #             "L23": ["n2", "n3"], "L45": ["n4", "n5"], "L75": ["n7", "n5"],
        #             "L32": ["n3", "n2"], "L54": ["n5", "n4"], "L57": ["n5", "n7"]}

        position = {("n1", "n3"): "L13", ("n4", "n3"): "L43", ("n5", "n6"): "L56",
                    ("n3", "n1"): "L31", ("n3", "n4"): "L34", ("n6", "n5"): "L65",
                    ("n2", "n3"): "L23", ("n4", "n5"): "L45", ("n7", "n5"): "L75",
                    ("n3", "n2"): "L32", ("n5", "n4"): "L54", ("n5", "n7"): "L57",
                    ("n2","n8"):"L28", ("n8","n2"):"L82"}

        #bb2 = {v: k for k, v in direct.items()}

        link_name = []
        for i in range(len(path)-1):
            link = []
            link.append(path[i])
            link.append(path[i+1])

            link = tuple(link)

            link_name.append(position[link])
        print("Link_name =",link_name)

        usernotice = []

        for i in range(len(link_name)):
            usernotice.append(direct[link_name[i]][0])

        print("usernotice", usernotice)


        continue_dist = []
        for i in range(len(link_name)):
            continue_dist.append(direct[link_name[i]][1])
        print("continue_dist =",continue_dist)

        continue_index = []
        distance_sum = 0
        for i in range(len(usernotice)-1):
            if usernotice[i] == usernotice[i + 1]:
                continue_index.append(i)
                continue_index.append(i+1)


                #distance_sum += direct[link_name[i]][1]
        k = 0
        while k < len(continue_index) - 1:
            if continue_index[k] == continue_index[k + 1]:
                del continue_index[k]
            else:
                k = k + 1

        print("continue_index =",continue_index)

        for i in continue_index:
            distance_sum += direct[link_name[continue_index[i]]][1]
        #연속되는 realnotice 값 1개로 처리
        i = 0
        while i < len(usernotice) - 1:
            if usernotice[i] == usernotice[i + 1]:
                del usernotice[i]
            else:
                i = i + 1
        print("usernotice =",usernotice)

        for i in continue_index:
            continue_dist[i] = distance_sum

        j = 0
        while j < len(continue_dist) - 1:
            if continue_dist[j] == continue_dist[j + 1]:
                del continue_dist[j]
            else:
                j = j + 1
        print("continue_dist =",continue_dist)

        realnotice = []

        for i in range(len(usernotice) - 1):
            realnotice.append([usernotice[i], usernotice[i + 1]])

        print("realnotice =", realnotice)

        # 0번째 안내
        if realnotice[0][0] == "E":
            print("우회전하세요")
            text = "우회전하세요"
            tts(text)

        elif realnotice[0][0] == "S":
            print("뒤로 도세요")
            text = "뒤로 도세요"
            tts(text)

        elif realnotice[0][0] == "W":
            print("좌회전하세요")
            text = "좌회전하세요"
            tts(text)

        elif realnotice[0][0] == "N":
            print("직진하세요")
            text = "직진하세요"
            tts(text)

        cv2.waitKey(1500)

        ##첫번째부터 안내 시작

        # notice_angle_1 = "90도"
        # notice_angle_2 = "180도"
        #
        # notice_direction_1 = "오른쪽으로 도세요"
        # notice_direction_2 = "왼쪽으로 도세요"


        for i in range(len(realnotice)):
            # print(realnotice[i])
            # 거리
            # notice_dist = []
            # notice_dist.append(direct[link_name[i]][1])
            print(continue_dist[i], "미터 앞으로 가세요")
            num = continue_dist[i]
            text = str(num) + "미터 앞으로 가세요"
            tts(text)
            # cv2.waitKey(300)
            # text = "미터 앞으로 가세요"
            # tts(text)
            cv2.waitKey(1500)

            if realnotice[i][0] == realnotice[i][1]:
                print("계속 같은 방향입니다")
                text = "계속 같은 방향입니다"
                tts(text)

            else:
                # 각도
                notice_angle = 0
                an_90 = [['N', 'E'], ['W', 'N'], ['E', 'S'], ['S', 'W'], ['E', 'N'], ['N', 'W'], ['S', 'E'], ['W', 'S']]
                if realnotice[i] in an_90:
                    notice_angle = 1  # 90
                else:
                    notice_angle = 2

                # 방향

                notice_direction = 0
                direct_r = [['N', 'E'], ['W', 'N'], ['N', 'S'], ['E', 'W'], ['E', 'S'], ['S', 'W']]
                if realnotice[i] in direct_r:
                    notice_direction = 1  # 오른쪽
                else:
                    notice_direction = 2
                # print("notice_direction =", notice_direction)

                if notice_angle == 1 and notice_direction == 1:
                    print("우회전하세요")
                    text = "우회전하세요"
                    tts(text)
                elif notice_angle == 1 and notice_direction == 2:
                    print("좌회전하세요")
                    text = "좌회전하세요"
                    tts(text)
                elif notice_angle == 2 and notice_direction == 1:
                    print("뒤로 도세요")
                    text = "뒤로 도세요"
                    tts(text)
                else:
                    print("뒤로 도세요")
                    text= "뒤로 도세요"
                    tts(text)

            cv2.waitKey(1500)

        x = len(link_name)
        print(continue_dist[len(continue_dist)-1], "미터 앞으로 가세요")
        num = continue_dist[len(continue_dist)-1]
        text = str(num) + "미터 앞으로 가세요"
        # tts(text)
        # cv2.waitKey(300)
        # text = "미터 앞으로 가세요"
        tts(text)
        cv2.waitKey(1500)
        # f ocr1 == stt_result or ocr2 == stt_result:i
        # while True:
        #     final1 = total_ocr1()
        #     final2 = total_ocr2()
        #     if final1 == stt_result:
        #         print("오른쪽에 목적지가 있습니다")
        #         break
        #     elif final2 == stt_result:
        #         print("왼쪽에 목적지가 있습니다")
        #         break
        print("도착!")
        text = "도착"
        tts(text)
        return link_name