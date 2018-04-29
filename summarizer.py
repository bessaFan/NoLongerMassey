import math

N = 5
d = 0.85

class sentence:
    def __init__(self, sentence):
        self.sentence = sentence

        new = sentence.lower().split(" ")
        for i in range(len(new)):
            if new[i] == '':
                new[i] = None

        self.words = []
        for i in range(len(new)):
            if new[i] is not None:
                self.words.append(new[i])

        self.removePeriods()
        self.removeString("!")
        self.removeString("?")
        self.removeString("!")
        self.removeString(",")
        self.removeString("\"")
        self.removeString("-")

    def removeString(self, string):
        for i in range(len(self.words)):
            self.words[i] = self.words[i].replace(string, "")

    def removePeriods(self):
        for i in range(len(self.words)):
            if self.words[i][len(self.words[i]) - 1] == ".":
                self.words[i] = self.words[i][:len(self.words[i]) - 1]

def similarity(a, b):
    intersections = 0

    for i in range(len(a.words)):
        for j in range(len(b.words)):
            if isCommon(a.words[i]) or isCommon(b.words[j]):
                continue

            if a.words[i] == b.words[j]:
                intersections += 1

    return intersections / (math.log(len(a.words)) + math.log(len(b.words)))

def isCommon(s):
    common = ["the", "in", "on", "was", "a", "an", "are", "of", "to", "at", "and", "for", "there", "from", "it", "these", "that", "by", "is", "has"]
    return s in common;


class matrix:
    def __init__(self, N):
        self.N = N
        self.scores = [0 for x in range(N)]
        self.weightMatrix = [[0 for x in range(N)] for y in range(N)]

    def update(self):
        new = [[0 for x in range(self.N)] for y in range(self.N)]

        for i in range(self.N):
            sum = 0
            for j in range(self.N):
                if self.isParent(j, i):
                    weightSum = 0

                    for k in range(self.N):
                        if self.isParent(j, k):
                            weightSum += self.weightMatrix[j][k]

                    weightSum = max(weightSum, 1)
                    sum += self.weightMatrix[j][i] / weightSum * self.scores[j]
            new[i] = (1 - d) + d * sum

        self.scores = new


    def isParent(self, i, j):
        if i == j:
            return False

        return self.weightMatrix[i][j] != 0

def summarize(paragraph):
    sentences = paragraph.split(".")

    for i in range(len(sentences)):
        if sentences[i] == "":
            sentences.pop(i)
            i -= 1

    for i in range(len(sentences)):
        sentences[i] += "."

    D = len(sentences)

    for i in range(D):
        sentences[i] = sentence(sentences[i])

    graph = matrix(D)

    weights = [[0 for x in range(D)] for y in range(D)]

    for i in range(D - 1):
        for j in range(i+1, D):
            weights[i][j] = similarity(sentences[i], sentences[j])
            weights[j][i] = weights[i][j]

    graph.weightMatrix = weights

    for _ in range(100):
        graph.update()

    scores = []

    for i in range(D):
        scores.append(graph.scores[i])

    scores.sort()
    scores = scores[::-1]

    summary = []
    for j in range(D):
        for i in range(N):
            if graph.scores[j] == scores[i]:
                summary.append(sentences[j].sentence)
                break

    return summary

def main():
    s = summarize("In 1996, treasure hunter Brock Lovett and his team aboard the research vessel Keldysh search the wreck of RMS Titanic for a necklace with a rare diamond, the Heart of the Ocean. They recover a safe containing a drawing of a young woman wearing only the necklace. It is dated April 14, 1912, the day the ship struck the iceberg. Rose Dawson Calvert, claiming to be the person in the drawing, visits Lovett and tells of her experiences aboard the ship. In 1912 Southampton, 17-year-old first-class passenger Rose DeWitt Bukater, her fiancé Cal Hockley, and her mother Ruth board the Titanic. Ruth emphasizes that Rose's marriage will resolve the DeWitt Bukaters' financial problems. Distraught over the engagement, Rose considers committing suicide by jumping from the stern; Jack Dawson, a penniless artist, convinces her not to. Discovered with Jack, Rose tells Cal that she was peering over the edge and Jack saved her from falling. Cal is indifferent, but when Rose indicates some recognition is due, he offers Jack a small amount of money. After Rose asks whether saving her life meant so little, he invites Jack to dine with them in first class the following night. Jack and Rose develop a tentative friendship, though Cal and Ruth are wary of him. Following dinner, Rose secretly joins Jack at a party in third class. Aware of Cal and Ruth's disapproval, Rose rebuffs Jack's advances, but later realizes that she prefers him over Cal. After rendezvousing on the bow at sunset, Rose takes Jack to her state room and displays Cal's engagement present: the Heart of the Ocean. At her request, Jack sketches Rose posing nude wearing it. They evade Cal's bodyguard and have sex in an automobile inside the cargo hold. They later visit the forward deck, witnessing a collision with an iceberg and overhearing the officers and designer discussing its seriousness. Cal discovers Jack's sketch of Rose and a mocking note from her in his safe along with the necklace. When Jack and Rose attempt to tell Cal of the collision, he has his butler slip the necklace into Jack's pocket and accuses him of theft. He is arrested, taken to the Master-at-arms' office, and handcuffed to a pipe. Cal puts the necklace in his own coat pocket. With the ship sinking, Rose is desperate to free Jack. She flees Cal and her mother, who has boarded a lifeboat, and rescues him. They return to the boat deck, where Cal and Jack encourage her to board a lifeboat; Cal claims he can get himself and Jack off safely. After Rose boards one, Cal tells Jack the arrangement is only for himself. As her boat lowers, Rose decides that she cannot leave Jack and jumps back on board. Cal takes his butler's pistol and chases Rose and Jack into the flooding first class dining saloon. After using up his ammunition, Cal realizes he gave his coat and consequently the necklace to Rose. He later boards a collapsible lifeboat by carrying a lost child. After braving several obstacles, Jack and Rose return to the boat deck. All the lifeboats have departed and passengers are falling to their deaths as the stern rises out of the water. The ship breaks in half, lifting the stern into the air. Jack and Rose ride it into the ocean and he helps her onto a wooden panel only buoyant enough for one person. Holding the edge, he assures her that she will die an old woman, warm in her bed. He dies of hypothermia but she is saved. With Rose hiding from Cal en route, the RMS Carpathia takes the survivors to New York. There she gives her name as Rose Dawson. She later learns that Cal committed suicide after losing everything in the 1929 Wall Street Crash. Lovett abandons his search after hearing Rose's story. Alone on the stern of the Keldysh, Rose takes out the Heart of the Oceanin her possession all alongand drops it into the sea over the wreck site. While she is seemingly asleep in her bed, photos on her dresser depict a life of freedom and adventure, partly inspired by Jack. A young Rose reunites with him at the ship's Grand Staircase, applauded by those who perished.")
    for i in range(len(s)):
        print(s[i])

main()

