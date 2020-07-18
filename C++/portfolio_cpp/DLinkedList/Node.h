#pragma once
#ifndef NODE_H
#define NODE_H

template<typename T>
class Node
{
public:
	// constructor
	Node(T item);
	// destructor
	~Node();
	// return the item of the node
	T getItem();
	// return the next node
	Node<T>* getNext();
	// retunr the prev node
	Node<T>* getPrev();
	// set the next node
	void setNext(Node<T>* next);
	// set the previous
	void setPrevious(Node<T>* prev);

private:
	T item_;
	Node<T>* next_; 
	Node<T>* prev_;
};

#endif // !NODE_H

