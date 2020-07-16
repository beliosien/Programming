/**
 * @author Ossim Belias
 * 
 * @brief Implementation of my own generic  doubly LinkedList in C++
 *
*/
#pragma once

#include "Node.h"

template <typename T>
class LinkedList
{   
private:
    Node<T>* head_;
    Node<T>* tail_;
    int size_;
public:
    // constructor
    LinkedList();
    // destructor
    ~LinkedList();

    // add element at the front
    void addFirst(T& item);
    // add element at the back;
    void addLast(T& item);
    // remove element at the front 
    T& removeFirst();
    // remove element at the end
    T& removeLast();
    // return the size 
    int size();
    // check if the doubly linked list is empty
    bool isEmpty();
};





