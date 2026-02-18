code = '^^^>v^<<v><vv>><>>><^>><>>v>^v^><>v<^^<vv<v^v^>>^^v^>^<v^<<v<<^^v^<>^^^v<<>v><<^>>^v><v>>vv><>^^vvv^>^v><^<><v>vvv^<>v^><v^><^vv<>^v^v>v>v><^>v^vv>v<<vv<'

def test():
    plusfloor = '^'
    minusfloor = 'v'
    plusroom = '>'
    minusroom = '<'
    
    floorCount = 0
    roomCount = 0
    
    for i in code:
        if i == plusfloor:
            floorCount += 1
        elif i == plusroom:
            roomCount += 1
        elif i == minusfloor:
            floorCount -= 1
        else:
            roomCount -= 1    
    
    return (floorCount, roomCount)

print(test())
