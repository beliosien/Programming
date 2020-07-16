/**
 * @author Ossim Belias
 * 
 * @brief Implementation of my own generic  doubly LinkedList in C++
 *
*/

template <typename T>
class LinkedList
{
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
        Node& getNext();
        // return the previous node
        Node& getPrevious();
        // return the item
        T& getItem();
        // set the next node
        void setNext(Node& next);
        // set the previous node
        void setPrevious(Node& previous);
    };
    
private:
    Node* head_;
    Node* tail_;
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
};


