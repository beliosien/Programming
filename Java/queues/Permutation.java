/* *****************************************************************************
 *  Name: Ossim Belias
 *  Date: 2020-07-14
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.In;

public class Permutation {
    public static void main(String[] args) {
        RandomizedQueue<String> randomizedQueue = new RandomizedQueue<String>();
        In in = new In(args[0]);
        int n = Integer.parseInt(args[1]);
        String[] word = in.readLine().split(" ");
        String[] arr = new String[word.length];

        for (int i = 0; i < word.length; i++) {
            randomizedQueue.enqueue(word[i]);
        }

        for (int i = 0; i < n; i++) {
            String sample = randomizedQueue.sample();
            System.out.println(sample);
        }
    }
}
