# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import re

def solution(N, S, T):
    ships = []
    list_S = re.findall('([0-9]+)([A-Z]) ([0-9]+)([A-Z])',S)
    list_T = re.findall('([0-9]+)([A-Z])',T)

    for s_tuple in list_S:
        tiles = (abs(int(s_tuple[2]) - int(s_tuple[0]))+1) * (abs(ord(s_tuple[3]) - ord(s_tuple[1]))+1)
        max_disp = max(abs(int(s_tuple[2]) - int(s_tuple[0]))+1,(abs(ord(s_tuple[3]) - ord(s_tuple[1]))+1))
        ships.append([s_tuple,tiles,tiles,max_disp])

    for h_tuple in list_T:
        for ship in ships:
            if (check_hit(ship, h_tuple)):
                ship[1] -= 1
                break
    sunked = 0
    hits = 0
    for ship in ships:
        if (ship[1] == 0):
            sunked +=1
        elif (ship[1] < ship[2]):
            hits += 1
    return str(sunked) + "," + str(hits)

def check_hit(ship, hit):
    return max(abs(int(ship[0][0]) - int(hit[0])) + abs(int(ship[0][2]) - int(hit[0])),
                abs(ord(ship[0][1]) - ord(hit[1])) + abs(ord(ship[0][3]) - ord(hit[1]))) < ship[3]


print(solution(12, '1B 4D', '1A'))

print(solution(4, '1B 2C,2D 4D', '2B 2D 3D 4D 4A'))
print(solution(12, '1A 2A,12A 12A', '12A'))
print(solution(3, '1A 1B,2C 2C', '1B'))
