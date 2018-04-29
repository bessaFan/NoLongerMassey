import math
from Main import run

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
    common = ["the", "in", "on", "was", "a", "an", "are", "of", "to", "at", "and", "for", "there", "from", "it",
              "these", "that", "by", "is", "has"]
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
        for j in range(i + 1, D):
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
    raw_text = run('dog')
    print(raw_text + '\n\n')
    s = summarize(raw_text)
    for i in range(len(s)):
        print(s[i])


main()
