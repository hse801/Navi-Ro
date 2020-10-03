from __future__ import print_function


def main():
    from set_map import bring, link

    path, strt, fin_node, fin = bring.main()

    #link = link.direction(path)
    continue_dist, realnotice, user, next_name, fin = link.direction(path, fin_node, fin)

    link.notice(continue_dist, realnotice, user, next_name,fin)
    #print("link =", link)