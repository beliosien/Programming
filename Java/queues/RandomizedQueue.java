/* *****************************************************************************
 *  Name: Ossim Belias
 *  Date: 2020-07-14
 *  Description: Creation of my own Randomized queue
 *  A randomized queue is like a stack or queue except that the item removed
 * is chosen uniformly at random among items in the data structure.
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private static final int INIT_SIZE = 1;
    private Item[] queue;
    private int size;

    private class ReverseArrayIterator implements Iterator<Item> {
        private int i = size;
        private Item[] shuffleQueue = queue.clone();

        ReverseArrayIterator() {
            StdRandom.shuffle(shuffleQueue);
        }

        public boolean hasNext() {
            return i > 0;
        }

        public Item next() {
            if (i == 0) {
                throw new NoSuchElementException();
            }
            else {
                int index = StdRandom.uniform(shuffleQueue.length);
                Item item = shuffleQueue[index];
                while (item == null) {
                    index = StdRandom.uniform(shuffleQueue.length);
                    item = shuffleQueue[index];
                }
                shuffleQueue[index] = null;
                i--;
                return item;
            }
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    // construct an empty randomized queue
    public RandomizedQueue() {
        this.queue = (Item[]) new Object[INIT_SIZE];
        this.size = 0;
    }

    // double the size of the array
    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        int pos = capacity - 1;
        for (int i = this.queue.length - 1; i >= 0; i--) {
            if (queue[i] != null) {
                copy[pos] = queue[i];
                pos--;
            }
        }
        queue = copy;
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return this.size == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        for (Item item : this) {
            if (item != null) {
                this.size++;
            }
        }
        return this.size;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        else {
            if (queue.length == size) {
                this.resize(2 * this.size);
            }
            for (int i = this.queue.length - 1; i >= 0; i--) {
                if (queue[i] == null) {
                    queue[i] = item;
                    this.size++;
                    break;
                }
            }
        }
    }

    // remove and return a random item
    public Item dequeue() {
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        else {
            int pos = this.queue.length - 1;
            Item item = queue[pos];
            while (item == null) {
                pos--;
                item = queue[pos];
            }
            queue[pos] = null;
            this.size--;
            if (this.size > 0 && this.size == queue.length / 4) {
                this.resize(queue.length / 2);
            }
            return item;
        }
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        else {
            int index = StdRandom.uniform(this.queue.length);
            Item item = queue[index];
            while (item == null) {
                index = StdRandom.uniform(this.queue.length);
                item = queue[index];
            }
            return item;
        }
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new ReverseArrayIterator();
    }

    // unit testing (required)
    public static void main(String[] args) {
        int n = 5;
        RandomizedQueue<Integer> queue = new RandomizedQueue<Integer>();
        System.out.println(queue.isEmpty());
        for (int i = 0; i < n; i++)
            queue.enqueue(i);
        for (int a : queue) {
            for (int b : queue)
                StdOut.print(a + "-" + b + " ");
            StdOut.println();
        }
        System.out.println(queue.isEmpty());
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        queue.enqueue(36);
    }
}
