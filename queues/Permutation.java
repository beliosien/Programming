/* *****************************************************************************
 *  Name: Ossim Belias
 *  Date: 2020-07-14
 *  Description:
Permutation client. Write a client program Permutation.java that
* takes a command-line integer k; reads in a sequence of strings from standard input using StdIn.readString();
* and prints exactly k of them, uniformly at random. Print each item from the sequence at most once. You may assume that 0 ≤ k ≤ n, where n is the number of string on standard input.
Sample:
---
% more distinct.txt
A B C D E F G H I
% java Permutation 3 < distinct.txt
C
G
A
---
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;

public class Permutation {

    public static void main(String[] args) {
        RandomizedQueue<String> randomizedQueue = new RandomizedQueue<String>();
        int n = Integer.parseInt(args[0]);
        while (!StdIn.isEmpty()) {
            String word = StdIn.readString();
            randomizedQueue.enqueue(word);
        }
        for (int i = 0; i < n; i++) {
            System.out.println(randomizedQueue.dequeue());
        }
    }
}
