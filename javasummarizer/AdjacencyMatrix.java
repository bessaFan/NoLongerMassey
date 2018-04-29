package javasummarizer;

public class AdjacencyMatrix {

    int N;
    double[] scores;
    double[][] weightMatrix; // [i][j] is the weight from [i] to [j]
    int[] numChildren;
    int[] numParents;
    final static double dampingFactor = 0.85;

    public AdjacencyMatrix(int N) {
        this.N = N;
        scores = new double[N];
        weightMatrix = new double[N][N];
        numChildren = new int[N];
        numParents = new int[N];
    }

    public double update() {
        double[] newScores = new double[N];

        for (int i = 0; i < N; i++) {
            double sum = 0;

            for (int j = 0; j < N; j++) {
                if (isParent(j, i)) {
                    double weightSum = 0;

                    for (int k = 0; k < N; k++) {
                        if (isParent(j, k)) {
                            weightSum += weightMatrix[j][k];
                        }
                    }

                    weightSum = Math.max(weightSum, 1);
                    sum += weightMatrix[j][i] / weightSum * scores[j];
                }
            }

            newScores[i] = (1 - dampingFactor) + dampingFactor * sum;
        }

        double error = 0;
        for (int i = 0; i < N; i++) {
            error += Math.abs(scores[i] - newScores[i]);
        }
        scores = newScores;

        return error;
    }

    public boolean isParent(int parent, int child) {
        if (parent == child) {
            return false;
        }

        return weightMatrix[parent][child] != 0;
    }

    public void printScores() {
        for (int i = 0; i < N; i++) {
            System.out.print(scores[i] + " ");
        }
        System.out.println();
    }
}
