package javasummarizer;

import java.util.ArrayList;
import java.util.List;

public class Sentence {

    String sentence;
    List<String> words;
    final static String[] common = new String[]{"the", "in", "on", "was", "a", "an", "are", "of", "to", "at", "and", "for", "there", "from", "it", "these", "that", "by", "is", "has"};

    public Sentence(String sentence) {
        this.sentence = sentence;

        String[] chunks = sentence.toLowerCase().split(" ");

        words = new ArrayList(chunks.length);
        for (int i = 0; i < chunks.length; i++) {
            words.add(chunks[i]);
        }

        List<String> toRemove = new ArrayList<>();
        for (String i : words) {
            if (i.length() == 0) {
                toRemove.add(i);
            }
        }
        words.removeAll(toRemove);

        removePeriods();
        removeString(";");
        removeString("?");
        removeString("!");
        removeString(",");
        removeString("\"");
    }

    public void removeString(String remove) {
        for (String i : words) {
            i.replace(remove, "");
        }
    }

    public void removePeriods() {
        for (String i : words) {
            if (i.charAt(i.length() - 1) == '.') {
                i.substring(0, i.length() - 1);
            }
        }
    }

    public static double similarity(Sentence a, Sentence b) { // Where magic happens
        int intersections = 0;

        for (String i : a.words) {
            for (String j : b.words) {
                if (isCommon(i) || isCommon(j)) continue;

                if (i.equals(j)) {
                    intersections++;
                }
            }
        }

        return (double) intersections / (Math.max(1, Math.log(a.words.size())) + Math.max(1, Math.log(b.words.size())));
    }

    public static boolean isCommon(String s) {
        for (int i = 0; i < common.length; i++) {
            if (s.equals(common[i])) {
                return true;
            }
        }

        return false;
    }
}
