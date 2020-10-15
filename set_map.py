import cv2
from aws_text_recognition import total_ocr1
from aws_text_recognition import total_ocr2
from naver_stt import main_stt
import pygame.mixer


class set_node:
    def name(self):
        num = {"LOTTERIA": "n1", "VIPS": "n1", "BEANPOLE": "n2", "adidas": "n2", "LACOSTE": "n3", "STARBUCKS": "n4",
               "BOBBIBROWN": "n4", "ASHLEY": "n5", "ZARA": "n6", "BURBERRY": "n6",
               "SUBWAY": "n7", "A TWOSOME PLACE": "n7", "THOMBROWNE": "n8", "Dior": "n8"}
        bb = {v: k for k, v in num.items()}
        return bb[self]


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


class navi:
    def path(start, fin):
        maze = [[0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 1],
                [0, 1, 1, 1, 0, 1]]
        SMN, FMN = navi.maze_node(start, fin)
        return navi.astar(maze, SMN, FMN)

    def maze_node(start, fin):
        maze_dict = {"n1": (2, 4), "n2": (0, 4), "n3": (1, 3), "n4": (1, 2), "n5": (1, 1), "n6": (0, 0), "n7": (2, 0),
                     "n8": (0, 5)}
        return maze_dict[start], maze_dict[fin]

    def astar(maze, start, end):
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0

        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = []
        closed_list = []

        open_list.append(start_node)
        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node

                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
            children = []

            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1),
                                 (1, 1)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue

                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node, node_position)
                children.append(new_node)
            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                open_list.append(child)


class link:
    def dist(path):
        maze_dict = {"n1": (2, 4), "n2": (0, 4), "n3": (1, 3), "n4": (1, 2), "n5": (1, 1), "n6": (0, 0), "n7": (2, 0),
                     "n8": (0, 5)}
        bb = {v: k for k, v in maze_dict.items()}
        path_node = []
        for i in range(len(path)):
            path_node.append(bb.get(path[i]))
        return path_node

    def direction(path, fin_node, fin):
        direct = {"L13": ["N", 16], "L43": ["E", 15], "L56": ["N", 12],
                  "L31": ["S", 16], "L34": ["W", 15], "L65": ["S", 12],
                  "L23": ["W", 14], "L45": ["W", 7], "L75": ["N", 11],
                  "L32": ["E", 14], "L54": ["E", 7], "L57": ["S", 11],
                  "L28": ["N", 10], "L82": ["S", 10]}

        position = {("n1", "n3"): "L13", ("n4", "n3"): "L43", ("n5", "n6"): "L56",
                    ("n3", "n1"): "L31", ("n3", "n4"): "L34", ("n6", "n5"): "L65",
                    ("n2", "n3"): "L23", ("n4", "n5"): "L45", ("n7", "n5"): "L75",
                    ("n3", "n2"): "L32", ("n5", "n4"): "L54", ("n5", "n7"): "L57",
                    ("n2", "n8"): "L28", ("n8", "n2"): "L82"}

        link_name = []
        for i in range(len(path) - 1):
            link = []
            link.append(path[i])
            link.append(path[i + 1])
            link = tuple(link)
            link_name.append(position[link])

        usernotice = []
        for i in range(len(link_name)):
            usernotice.append(direct[link_name[i]][0])
        next_node = bring.send(usernotice, path)
        continue_dist = []

        for i in range(len(link_name)):
            continue_dist.append(direct[link_name[i]][1])
        continue_index = []
        distance_sum = 0

        for i in range(len(usernotice) - 1):
            if usernotice[i] == usernotice[i + 1]:
                continue_index.append(i)
                continue_index.append(i + 1)
        k = 0

        while k < len(continue_index) - 1:
            if continue_index[k] == continue_index[k + 1]:
                del continue_index[k]
            else:
                k = k + 1

        for i in continue_index:
            distance_sum += direct[link_name[i]][1]
        i = 0
        while i < len(usernotice) - 1:
            if usernotice[i] == usernotice[i + 1]:
                del usernotice[i]
            else:
                i = i + 1

        for i in continue_index:
            continue_dist[i] = distance_sum
        j = 0
        while j < len(continue_dist) - 1:
            if continue_dist[j] == continue_dist[j + 1]:
                del continue_dist[j]
            else:
                j = j + 1
        user = ["N"]
        user.extend(usernotice)
        realnotice = []

        for i in range(len(user) - 1):
            realnotice.append([user[i], user[i + 1]])
        next_name = []

        for i in next_node:
            next_name.append(set_node.name(i))
        next_name.append(set_node.name(fin_node))
        print('경로 안내를 시작합니다.')
        return continue_dist, realnotice, user, next_name, fin

    def notice(continue_dist, realnotice, user, next_name, fin):
        for i in range(len(realnotice)):
            if realnotice[i][0] == realnotice[i][1]:
                realnotice[i][0] == realnotice[i][1]
            else:
                notice_angle = 0
                an_90 = [['N', 'E'], ['W', 'N'], ['E', 'S'], ['S', 'W'], ['E', 'N'], ['N', 'W'], ['S', 'E'], ['W', 'S']]
                if realnotice[i] in an_90:
                    notice_angle = 1
                else:
                    notice_angle = 2
                notice_direction = 0
                direct_r = [['N', 'E'], ['W', 'N'], ['N', 'S'], ['E', 'W'], ['E', 'S'], ['S', 'W']]
                if realnotice[i] in direct_r:
                    notice_direction = 1
                else:
                    notice_direction = 2

                if notice_angle == 1 and notice_direction == 1:
                    print("우회전하세요")
                    pygame.mixer.init()
                    pygame.mixer.pre_init(44100, -16, 2, 512)
                    pygame.mixer.music.load("/home/pi/Downloads/right.mp3")
                    pygame.mixer.music.play()
                    cv2.waitKey(1100)
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                elif notice_angle == 1 and notice_direction == 2:
                    print("좌회전하세요")
                    pygame.mixer.init()
                    pygame.mixer.pre_init(44100, -16, 2, 512)
                    pygame.mixer.music.load("/home/pi/Downloads/left.mp3")
                    pygame.mixer.music.play()
                    cv2.waitKey(1100)
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                elif notice_angle == 2 and notice_direction == 1:
                    print("뒤로 도세요")
                    pygame.mixer.init()
                    pygame.mixer.pre_init(44100, -16, 2, 512)
                    pygame.mixer.music.load("/home/pi/Downloads/back.mp3")
                    pygame.mixer.music.play()
                    cv2.waitKey(1100)
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                else:
                    print("뒤로 도세요")
                    pygame.mixer.init()
                    pygame.mixer.pre_init(44100, -16, 2, 512)
                    pygame.mixer.music.load("/home/pi/Downloads/back.mp3")
                    pygame.mixer.music.play()
                    cv2.waitKey(1100)
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
            print(round(continue_dist[i] / 5) * 5, "미터 앞으로 가세요")
            num = continue_dist[i]
            final_num = round(num / 5) * 5

            if final_num == 5:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/five_m.mp3")
                pygame.mixer.music.play()
            elif final_num == 10:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/ten_m.mp3")
                pygame.mixer.music.play()
            elif final_num == 15:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/fifteen_m.mp3")
                pygame.mixer.music.play()
            elif final_num == 20:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/twenty_m.mp3")
                pygame.mixer.music.play()
            elif final_num == 25:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/twentyfive_m.mp3")
                pygame.mixer.music.play()
            elif final_num == 30:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/thity_m.mp3")
                pygame.mixer.music.play()
            else:
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/thityfive_m.mp3")
                pygame.mixer.music.play()

            start1 = "none"
            start2 = "none"

            while start1 != next_name[i] and start2 != next_name[i]:
                node_info = {"LOTTERIA": "n1", "VIPS": "n1", "BEANPOLE": "n2", "adidas": "n2", "LACOSTE": "n3",
                             "STARBUCKS": "n4", "BOBBIBROWN": "n4", "ASHLEY": "n5", "ZARA": "n6", "BURBERRY": "n6",
                             "SUBWAY": "n7", "A TWOSOME PLACE": "n7", "THOMBROWNE": "n8", "Dior": "n8"}

                prepare_ocr1 = total_ocr1()
                ocr1 = [0]
                for p in range(len(prepare_ocr1)):
                    if prepare_ocr1[p] in node_info:
                        ocr1 = prepare_ocr1[p]

                        print("간판 텍스트 인식 결과:", ocr1)
                prepare_ocr2 = total_ocr2()
                ocr2 = [0]
                for p in range(len(prepare_ocr2)):
                    if prepare_ocr2[p] in node_info:
                        ocr2 = prepare_ocr2[p]

                        print("간판 텍스트 인식 결과:", ocr2)

                while ocr1 == [0] and ocr2 == [0]:
                    prepare_ocr1 = total_ocr1()
                    ocr1 = [0]
                    for p in range(len(prepare_ocr1)):
                        if prepare_ocr1[p] in node_info:
                            ocr1 = prepare_ocr1[p]

                            print("간판 텍스트 인식 결과:", ocr1)
                    prepare_ocr2 = total_ocr2()
                    ocr2 = [0]
                    for p in range(len(prepare_ocr2)):
                        if prepare_ocr2[p] in node_info:
                            ocr2 = prepare_ocr2[p]

                            print("간판 텍스트 인식 결과:", ocr2)
                if ocr1 != [0]:
                    start1 = ocr1
                if ocr2 != [0]:
                    start2 = ocr2

                while start1 not in node_info and start2 not in node_info:
                    while ocr1 == [0] and ocr2 == [0]:
                        prepare_ocr1 = total_ocr1()
                        ocr1 = [0]
                        for p in range(len(prepare_ocr1) - 1):
                            if prepare_ocr1[p] in node_info:
                                ocr1 = prepare_ocr1[p]

                                print("간판 텍스트 인식 결과:", ocr1)
                        prepare_ocr2 = total_ocr2()
                        ocr2 = [0]
                        for p in range(len(prepare_ocr2) - 1):
                            if prepare_ocr2[p] in node_info:
                                ocr2 = prepare_ocr2[p]

                                print("간판 텍스트 인식 결과:", ocr2)

                    prepare_ocr1 = total_ocr1()
                    ocr1 = [0]
                    for p in range(len(prepare_ocr1) - 1):
                        if prepare_ocr1[p] in node_info:
                            ocr1 = prepare_ocr1[p]

                            print("간판 텍스트 인식 결과:", ocr1)
                    prepare_ocr2 = total_ocr2()
                    ocr2 = [0]

                    for p in range(len(prepare_ocr2) - 1):
                        if prepare_ocr2[p] in node_info:
                            ocr2 = prepare_ocr2[p]

                            print("간판 텍스트 인식 결과:", ocr2)
                    if ocr1 != [0] and ocr1 in node_info:
                        start1 = ocr1
                    if ocr2 != [0] and ocr2 in node_info:
                        start2 = ocr2

                    print("start1 =", start1)
                    print('start2 = ', start2)
        print("도착!")
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.music.load("/home/pi/Downloads/arrive.mp3")
        pygame.mixer.music.play()
        cv2.waitKey(500)
        final_position = {"LOTTERIA": "W", "BEANPOLE": "S", "LACOSTE": "N", "STARBUCKS": "N", "ASHLEY": "W", "ZARA": "N"
                          ,"SUBWAY": "E", "THOMBROWNE": "N", "BOBBIBROWN": "S", "VIPS": "E", "adidas": "E",
                          "Dior": "W", "BURBERRY": "E", "A TWOSOME PLACE": "W"}

        compare = []
        compare.append(user[len(user) - 1])
        compare.append(final_position[fin])
        if compare[0] == compare[1]:
            print("정면에 목적지가 있습니다.")
            pygame.mixer.init()
            pygame.mixer.pre_init(44100, -16, 2, 512)
            pygame.mixer.music.load("/home/pi/Downloads/front_destin.mp3")
            pygame.mixer.music.play()
        else:
            notice_direction = 0
            direct_r = [['N', 'E'], ['W', 'N'], ['N', 'S'], ['E', 'W'], ['E', 'S'], ['S', 'W']]
            if compare in direct_r:
                notice_direction = 1
            else:
                notice_direction = 2
            if notice_direction == 1:
                print("우측에 목적지가 있습니다.")
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/right_destin.mp3")
                pygame.mixer.music.play()

            elif notice_direction == 2:
                print("좌측에 목적지가 있습니다.")
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/left_destin.mp3")
                pygame.mixer.music.play()


class bring:
    def main():
        from set_map import link
        node_info = {"LOTTERIA": "n1", "VIPS": "n1", "BEANPOLE": "n2", "adidas": "n2", "LACOSTE": "n3",
                     "STARBUCKS": "n4", "BOBBIBROWN": "n4", "ASHLEY": "n5", "ZARA": "n6", "BURBERRY": "n6",
                     "SUBWAY": "n7", "A TWOSOME PLACE": "n7", "THOMBROWNE": "n8", "Dior": "n8"}
        print("목적지를 말하세요.")

        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.music.load("/home/pi/Downloads/destin.mp3")
        pygame.mixer.music.play()
        text_result = main_stt()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        prepare_ocr1 = total_ocr1()

        ocr1 = [0]
        for p in range(len(prepare_ocr1)):
            if prepare_ocr1[p] in node_info:
                ocr1 = prepare_ocr1[p]
                print('현재 위치는', ocr1, '입니다')

        prepare_ocr2 = total_ocr2()
        ocr2 = [0]

        for p in range(len(prepare_ocr2)):
            if prepare_ocr2[p] in node_info:
                ocr2 = prepare_ocr2[p]
                print('현재 위치는', ocr2, '입니다')

        while ocr1 == [0] and ocr2 == [0]:
            prepare_ocr1 = total_ocr1()
            ocr1 = [0]

            for p in range(len(prepare_ocr1)):
                if prepare_ocr1[p] in node_info:
                    ocr1 = prepare_ocr1[p]
                    print('현재 위치는', ocr1, '입니다')

            prepare_ocr2 = total_ocr2()
            ocr2 = [0]

            for p in range(len(prepare_ocr2)):
                if prepare_ocr2[p] in node_info:
                    ocr2 = prepare_ocr2[p]
                    print('현재 위치는', ocr2, '입니다')

        if ocr1 != [0]:
            start = ocr1
        elif ocr2 != [0]:
            start = ocr2
        while start not in node_info:
            while ocr1 == [0] and ocr2 == [0]:
                prepare_ocr1 = total_ocr1()
                ocr1 = [0]
                for p in range(len(prepare_ocr1)):
                    if prepare_ocr1[p] in node_info:
                        ocr1 = prepare_ocr1[p]
                prepare_ocr2 = total_ocr2()
                ocr2 = [0]

                for p in range(len(prepare_ocr2)):
                    if prepare_ocr2[p] in node_info:
                        ocr2 = prepare_ocr2[p]

            prepare_ocr1 = total_ocr1()
            ocr1 = [0]

            for p in range(len(prepare_ocr1)):
                if prepare_ocr1[p] in node_info:
                    ocr1 = prepare_ocr1[p]
                    print('현재 위치는', ocr1, '입니다')
            prepare_ocr2 = total_ocr2()
            ocr2 = [0]

            for p in range(len(prepare_ocr2)):
                if prepare_ocr2[p] in node_info:
                    ocr2 = prepare_ocr2[p]
                    print('현재 위치는', ocr2, '입니다')

            if ocr1 != [0] and ocr1 in node_info:
                start = ocr1
            elif ocr2 != [0] and ocr2 in node_info:
                start = ocr2
        name = 0
        while name == 0:
            if text_result == "빈폴." or text_result == "빈폴":
                stt_result = "BEANPOLE"
                name = 1
            elif text_result == "라코스테." or text_result == "라코스테":
                stt_result = "LACOSTE"
                name = 1
            elif text_result == "서브웨이." or text_result == "서브웨이":
                stt_result = "SUBWAY"
                name = 1
            elif text_result == "스타벅스." or text_result == "스타벅스":
                stt_result = "STARBUCKS"
                name = 1
            elif text_result == "자라." or text_result == "자라":
                stt_result = "ZARA"
                name = 1
            elif text_result == "롯데리아." or text_result == "롯데리아":
                stt_result = "LOTTERIA"
                name = 1
            elif text_result == "톰브라운." or text_result == "톰브라운":
                stt_result = "THOMBROWNE"
                name = 1
            elif text_result == "빕스." or text_result == "빕스":
                stt_result = "VIPS"
                name = 1
            elif text_result == "아디다스." or text_result == "아디다스":
                stt_result = "adidas"
                name = 1
            elif text_result == "애슐리." or text_result == "애슐리":
                stt_result = "ASHLEY"
                name = 1
            elif text_result == "버버리." or text_result == "버버리":
                stt_result = "BURBERRY"
                name = 1
            elif text_result == "투썸플레이스." or text_result == "투썸플레이스":
                stt_result = "A TWOSOME PLACE"
                name = 1
            elif text_result == "디올." or text_result == "디올":
                stt_result = "Dior"
                name = 1
            elif text_result == "바비브라운." or text_result == "바비브라운":
                stt_result = "BOBBIBROWN"
                name = 1
            else:
                print("다시 목적지를 말하세요.")
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.music.load("/home/pi/Downloads/again_destin.mp3")
                pygame.mixer.music.play()
                text_result = main_stt()
                pygame.mixer.music.stop()
                pygame.mixer.quit()

        strt_node = node_info[start]
        fin = stt_result
        fin_node = node_info[fin]
        path = navi.path(strt_node, fin_node)
        path_node = link.dist(path)

        return path_node, strt_node, fin_node, fin

    def send(usernotice, path):
        arrange_index = []
        next_node = []

        for i in range(len(usernotice) - 1):
            if usernotice[i] != usernotice[i + 1]:
                arrange_index.append(i + 1)

        for i in range(len(arrange_index)):
            next_node.append(path[arrange_index[i]])

        return next_node