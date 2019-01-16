Settings.MinSimilarity = 0.8
Env.addHotkey(Key.F1, KeyModifier.ALT, quit)

mission = Region(906,72,182,27)
ship = Region(904,133,108,29)
controls = Region(476,557,837,30)

def quit():
    exit()

def canPull():
    return controls.exists("request.png") or controls.exists("complete.png")

def turnIn():
    if exists("complete.png"):
        click("complete.png")        

def request():
    wait("request.png", 20)
    click("request.png")
    wait("accept.png", 20)

def decline():
    click("decline.png")

def accept():
    click("accept.png")
    wait("complete.png", 20)
    click("close.png")

def goodBurner():
    return ship.exists("hawk.png") or ship.exists("enyo.png")

def isTeam():
    return mission.exists("team.png")

def procureTeam():
    while True:
        request()
        if isTeam():
            if goodBurner():
                accept()
                break
        decline()

while canPull():
    turnIn()
    procureTeam()