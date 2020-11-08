# Nathan Shulkin
# player class


class Player:
    def __init__(self, name, goals, assists, mGoals, mAssists, mAppear, mScore, mPoints):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.GA = goals + assists
        self.mGoals = mGoals
        self.mAssists = mAssists
        self.mGA = mGoals + mAssists
        self.mAppear = mAppear
        self.mScore = mScore
        self.mPoints = mPoints

    def getName(self):
        return self.name

    def getGoals(self):
        return self.goals

    def getAssists(self):
        return self.assists

    def getGA(self):
        return self.GA

    def getMeanG(self):
        return self.mGoals

    def getMeanA(self):
        return self.mAssists

    def getMeanGA(self):
        return self.mGA

    def getMeanApp(self):
        return self.mAppear

    def getMeanScore(self):
        return self.mScore

    def getMeanPoints(self):
        return self.mPoints
