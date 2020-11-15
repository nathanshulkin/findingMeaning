# Nathan Shulkin
# player class


class Player:
    def __init__(self, name, goals, assists, mGA, mAppear, mScore, mPoints, ptDiff):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.GA = goals + assists
        self.mGA = mGA
        self.mAppear = mAppear
        self.mScore = mScore
        self.mPoints = mPoints
        self.ptDiff = ptDiff

    def getName(self):
        return self.name

    def getGoals(self):
        return self.goals

    def getAssists(self):
        return self.assists

    def getGA(self):
        return self.GA

    def getMeanGA(self):
        return self.mGA

    def getMeanApp(self):
        return self.mAppear

    def getMeanScore(self):
        return self.mScore

    def getMeanPoints(self):
        return self.mPoints

    def getPointDiff(self):
        return self.ptDiff
