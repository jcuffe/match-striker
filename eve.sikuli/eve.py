Settings.MoveMouseDelay = 0.3
Settings.MinSimilarity = 0.8
Settings.AutoWaitTimeout = 0

def canPull():
    return findBest("request.png", "complete.png", "decline.png")

def prepare():
    click(findBest("complete.png", "decline.png"))

# ask for a mission, wait until offer is loaded
def request():
    wait("request.png", 20)
    click()
    wait("location.png", 20)

# controls should always have decline as last match here
def decline():
    wait("decline.png", 20)
    click()

# take a mission, then close the window
def accept():
    wait("accept.png", 20)
    click()
    wait("close.png", 20)
    click()

def goodBurner():
    return findBest("hawk.png", "enyo.png")

def isTeam():
    return exists("team.png")

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
    prepare()
    procureTeam()