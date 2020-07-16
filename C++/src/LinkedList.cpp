#include "LinkedList.h"

template<typename T>
LinkedList<T>::LinkedList(): head_(nullptr), tail_(nullptr)
{
}

template<typename T>
LinkedList<T>::~LinkedList()
{
    delete head_;
    delete tail_;
}

template<typename T>
LinkedList<T>::Node::Node(T& item): item_(item), next(nullptr), prev(nullptr)
{
}

template<typename T>
T& LinkedList<T>::Node::getItem()
{
    return item_;
}

template<typename T>
LinkedList<T>::Node& LinkedList<T>::Node::getNext()
{
    return &next_;
}

template<typename T>
LinkedList<T>::Node& LinkedList<T>::Node::getPrevious()
{
    return &prev_;
}

template<typename T>
void LinkedList<T>::Node::setNext(Node& next)
{
    this->next_ = next;
}

template<typename T>
void LinkedList<T>::Node::setPrevious(Node& prev)
{
    this->prev_ = prev;
}

template<typename T>
LinkedList<T>::Node::~Node()
{
}
