#include "Node.h"

template<typename T>
Node<T>::Node(T item) : item_(item), next_(nullptr), prev_(nullptr)
{
}

template<typename T>
T Node<T>::getItem()
{
    return item_;
}

template<typename T>
Node<T>* Node<T>::getNext()
{
    return next_;
}

template<typename T>
Node<T>* Node<T>::getPrev()
{
    return prev_;
}

template<typename T>
void Node<T>::setNext(Node* next)
{
    this->next_ = next;
}

template<typename T>
void Node<T>::setPrevious(Node* prev)
{
    this->prev_ = prev;
}

template<typename T>
Node<T>::~Node()
{
}