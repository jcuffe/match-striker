Settings.MinSimilarity = 0.8
Env.addHotkey(Key.F1, KeyModifier.ALT, quit)

mission = Region(906,72,182,27)
ship = Region(904,133,108,29)
controls = Region(476,557,837,30)

def quit():
    exit()

def canPull():
    return controls.exists("accept.png") or controls.exists("complete.png")

def turnIn():
    if exists("complete.png"):
        click("complete.png")
        wait("request.png", 20)

def decline():
    click("decline.png")
    wait("request.png", 20)
    click("request.png")
    wait("accept.png", 20)

def accept():
    click("accept.png")
    wait("complete.png", 20)
    click("close.png")

def goodBurner():
    return ship.exists("hawk.png", 0) or ship.exists("enyo.png", 0)

def isTeam():
    return mission.exists("team.png", 0)

def procureTeam():
    while not controls.exists("complete.png"):
        if isTeam():
            if goodBurner():
                accept()
            else:
                decline()
        elif exists("decline.png"):
            decline()        

while canPull():
    turnIn()
    procureTeam()