Settings.MoveMouseDelay = 0.4
Settings.MinSimilarity = 0.8
Settings.AutoWaitTimeout = 20
Env.addHotkey(Key.F1, KeyModifier.ALT, exit)

mission = Region(906,72,182,27)
ship = Region(904,133,108,29)
controls = Region(476,557,837,30)

mission.setAutoWaitTimeout(0)
ship.setAutoWaitTimeout(0)

def canPull():
    return controls.findBest("request.png", "complete.png")

def turnIn():
    if controls.exists("complete.png", 0):
        controls.click()        

# ask for a mission, wait until offer is loaded
def request():
    controls.wait("request.png")
    controls.click()
    controls.wait("accept.png")

# controls should always have decline as last match here
def decline():
    controls.click("decline.png")

# take a mission, then close the window
def accept():
    controls.wait("accept.png")
    controls.click()
    controls.wait("complete.png")
    controls.click("close.png")

def goodBurner():
    return ship.findBest("hawk.png", "enyo.png")

def isTeam():
    return mission.exists("team.png")

def procureTeam():
    while True:
        request()
        if isTeam():
            if goodBurner():
                accept()
                wait(1)
                break
        decline()

while canPull():
    turnIn()
    procureTeam()