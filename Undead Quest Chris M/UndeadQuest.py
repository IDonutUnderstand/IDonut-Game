#eRushed Inc.
#Undead Quest 
#Chris, Gio
#

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"Undead Quest")
bk = Image("start.png",game)
bk.resizeTo(game.width, game.height)
time = 0
title=Image("title.png",game)
title.resizeBy(-50)
start=Image("startlogo.png",game)
start.resizeBy(-30)
start.moveTo(150,500)
story=Image("story.png",game)
story.resizeBy(-30)
story.moveTo(650,500)
scroll = Image("scroll.png",game)
scroll.resizeTo(game.width,game.height)
skeletonidle = Animation("skeletonidle.png",11,game,264/11,32)
skeletonidle.resizeBy(900)
skeletonidle.moveTo(200,375)
skeletonattack = Animation("skeletonattack.png",18,game,774/18,37)
skeletonattack.moveTo(225,355)
skeletonattack.resizeBy(900)
skeletonattack.playAnim=False
skeletonattack.loop = False
enemy1 = Animation ("enemy.png",15,game,1000/4,1212/4)
enemy1.moveTo(650,400)
attack = 0
time2 = randint(60,120)
#Title Screen - Game Loop

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    title.draw()
    start.draw()
    story.draw()
    if story.collidedWith(mouse):
        scroll.draw()
    if mouse.LeftClick and start.collidedWith(mouse):
        game.over = True
    game.update(30)

game.over = False
#Level 1 - game loop
while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    enemy1.draw()
    game.drawText("Health: " +str(enemy1.health),650,550)
    
    if mouse.LeftClick and time <= 0:
        time = 30
        attack = 1
    if mouse.RightClick:
        game.over=False
    if enemy1.health <= 0:
        game.over=True
    if time ==18:
        enemy1.health-=4
    if time <=11:
        skeletonidle.draw()

    if time >=12:
        skeletonattack.playAnim=True
        skeletonattack.draw()
    time2 -= 1
    time -= 1
    game.update(20)

game.quit()
