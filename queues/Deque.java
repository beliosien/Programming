/* *****************************************************************************
 *  Name: Ossim Belias
 *  Date: 2020-07-13
 *  Description: Implementation of my own generic deque queue
 * A double-ended queue or deque (pronounced “deck”) is a generalization of a stack and a queue
 * that supports adding and removing items from either the front or the back of the data structure.
 **************************************************************************** */

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private int size;
    private Node first;
    private Node last;

    private class Node {
        private final Item item;
        private Node next;
        private Node previous;

        // construct a node
        Node(Item item) {
            this.item = item;
            this.next = null;
            this.previous = null;
        }

        // return the item of the node
        public Item getItem() {
            return this.item;
        }

        // return the next node
        public Node getNext() {
            return next;
        }

        // return the previous
        public Node getPrevious() {
            return previous;
        }

        // set the next node
        public void setNext(Node next) {
            this.next = next;
        }

        // set the previous node
        public void setPrevious(Node previous) {
            this.previous = previous;
        }
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            if (this.current != null) {
                Item item = this.current.getItem();
                this.current = this.current.getPrevious();
                return item;
            }
            else {
                throw new NoSuchElementException();
            }
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    // construct an empty deque
    public Deque() {
        this.size = 0;
        this.first = null;
        this.last = null;
    }

    // is the deque empty?
    public boolean isEmpty() {
        return this.size == 0;
    }

    // return the number of items on the deque
    public int size() {
        return this.size;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        else {
            if (this.isEmpty()) {
                this.first = new Node(item);
                this.last = this.first;
            }
            else {
                Node temp = new Node(item);
                this.first.setNext(temp);
                temp.setPrevious(first);
                this.first = temp;
            }
            this.size++;
        }
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        else {
            if (this.isEmpty()) {
                this.last = new Node(item);
                this.first = this.last;
            }
            else {
                Node temp = last;
                this.last = new Node(item);
                temp.setPrevious(last);
                this.last.setNext(temp);
            }
            this.size++;
        }
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        else {
            Item item = this.first.getItem();
            if (this.size == 1) {
                this.last = null;
                this.first = null;
            }
            else {
                this.first.getPrevious().setNext(null);
                first = first.getPrevious();
                first.setNext(null);
            }

            this.size--;
            return item;
        }
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (this.isEmpty()) {
            throw new NoSuchElementException();
        }
        else {
            Item item = last.getItem();
            if (this.size == 1) {
                this.first = null;
                this.last = null;
            }
            else {
                last = last.getNext();
                last.setPrevious(null);
            }
            this.size--;
            return item;
        }
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new ListIterator();
    }


    // unit testing (required)
    public static void main(String[] args) {
        int n = 10;
        Deque<Integer> deque = new Deque<Integer>();
        for (int i = 0; i < n; i++) {
            deque.addFirst(i + 1);
        }
        for (int i : deque) {
            System.out.println(i);
        }

    }
}
