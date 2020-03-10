#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include "Block.h"
using namespace std;

class LinkedList
{
private:
    // The head block of the linked list
    Block* headBlock;
    Block* tailBlock;

public:
    // Constructor 
    LinkedList();

    // Destructor
    ~LinkedList();

    // Add a new block in the block chain
    void AddBlock(string data, char hash[65], VerificationLevel verificationLevel);

    // Return the last added block   
    Block* getTail();

    // Return the first block 
    Block* getHead();

    // Create the first block of the list
    Block* CreateGenesisBlock(string data, char hash[65], VerificationLevel verificationLevel);

    // Check if the blockChain is empty
    bool isListEmpty();

    // Check if the list is valid
    bool isListValid();

    // print the list
    void DisplayList();

};
#endif
