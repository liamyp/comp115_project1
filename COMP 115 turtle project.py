import turtle
import math
Screen = turtle.Screen()
james = turtle.Turtle()
james.speed(10)
lastEnd = []
northPoint = -1000, 0
eastPoint = 500, 0
centerPoint = -60, 0
SEPoint = 4550, 0
turtle.tracer(4, 0)
def toPoint(dist, dir, start, up=False, slope = 0,  interStart = None, interEnd = None):
    if up:
        james.penup()
    if dir == northPoint:
        dist = -dist
    spot = dir
    point = (spot[0], slope)
    x1, y1 = start
    james.teleport(x1, y1, fill_gap=False)
    if interStart != None and interEnd != None:
        x2,y2 = interStart
        x3,y3 = interEnd
        xP, yP = point
        slope1 = (y1 - yP)/(x1 - xP)
        slope2 = (y2 - y3)/(x2 - x3)
        xEnd = (slope1 * x1 - slope2 * x2 + y2 - y1) / (slope1 - slope2)
        yEnd = (slope1 * slope2 * (x1 - x2) + y2 * slope1 - y1 * slope2) / (slope1 - slope2)
        james.goto(xEnd, yEnd)
    else:
        hyp = dist / math.cos(math.radians(james.towards(point)))
        james.setheading(james.towards(point))
        james.forward(hyp)
    james.pendown()
    return james.pos()
def line(start, end, up = False, interStart = None, interEnd = None):
    if up:
        james.penup()
    x1,y1 = start
    x2,y2 = end
    james.teleport(x1,y1,fill_gap=False)
    if interStart != None and interEnd != None:
            xA,yA = interStart
            xB, yB = interEnd
            slope2 = (yA - yB)/(xA - xB)
            if x1!=x2:
                slope1 = (y1 - y2)/(x1 - x2)
                xEnd = (slope1 * x1 - slope2 * xA + yA - y1) / (slope1 - slope2)
                yEnd = (slope1 * slope2 * (x1 - xA) + yA * slope1 - y1 * slope2) / (slope1 - slope2)
                james.goto(xEnd, yEnd)
            else:
                yEnd = slope2 * (x1 - xB) + yB
                james.goto(x1, yEnd)

    else:
        james.goto(x2,y2)
    james.pendown()
    return james.pos()

#Drawing the closer building
baseA = []
doorA = []
deckA = []
buildA = [baseA, doorA, deckA]
buildA[0].append(toPoint(-220, northPoint, (0, -150), True)) #baseA 0
buildA[0].append(toPoint(-100, northPoint, baseA[0], True)) #baseA 1
buildA[0].append(line(baseA[0], (baseA[0]) + (0, 230))) #baseA 2
buildA[0].append(line(baseA[2], (baseA[2]) + (0, 250), True)) #baseA 3
buildA[0].append(line(baseA[3], (baseA[3]) + (0, 20))) #baseA 4
buildA[0].append(toPoint(-200, northPoint, baseA[4])) #baseA 5
buildA[0].append(toPoint(-200, northPoint, baseA[3])) #baseA 6
buildA[0].append(toPoint(-200, northPoint, baseA[2])) #baseA 7
#start drawing the closer building door
buildA[1].append(line(baseA[1], (baseA[1]) + (0, 20), True)) #doorA 0
buildA[1].append(line(doorA[0], (doorA[0] + (0,100)), False)) #doorA 1
james.seth(james.towards(northPoint))
james.right(90)
james.circle(-50,180)
buildA[1].append(james.pos) #doorA 2
buildA[1].append(toPoint(15, eastPoint, doorA[0], False)) #doorA 3
buildA[1].append(toPoint(15, eastPoint, doorA[1], True)) #doorA 4
line(doorA[3], doorA[4])
james.seth(james.towards(northPoint))
james.right(90)
james.circle(-45,60)
buildA[1].append(toPoint(-20, eastPoint, doorA[0], False)) #doorA 5
buildA[1].append(toPoint(-20, eastPoint, baseA[1], True)) #doorA 6
buildA[1].append(toPoint(1, northPoint, doorA[0], False, -400, baseA[1], northPoint)) #doorA 7
buildA[1].append(toPoint(-1, eastPoint, doorA[7], False, 0, doorA[6], northPoint)) #doorA 8
line(doorA[8], doorA[5])
line(doorA[6], doorA[8])
toPoint(-100, northPoint, doorA[5])
toPoint(-100, northPoint, doorA[6])
toPoint(-100, northPoint, doorA[3])
line(baseA[0], doorA[7])
#start drawing the closer building balcony
buildA[2].append(toPoint(100, eastPoint, baseA[3])) #deckA 0
buildA[2].append(toPoint(100, eastPoint, baseA[2], True)) #deckA 1
buildA[2].append(toPoint(-5, northPoint, deckA[0], True)) #deckA 2
#drawing the balcony part fo the balcony
buildA[2].append(toPoint(-97, eastPoint, deckA[2] + (0, -((deckA[0][1] - deckA[1][1])/2) - 4))) #deckA 3
buildA[2].append(line(deckA[3], deckA[3] + (0, 8))) #deckA 4
toPoint(-200, northPoint, deckA[3])
toPoint(-200, northPoint, deckA[4])
#the walls behind the balcony
line(deckA[0], deckA[0]+(0,-1),False,deckA[4],northPoint)
line(james.pos(), james.pos()+(0,-1),True,deckA[3],eastPoint)
line(james.pos(), james.pos()+(0,-1),False,baseA[2],baseA[7])
toPoint(-110, northPoint, baseA[3], True)
buildA[2].append(toPoint(25, eastPoint, james.pos(), True)) #deckA 5
toPoint(1, northPoint, deckA[5], True, 0, deckA[2], eastPoint)
buildA[2].append(line(james.pos(), james.pos() + (0, -1), True, deckA[3], eastPoint)) #deckA 6
buildA[2].append(toPoint(deckA[5][0] - deckA[6][0], northPoint, james.pos(), True)) #deckA 7
buildA[2].append(line(deckA[5], deckA[5] +(0, -1), False, deckA[4], northPoint)) #deckA 8
buildA[2].append(line(deckA[8], deckA[8] +(0, -1), True, deckA[7], northPoint)) #deckA 9
buildA[2].append(line(deckA[9], deckA[9] +(0, -1), False, baseA[2], northPoint)) #deckA 10
#balcony pillar support
buildA[2].append(toPoint(-9, northPoint, deckA[0], True)) #deckA 11
buildA[2].append(toPoint(-90, eastPoint, deckA[11], True)) #deckA 12
buildA[2].append(toPoint(-14, northPoint, deckA[12], False)) #deckA 13
buildA[2].append(toPoint(10, eastPoint, deckA[13], False)) #deckA 14
buildA[2].append(toPoint(-90, eastPoint, deckA[11] + (0, -((deckA[0][1] - deckA[1][1])/2) - 4), True)) #deck 15
buildA[2].append(toPoint(-14, northPoint, deckA[15], False)) #deckA 16
buildA[2].append(toPoint(10, eastPoint, deckA[16], False)) #deckA 17
for i in range(3):
    buildA[2].append(line(deckA[12 + i], deckA[12 + i] + (0, -1), False, deckA[4], northPoint)) #deck 18-20
    line(james.pos(), deckA[15+i], True)
    buildA[2].append(line(deckA[15 + i], deckA[15 + i] + (0, -1), False, baseA[2], northPoint)) #deck 21-23
#filling in the gaps in the balcony
toPoint(-100, northPoint, deckA[9])
toPoint(-100, northPoint, deckA[5])
toPoint(deckA[0][0]-deckA[5][0], northPoint, deckA[0])
toPoint(deckA[2][0]-deckA[5][0], northPoint, deckA[2] + (0, -((deckA[0][1] - deckA[1][1])/2) - 4))

#drawing the further block
def center(pos1, pos2, pos3, pos4, pos5 = None, pos6 = None):
    line(pos1,pos4,True,pos2,pos3)
    if pos5 != None:
        line(james.pos(), james.pos() +(0, 1), True, pos5, pos6)
    return james.pos()

def scale(pos, point, side = None):
    d = math.dist(pos, point)
    dX = abs(pos[0] - point[0])
    s = d/abs(point[0])
    sX = dX/abs(point[0])
    if side == 'x':
        return sX
    elif side == 'y':
        return s
    return s, sX

def pillar(pos, side, Epos1, Epos2,centered = False, posSide = False):
    if side == eastPoint:
        otSide = northPoint
    else:
        otSide = eastPoint
    pillar = []
    if centered:
        pillar.append(toPoint(-5 * scale(pos, side, 'x'), side, pos, True))#0
    elif posSide:
        pillar.append(toPoint(-10 * scale(pos, side, 'x'), side, pos, True))#0
    else:
        pillar.append(pos)#0
    pillar.append(line(pillar[0], pillar[0] - (0, 80 * scale(pillar[0], side, 'y')))) #1
    pillar.append(toPoint(-5 * scale(pillar[0], side, 'x'), otSide, pillar[0], True)) #2
    pillar.append(line(pillar[2] + (0, -20 * scale(pillar[2], side, 'y')), pillar[2] + (0, 20 * scale(pillar[2], side, 'y')))) #3
    pillar.append(toPoint(8 * scale(pillar[3], side, 'x'), otSide, pillar[3])) #4
    line(pillar[4], pillar[4] + (0, -1), False, Epos1, Epos2)
    pillar.append(toPoint(10 * scale(pillar[3], side, 'x'), side, pillar[3])) #5
    pillar.append(line(pillar[5], pillar[5] + (0, -35 * scale(pillar[5], side, 'y')))) #6
    pillar.append(toPoint(-10 * scale(pillar[6], side, 'x'), side, pillar[6])) #7
    pillar.append(toPoint(9 * scale(pillar[1], side, 'x'), side, pillar[1])) #8
    pillar.append(toPoint((5 * scale(pillar[0], side, 'x')), side, pillar[0], True)) #9
    pillar.append(toPoint((5 * scale(pillar[1], side, 'x')), side, pillar[1], True)) #10
    line(pillar[7], pillar[1])
    line(pillar[6], pillar[8])
    pillarB.append(pillar)

def window(pos1, pos2, side, a = 1):
    if side == eastPoint:
        otSide = northPoint
    else:
        otSide = eastPoint
    window = [pos1 + (a * -24 * scale(pos1, side, 'x'), 0), pos2 + (a * 27 * scale(pos2, side, 'x'), 0)]
    window.append(line(window[0], window[0] + (0, -50 * scale(window[0], side, 'y')), True))
    window.append(toPoint(abs(window[1][0] - window[0][0]), side, window[2]))
    window.append(line(window[2], window[2] - (0, 60 * scale(window[2], side, 'y'))))
    window.append(toPoint(abs(window[1][0] - window[0][0]), side, window[4]))
    window.append(toPoint(5 * scale(window[3], side, 'x'), otSide, window[3]))
    window.append(toPoint(-abs(window[0][0] - window[6][0]), side, window[6]))
    line(window[6], window[6] - (0, 1), False, window[5], side)
    line(window[3], window[5])
    # window.append(toPoint(5 * scale(window[3], northPoint)))
    windowB.append(window)

doorB1 = []
signB = []
windowB = []
pillarB = []
baseB = []
buildB = [baseB, pillarB, windowB, signB, doorB1]
buildB[0].append(toPoint(50, eastPoint, (0, 200), True)) #0
buildB[0].append(toPoint(50, eastPoint, (0, -150), True)) #1
buildB[0].append(toPoint(150, eastPoint, baseB[0], False)) #2
buildB[0].append(toPoint(150, eastPoint, baseB[1], False)) #3
james.goto(baseB[2])
buildB[0].append(toPoint(75, northPoint, (0, 200),True)) #4
buildB[0].append(toPoint(75, northPoint, (0, -150), True)) #5
buildB[0].append(toPoint(400, northPoint, baseB[4], False)) #6
buildB[0].append(toPoint(400, northPoint, baseB[5], False)) #7
james.goto(baseB[6])
line(baseB[0], baseB[4])
line(baseB[1], baseB[5])
line(baseB[0], baseB[1])
line(baseB[4],baseB[5])
#drawing the pillars
pillar(baseB[0], eastPoint, baseB[0], baseB[4]) #pillarB 0
pillar(baseB[2], eastPoint, baseB[0], baseB[2],False, True) #pillarB 1
buildB[1].append(center(baseB[0], baseB[1], baseB[2], baseB[3], baseB[0], baseB[2])) #pillarB 2
pillar(pillarB[2], eastPoint, baseB[0], baseB[2], True) #pillarB 3
pillar(baseB[4], northPoint, baseB[4], baseB[6]) #pillarB 4
pillar(baseB[6], northPoint, baseB[4], baseB[6], False, True) #pillarB 5
buildB[1].append(center(baseB[4], baseB[5], baseB[6], baseB[7], baseB[4], baseB[6])) #pillarB 6
pillar(pillarB[6], northPoint, baseB[4], baseB[6], True)  #pillar 7
buildB[1].append(center(pillarB[4][9], pillarB[4][10], pillarB[7][9], pillarB[7][10], baseB[4], baseB[6])) #pillar 8
pillar(pillarB[8], northPoint, baseB[4], baseB[6], True) #pillar 9
buildB[1].append(center(pillarB[5][9], pillarB[5][10], pillarB[7][9], pillarB[7][10], baseB[4], baseB[6])) #pillar 10
pillar(pillarB[10], northPoint, baseB[4], baseB[6], True) #pillar 11
#drawing the upper windows
window(pillarB[4][9], pillarB[9][9], northPoint)
window(pillarB[9][9], pillarB[7][9], northPoint)
window(pillarB[7][9], pillarB[11][9], northPoint)
window(pillarB[11][9], pillarB[5][9], northPoint)
window(pillarB[0][9], pillarB[3][9], eastPoint, -1)
window(pillarB[3][9], pillarB[1][9], eastPoint, -1)
#drawing the signs
buildB[3].append(baseB[5] + (0, 190)) #signB 0
buildB[3].append(toPoint(1, SEPoint, signB[0], True, 0, baseB[0], baseB[1])) #1
buildB[3].append(toPoint(3, centerPoint, signB[1])) #2
buildB[3].append(toPoint(-1, SEPoint, signB[2], False, 0, signB[0], centerPoint)) #3
line(signB[3],signB[0])
buildB[3].append(toPoint(abs(baseB[2][0] - signB[1][0]), eastPoint, signB[1], True))#4
buildB[3].append(toPoint(abs(signB[0][0] - baseB[6][0]), northPoint, signB[0], True)) #5
buildB[3].append(toPoint(1, northPoint, signB[3], False, 0, centerPoint, signB[5])) #6
buildB[3].append(toPoint(1, eastPoint, signB[2], False, 0, centerPoint, signB[4])) #7
buildB[3].append(line(signB[4], signB[4]+(0,-27), True)) #8
buildB[3].append(toPoint(-abs(signB[1][0]-signB[8][0]), eastPoint, signB[8])) #9
buildB[3].append(toPoint(-abs(signB[9][0]-signB[0][0]), SEPoint, signB[9])) #10
buildB[3].append(toPoint(abs(signB[10][0]-signB[5][0]), northPoint, signB[10])) #11
buildB[3].append(line(signB[7], signB[7]+(0,-1), False, centerPoint, signB[8])) #12
buildB[3].append(line(signB[6], signB[6]+(0,-1), False, centerPoint, signB[11])) #13
buildB[3].append(toPoint(-1, eastPoint, signB[12], False, 0, centerPoint, signB[9])) #14
buildB[3].append(toPoint(-1, northPoint, signB[13], False, 0, centerPoint, signB[10])) #15
line(signB[14], signB[15])
#building the center door
buildB[4].append(toPoint(34, SEPoint, baseB[5], True)) #0
buildB[4].append(line(doorB1[0], doorB1[0] + (0, 110))) #1
buildB[4].append(toPoint(60, SEPoint, doorB1[1])) #2
buildB[4].append(line(doorB1[2], doorB1[2] - (0, 1), False, SEPoint, baseB[5])) #3
buildB[4].append(toPoint(-3, centerPoint, doorB1[3])) #4
buildB[4].append(line(doorB1[4], doorB1[4] + (0, 1), False, doorB1[1], doorB1[2])) #5
buildB[4].append(toPoint(doorB1[0][0]-doorB1[4][0], SEPoint, doorB1[4])) #6

james.teleport(0, 0, fill_gap=False)
Screen.mainloop()