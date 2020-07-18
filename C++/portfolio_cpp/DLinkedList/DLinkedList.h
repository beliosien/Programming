/**
 * @author Ossim Belias
 *
 * @brief Implementation of my own generic  doubly LinkedList in C++
 *
*/

#pragma once
#ifndef DLINKEDLIST_H
#define DLINKEDLIST_H
#include "Node.cpp"
#include <string>

template <typename T>
class DLinkedList
{
private:
    Node<T>* head_;
    Node<T>* tail_;
    int size_;
public:
    // constructor
    DLinkedList();
    // destructor
    ~DLinkedList();

    // add element at the front
    void addFirst(T item);
    // add element at the back;
    void addLast(T item);
    // remove element at the front 
    T removeFirst();
    // remove element at the end
    T removeLast();
    // return the size 
    int size();
    // check if the doubly linked list is empty
    bool isEmpty();
    // return the head of the doubly linked list
    Node<T>* getHead();
    // return the tail of the doubly linked list
    Node<T>* getTail();
    // clear the doubly linkedList 
    void clear();
    // remove a give from the doubly linked list
    void remove(T item);
   
};
#endif // !LINKEDLIST_H

