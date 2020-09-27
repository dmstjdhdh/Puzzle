from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("원피스!", "Images/black.png")
scene2 = Scene("원피스 퍼즐게임!", "Images/oneone.jpg")
scene3 = Scene("원피스!", "Images/scene3.png")

onepiece = Object("Images/oneprint.png")
onepiece.locate(scene2, 0, 0)
onepiece.show()
onepiece.setScale(1.9)

playButton = Object("Images/start.png")
playButton.locate(scene2, 590, 70)
playButton.show()

nextButton = Object("images/play.png")
nextButton.locate(scene, 1150, 30)
nextButton.setScale(1.5)
nextButton.show()

nextButton2 = Object("images/play.png")
nextButton2.locate(scene3, 1150, 30)
nextButton2.setScale(1.5)
nextButton2.show()

k=300
def playButton_onMouseAction(x,y,action):
    showMessage("주어진 시간 안에 퍼즐을 맞추세요!")
    global k
    scene.enter()
    timer.set(k)
    timer.start()
playButton.onMouseAction = playButton_onMouseAction


    

timer = Timer(300.)
showTimer(timer)



x1=375
x2=585
x3=795
x4=375
x5=585
x6=795
x7=375
x8=585
y1=485
y2=485
y3=485
y4=275
y5=275
y6=275
y7=65
y8=65
xx=795
yy=65

problem = Object("Images/onepiece.png")
problem.setScale(0.93)
problem.locate(scene, 190, 50)
problem.show()

Image1 = Object("Images/4.png")
Image1.setScale(0.93)
Image1.locate(scene, x1, y1)
Image1.show()

Image2 = Object("Images/6.png")
Image2.setScale(0.93)
Image2.locate(scene, x2, y2)
Image2.show()

Image3 = Object("Images/1.png")
Image3.setScale(0.93)
Image3.locate(scene, x3, y3)
Image3.show()

Image4 = Object("Images/2.png")
Image4.setScale(0.93)
Image4.locate(scene, x4, y4)
Image4.show()

Image5 = Object("Images/8.png")
Image5.setScale(0.93)
Image5.locate(scene, x5, y5)
Image5.show()

Image6 = Object("Images/7.png")
Image6.setScale(0.93)
Image6.locate(scene, x6, y6)
Image6.show()

Image7 = Object("Images/3.png")
Image7.setScale(0.93)
Image7.locate(scene, x7, y7)
Image7.show()

Image8 = Object("Images/5.png")
Image8.setScale(0.93)
Image8.locate(scene, x8, y8)
Image8.show()

Image9 = Object("Images/10.png")
Image9.setScale(0.93)
Image9.locate(scene, xx, yy)
Image9.show()

  

def Image8_onMouseAction(x, y, action):
    global x8
    global xx
    global y8
    global yy
    if action==MouseAction.DRAG_RIGHT and x8+210==xx and y8==yy:
        x8=x8+210
        xx=xx-210
        Image8.locate(scene, x8, y8)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x8-210==xx and y8==yy:
        x8=x8-210
        xx=xx+210
        Image8.locate(scene, x8, y8)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x8==xx and y8+210==yy:
        y8=y8+210
        yy=yy-210
        Image8.locate(scene, x8, y8)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x8==xx and y8-210==yy:
        y8=y8-210
        yy=yy+210
        Image8.locate(scene, x8, y8)
        Image9.locate(scene, xx, yy)
Image8.onMouseAction = Image8_onMouseAction

def Image7_onMouseAction(x, y, action):
    global x7
    global xx
    global y7
    global yy
    if action==MouseAction.DRAG_RIGHT and x7+210==xx and y7==yy:
        x7=x7+210
        xx=xx-210
        Image7.locate(scene, x7, y7)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x7-210==xx and y7==yy:
        x7=x7-210
        xx=xx+210
        Image7.locate(scene, x7, y7)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x7==xx and y7+210==yy:
        y7=y7+210
        yy=yy-210
        Image7.locate(scene, x7, y7)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x7==xx and y7-210==yy:
        y7=y7-210
        yy=yy+210
        Image7.locate(scene, x7, y7)
        Image9.locate(scene, xx, yy)
Image7.onMouseAction = Image7_onMouseAction

def Image6_onMouseAction(x, y, action):
    global x6
    global xx
    global y6
    global yy
    if action==MouseAction.DRAG_RIGHT and x6+210==xx and y6==yy:
        x6=x6+210
        xx=xx-210
        Image6.locate(scene, x6, y6)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x6-210==xx and y6==yy:
        x6=x6-210
        xx=xx+210
        Image6.locate(scene, x6, y6)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x6==xx and y6+210==yy:
        y6=y6+210
        yy=yy-210
        Image6.locate(scene, x6, y6)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x6==xx and y6-210==yy:
        y6=y6-210
        yy=yy+210
        Image6.locate(scene, x6, y6)
        Image9.locate(scene, xx, yy)
Image6.onMouseAction = Image6_onMouseAction

def Image5_onMouseAction(x, y, action):
    global x5
    global xx
    global y5
    global yy
    if action==MouseAction.DRAG_RIGHT and x5+210==xx and y5==yy:
        x5=x5+210
        xx=xx-210
        Image5.locate(scene, x5, y5)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x5-210==xx and y5==yy:
        x5=x5-210
        xx=xx+210
        Image5.locate(scene, x5, y5)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x5==xx and y5+210==yy:
        y5=y5+210
        yy=yy-210
        Image5.locate(scene, x5, y5)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x5==xx and y5-210==yy:
        y5=y5-210
        yy=yy+210
        Image5.locate(scene, x5, y5)
        Image9.locate(scene, xx, yy)
Image5.onMouseAction = Image5_onMouseAction


def Image4_onMouseAction(x, y, action):
    global x4
    global xx
    global y4
    global yy
    if action==MouseAction.DRAG_RIGHT and x4+210==xx and y4==yy:
        x4=x4+210
        xx=xx-210
        Image4.locate(scene, x4, y4)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x4-210==xx and y4==yy:
        x4=x4-210
        xx=xx+210
        Image4.locate(scene, x4, y4)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x4==xx and y4+210==yy:
        y4=y4+210
        yy=yy-210
        Image4.locate(scene, x4, y4)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x4==xx and y4-210==yy:
        y4=y4-210
        yy=yy+210
        Image4.locate(scene, x4, y4)
        Image9.locate(scene, xx, yy)
Image4.onMouseAction = Image4_onMouseAction

def Image3_onMouseAction(x, y, action):
    global x3
    global xx
    global y3
    global yy
    if action==MouseAction.DRAG_RIGHT and x3+210==xx and y3==yy:
        x3=x3+210
        xx=xx-210
        Image3.locate(scene, x3, y3)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x3-210==xx and y3==yy:
        x3=x3-210
        xx=xx+210
        Image3.locate(scene, x3, y3)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x3==xx and y3+210==yy:
        y3=y3+210
        yy=yy-210
        Image3.locate(scene, x3, y3)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x3==xx and y3-210==yy:
        y3=y3-210
        yy=yy+210
        Image3.locate(scene, x3, y3)
        Image9.locate(scene, xx, yy)
Image3.onMouseAction = Image3_onMouseAction

def Image2_onMouseAction(x, y, action):
    global x2
    global xx
    global y2
    global yy
    if action==MouseAction.DRAG_RIGHT and x2+210==xx and y2==yy:
        x2=x2+210
        xx=xx-210
        Image2.locate(scene, x2, y2)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x2-210==xx and y2==yy:
        x2=x2-210
        xx=xx+210
        Image2.locate(scene, x2, y2)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x2==xx and y2+210==yy:
        y2=y2+210
        yy=yy-210
        Image2.locate(scene, x2, y2)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x2==xx and y2-210==yy:
        y2=y2-210
        yy=yy+210
        Image2.locate(scene, x2, y2)
        Image9.locate(scene, xx, yy)
Image2.onMouseAction = Image2_onMouseAction

def Image1_onMouseAction(x, y, action):
    global x1
    global xx
    global y1
    global yy
    if action==MouseAction.DRAG_RIGHT and x1+210==xx and y1==yy:
        x1=x1+210
        xx=xx-210
        Image1.locate(scene, x1, y1)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_LEFT and x1-210==xx and y1==yy:
        x1=x1-210
        xx=xx+210
        Image1.locate(scene, x1, y1)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_UP and x1==xx and y1+210==yy:
        y1=y1+210
        yy=yy-210
        Image1.locate(scene, x1, y1)
        Image9.locate(scene, xx, yy)
    elif action==MouseAction.DRAG_DOWN and x1==xx and y1-210==yy:
        y1=y1-210
        yy=yy+210
        Image1.locate(scene, x1, y1)
        Image9.locate(scene, xx, yy)
Image1.onMouseAction = Image1_onMouseAction


u = 300

def nextButton_onMouseAction(x,y,action):
    if x3==375 and y3==485 and x4==585 and y4==485 and x7==795 and y7==485 and x1==375 and y1==275 and x8==585 and y8==275 and x2==795 and y2==275 and x6==375 and y6==65 and x5==585 and y5==65:
        scene3.enter()
        showMessage((300-k), "초만에 통과했습니다!")
        global u
        timer.set(u)
        timer.start()
    else:
        showMessage("아직 퍼즐이 완성되지 않았어요!")
nextButton.onMouseAction = nextButton_onMouseAction

a1=288
a2=515
a3=742
a4=288
a5=515
a6=742
a7=288
a8=515
b1=472
b2=472
b3=472
b4=245
b5=245
b6=245
b7=18
b8=18
aa=742
bb=18


Image1a = Object("Images/1-4.png")
Image1a.locate(scene3, a1, b1)
Image1a.show()

Image2a = Object("Images/1-6.png")
Image2a.locate(scene3, a2, b2)
Image2a.show()

Image3a = Object("Images/1-1.png")
Image3a.locate(scene3, a3, b3)
Image3a.show()

Image4a = Object("Images/1-2.png")
Image4a.locate(scene3, a4, b4)
Image4a.show()

Image5a = Object("Images/1-8.png")
Image5a.locate(scene3, a5, b5)
Image5a.show()

Image6a = Object("Images/1-7.png")
Image6a.locate(scene3, a6, b6)
Image6a.show()

Image7a = Object("Images/1-3.png")
Image7a.locate(scene3, a7, b7)
Image7a.show()

Image8a = Object("Images/1-5.png")
Image8a.locate(scene3, a8, b8)
Image8a.show()

Image9a = Object("Images/10.png")
Image9a.locate(scene3, aa, bb)
Image9a.show()

def Image8a_onMouseAction(x, y, action):
    global a8
    global aa
    global b8
    global bb
    if action==MouseAction.DRAG_RIGHT and a8+227==aa and b8==bb:
        a8=a8+227
        aa=aa-227
        Image8a.locate(scene3, a8, b8)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a8-227==aa and b8==bb:
        a8=a8-227
        aa=aa+227
        Image8a.locate(scene3, a8, b8)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a8==aa and b8+227==bb:
        b8=b8+227
        bb=bb-227
        Image8a.locate(scene3, a8, b8)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a8==aa and b8-227==bb:
        b8=b8-227
        bb=bb+227
        Image8a.locate(scene3, a8, b8)
        Image9a.locate(scene3, aa, bb)
Image8a.onMouseAction = Image8a_onMouseAction

def Image7a_onMouseAction(x, y, action):
    global a7
    global aa
    global b7
    global bb
    if action==MouseAction.DRAG_RIGHT and a7+227==aa and b7==bb:
        a7=a7+227
        aa=aa-227
        Image7a.locate(scene3, a7, b7)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a7-227==aa and b7==bb:
        a7=a7-227
        aa=aa+227
        Image7a.locate(scene3, a7, b7)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a7==aa and b7+227==bb:
        b7=b7+227
        bb=bb-227
        Image7a.locate(scene3, a7, b7)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a7==aa and b7-227==bb:
        b7=b7-227
        bb=bb+227
        Image7a.locate(scene3, a7, b7)
        Image9a.locate(scene3, aa, bb)
Image7a.onMouseAction = Image7a_onMouseAction

def Image6a_onMouseAction(x, y, action):
    global a6
    global aa
    global b6
    global bb
    if action==MouseAction.DRAG_RIGHT and a6+227==aa and b6==bb:
        a6=a6+227
        aa=aa-227
        Image6a.locate(scene3, a6, b6)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a6-227==aa and b6==bb:
        a6=a6-227
        aa=aa+227
        Image6a.locate(scene3, a6, b6)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a6==aa and b6+227==bb:
        b6=b6+227
        bb=bb-227
        Image6a.locate(scene3, a6, b6)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a6==aa and b6-227==bb:
        b6=b6-227
        bb=bb+227
        Image6a.locate(scene3, a6, b6)
        Image9a.locate(scene3, aa, bb)
Image6a.onMouseAction = Image6a_onMouseAction

def Image5a_onMouseAction(x, y, action):
    global a5
    global aa
    global b5
    global bb
    if action==MouseAction.DRAG_RIGHT and a5+227==aa and b5==bb:
        a5=a5+227
        aa=aa-227
        Image5a.locate(scene3, a5, b5)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a5-227==aa and b5==bb:
        a5=a5-227
        aa=aa+227
        Image5a.locate(scene3, a5, b5)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a5==aa and b5+227==bb:
        b5=b5+227
        bb=bb-227
        Image5a.locate(scene3, a5, b5)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a5==aa and b5-227==bb:
        b5=b5-227
        bb=bb+227
        Image5a.locate(scene3, a5, b5)
        Image9a.locate(scene3, aa, bb)
Image5a.onMouseAction = Image5a_onMouseAction

def Image4a_onMouseAction(x, y, action):
    global a4
    global aa
    global b4
    global bb
    if action==MouseAction.DRAG_RIGHT and a4+227==aa and b4==bb:
        a4=a4+227
        aa=aa-227
        Image4a.locate(scene3, a4, b4)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a4-227==aa and b4==bb:
        a4=a4-227
        aa=aa+227
        Image4a.locate(scene3, a4, b4)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a4==aa and b4+227==bb:
        b4=b4+227
        bb=bb-227
        Image4a.locate(scene3, a4, b4)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a4==aa and b4-227==bb:
        b4=b4-227
        bb=bb+227
        Image4a.locate(scene3, a4, b4)
        Image9a.locate(scene3, aa, bb)
Image4a.onMouseAction = Image4a_onMouseAction

def Image3a_onMouseAction(x, y, action):
    global a3
    global aa
    global b3
    global bb
    if action==MouseAction.DRAG_RIGHT and a3+227==aa and b3==bb:
        a3=a3+227
        aa=aa-227
        Image3a.locate(scene3, a3, b3)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a3-227==aa and b3==bb:
        a3=a3-227
        aa=aa+227
        Image3a.locate(scene3, a3, b3)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a3==aa and b3+227==bb:
        b3=b3+227
        bb=bb-227
        Image3a.locate(scene3, a3, b3)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a3==aa and b3-227==bb:
        b3=b3-227
        bb=bb+227
        Image3a.locate(scene3, a3, b3)
        Image9a.locate(scene3, aa, bb)
Image3a.onMouseAction = Image3a_onMouseAction

def Image2a_onMouseAction(x, y, action):
    global a2
    global aa
    global b2
    global bb
    if action==MouseAction.DRAG_RIGHT and a2+227==aa and b2==bb:
        a2=a2+227
        aa=aa-227
        Image2a.locate(scene3, a2, b2)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a2-227==aa and b2==bb:
        a2=a2-227
        aa=aa+227
        Image2a.locate(scene3, a2, b2)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a2==aa and b2+227==bb:
        b2=b2+227
        bb=bb-227
        Image2a.locate(scene3, a2, b2)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a2==aa and b2-227==bb:
        b2=b2-227
        bb=bb+227
        Image3a.locate(scene3, a2, b2)
        Image9a.locate(scene3, aa, bb)
Image2a.onMouseAction = Image2a_onMouseAction

def Image1a_onMouseAction(x, y, action):
    global a1
    global aa
    global b1
    global bb
    if action==MouseAction.DRAG_RIGHT and a1+227==aa and b1==bb:
        a1=a1+227
        aa=aa-227
        Image1a.locate(scene3, a1, b1)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_LEFT and a1-227==aa and b1==bb:
        a1=a1-227
        aa=aa+227
        Image1a.locate(scene3, a1, b1)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_UP and a1==aa and b1+227==bb:
        b1=b1+227
        bb=bb-227
        Image1a.locate(scene3, a1, b1)
        Image9a.locate(scene3, aa, bb)
    elif action==MouseAction.DRAG_DOWN and a1==aa and b1-227==bb:
        b1=b1-227
        bb=bb+227
        Image1a.locate(scene3, a1, b1)
        Image9a.locate(scene3, aa, bb)
Image1a.onMouseAction = Image1a_onMouseAction

def nextButton2_onMouseAction(x,y,action):
    if a3==288 and b3==472 and a4==515 and a4==472 and a7==742 and b7==472 and a1==585 and b1==245 and a8==515 and b8==245 and a2==742 and b2==245 and a6==288 and b6==18 and a5==515 and b5==18:
        showMessage((300-k), "초만에 통과했습니다!")
    else:
        showMessage("아직 퍼즐이 완성되지 않았어요!")
nextButton2.onMouseAction = nextButton2_onMouseAction



startGame(scene2)
