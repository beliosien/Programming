#include "DLinkedList.h"

template<typename T>
DLinkedList<T>::DLinkedList() : head_(nullptr), tail_(nullptr)
{
    size_ = 0;
}

template<typename T>
DLinkedList<T>::~DLinkedList()
{
    if (!this->isEmpty())
    {
        this->clear();
    }
}

template<typename T>
void DLinkedList<T>::addFirst(T item)
{
    if (this->isEmpty())
    {
        head_ = new Node<T>(item);
        tail_ = head_;
    }
    else
    {
        if (this->size_ == 1)
        {
            head_ = new Node<T>(item);
            head_->setPrevious(tail_);
            tail_->setNext(head_);

        }
        else
        {
            Node<T>* temp = head_;
            head_ = new Node<T>(item);
            temp->setNext(head_);
            head_->setPrevious(temp);
        }
    }
    size_++;
}

template<typename T>
void DLinkedList<T>::addLast(T item)
{
    if (this->isEmpty())
    {
        tail_ = new Node<T>(item);
        head_ = tail_;
    }
    else if (this->size_ == 1)
    {
        tail_ = new Node<T>(item);
        tail_->setNext(head_);
        head_->setPrevious(tail_);
    }
    else
    {
        Node<T>* temp = tail_;
        tail_ = new Node<T>(item);
        temp->setPrevious(tail_);
        tail_->setNext(temp);
    }
    size_++;
}

template<typename T>
T DLinkedList<T>::removeFirst()
{
    Node<T>* temp = head_;
    T item = head_->getItem();
    head_ = head_->getPrev();
    head_->setNext(nullptr);
    size_--;
    delete temp;
    return item;
}

template<typename T>
T DLinkedList<T>::removeLast()
{
    Node<T>* temp = tail_;
    T item = tail_->getItem();
    tail_ = tail_->getNext();
    tail_->setPrevious(nullptr);
    size_--;
    delete temp;
    return item;
}

template<typename T>
int DLinkedList<T>::size()
{
    return this->size_;
}

template<typename T>
bool DLinkedList<T>::isEmpty()
{
    return this->size_ == 0;
}

template<typename T>
Node<T>* DLinkedList<T>::getHead()
{
    return head_;
}

template<typename T>
Node<T>* DLinkedList<T>::getTail()
{
    return tail_;
}

template<typename T>
void DLinkedList<T>::clear()
{
    Node<T>* temp = head_;
    while (temp != nullptr)
    {
        Node<T>* temp_ = temp;
        temp = temp->getPrev();
        delete temp_;
        size_--;
    }
    delete temp;
}

template<typename T>
void DLinkedList<T>::remove(T item)
{
    Node<T>* temp = head_;
    while (temp->getItem() != item)
    {
        temp = temp->getPrev();  
    }
    temp->getNext()->setPrevious(temp->getPrev());
    temp->getPrev()->setNext(temp->getNext());
    size_--;
    delete temp;
}

