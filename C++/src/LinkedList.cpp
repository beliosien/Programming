#include "LinkedList.h"

template<typename T>
LinkedList<T>::LinkedList(): head_(nullptr), tail_(nullptr)
{
    size_ = 0;
}

template<typename T>
LinkedList<T>::~LinkedList()
{
    delete head_;
    delete tail_;
}

template<typename T>
void LinkedList<T>::addFirst(T& item)
{
    if (this.isEmpty())
    {
        head_ = new Node(item);
        tail_ = head_;
    } else
    {
        if (this->size == 1)
        {
            head_ = new Node(item);
            head_->setPrevious(tail_);
            tail_->setNext(head_);

        } else
        {
            Node<T>* temp = head_;
            head_ = new Node(item);
            temp->setNext(head_);
            head_->setPrevious(temp); 
        }
    }
    size_++;
}

template<typename T> 
void LinkedList<T>::addLast(T& item)
{
    if (this->isEmpty())
    {
        tail_ = new Node(item);
        head_ = tail_;
    } else if (this->size_ == 1)
    {
        tail_ = new Node(item);
        tail_->setNext(head_);
        head_->setPrevious(tail_);
    } else
    {
        Node<T>* temp = tail;
        tail_ = new Node(item);
        temp->setPrevious(tail_);
        tail_->setNext(temp);
    }
    size_++;
}

template<typename T>
T& LinkedList<T>::removeFirst()
{
    Node* temp = head_;
    T item = head_->getItem();
    head_ = head_->getPrevious();
    head_->setNext(nullptr);
    size_--;
    delete temp;
    return item;
}

template<typename T>
T& LinkedList<T>::removeLast()
{
    Node* temp = tail_;
    T item = tail_->getItem();
    tail_ = tail_->getNext();
    tail_->setPrevious(nullptr);
    size_--;
    delete temp;
    return item;
}

template<typename T>
int LinkedList<T>::size()
{
    return this->size_;
}

template<typename T>
bool LinkedList<T>::isEmpty()
{
    return this->size_ == 0;
}