package javasummarizer;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

    final static int N = 5; // Number of sentences in summary

    public static void main(String[] args) {
        String s = readTextFile("String.txt");
        String[] w = s.split("\\."); // issue: a.m. not handled correctly
        for (int i = 0; i < w.length; i++) {
            w[i] += ".";
        }

        Sentence[] sentences = new Sentence[w.length];

        for (int i = 0; i < w.length; i++) {
            sentences[i] = new Sentence(w[i]);
        }

        AdjacencyMatrix mat = new AdjacencyMatrix(sentences.length);

        double[][] weights = new double[sentences.length][sentences.length];

        for (int i = 0; i < weights.length - 1; i++) {
            for (int j = i + 1; j < weights.length; j++) {
                weights[i][j] = Sentence.similarity(sentences[i], sentences[j]);
                weights[j][i] = weights[i][j];
            }
        }

        mat.weightMatrix = weights;

        double error = -1;
        for (int i = 0; i < 100; i++) {
            error = mat.update();
        }

        System.out.println("Error: " + error);

        for (int i = 0; i < mat.N; i++) {
            System.out.println(mat.scores[i] + " " + sentences[i].sentence);
        }

        //Order the scores from greatest to least
        ArrayList<Double> scores = new ArrayList();

        for (int i = 0; i < mat.N; i++) {
            scores.add(mat.scores[i]);
        }

        Collections.sort(scores);
        Collections.reverse(scores);

        System.out.println("\nOrdered List");
        for (int i = 0; i < mat.N; i++) {
            System.out.println(scores.get(i));
        }

        System.out.println("\nSummary");

        for (int j = 0; j < mat.N; j++) {
            for (int i = 0; i < N; i++) {
                if (mat.scores[j] == scores.get(i)) {
                    System.out.println(sentences[j].sentence);
                    break;
                }
            }
        }
    }

    // for testing
    public static String readTextFile(String path) {
        BufferedReader in;
        try {
            in = new BufferedReader(new FileReader(new File(path)));

            String s = "";
            String add;

            while ((add = in.readLine()) != null) {
                s += add;
            }
            in.close();
            return s;
        } catch (Exception e) {
            return null;
        }
    }
}
