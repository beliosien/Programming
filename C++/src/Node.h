/**
 * @author Ossim Belias
 * 
 * @brief implementation of the generic node class in order to support the 
 *      doubly linked list
 * 
*/

#pragma once

template<typename T>
class Node
{
private:
    T item_;
    Node* next_;
    Node* prev_;
        
public:
    // constructor
    Node(T& item);
    // destructor
    ~Node();
    
    // return the next node 
    Node* getNext();
    // return the previous node
    Node* getPrevious();
    // return the item
    T& getItem();
    // set the next node
    void setNext(Node& next);
    // set the previous node
    void setPrevious(Node& previous);
};
