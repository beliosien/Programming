/* *****************************************************************************
 *  Name:
 *  Date: 2020-07-13
 *  Description: Implementation of my own generic deque queue
 **************************************************************************** */

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private int size;
    private Node first;
    private Node last;

    private class Node {
        private Item item;
        private Node next;

        // construct a node
        Node(Item item) {
            this.item = item;
            this.next = null;
        }

        // return the item of the node
        public Item getItem() {
            return this.item;
        }

        // return the next node
        public Node getNext() {
            return next;
        }

        // set the next node
        public void setNext(Node next) {
            this.next = next;
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
            if (this.last == null) {
                this.last = new Node(item);
            }
            else {
                Node temp = first;
                this.last = new Node(item);
                while (temp.getNext() != null) {
                    temp = temp.getNext();
                }
                temp.setNext(this.last);
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
            if (this.first == null) {
                this.first = new Node(item);
            }
            else {
                Node temp = first;
                this.first = new Node(item);
                this.first.setNext(temp);
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
            Item item = this.last.getItem();
            Node temp = first;
            while (!temp.getNext().equals(last)) {
                temp = temp.getNext();
            }
            last = temp;
            last.setNext(null);
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
            Item item = first.getItem();
            first = first.getNext();
            this.size--;
            return item;
        }
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            if (this.current != null) {
                Item item = this.current.getItem();
                this.current = this.current.getNext();
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

    // unit testing (required)
    public static void main(String[] args) {
        Deque<Integer> deque = new Deque<Integer>();
        deque.addFirst(1);
        deque.addLast(2);
        deque.addFirst(5);
        deque.addLast(4);
        deque.addFirst(6);
        deque.addFirst(7);
        deque.addLast(10);
        for (int i : deque) {
            System.out.print(i + " ");
        }
        System.out.println();
        deque.removeLast();
        deque.removeLast();
        deque.removeFirst();
        deque.removeFirst();
        for (int i : deque) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

}
