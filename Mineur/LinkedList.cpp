#include "LinkedList.h"

/*
** Constructor
*/
LinkedList::LinkedList()
{
    headBlock = NULL;
    tailBlock = NULL;
}


/*
** Destructor 
*/
LinkedList::~LinkedList()
{
    // delete(headBlock);
    // delete(tailBlock);
}

/*
** Function that create the 
** first block of the chain
** parameter name = data 
*/
Block* LinkedList::CreateGenesisBlock(string data,char hash[65],VerificationLevel verificationLevel)
{
    cout<<"debutCreateGenesisBlock" << endl;
    Block* block = new Block(data, hash,"0",verificationLevel);
    cout<<"endCreateGenesisBlock" << endl;
    return block;
}


/*
** Function that add a new block
** in the chain 
** paramater name = data
*/
void LinkedList::AddBlock(string data, char hash[65], VerificationLevel verificationLevel) 
{
    if (isListEmpty()) 
    {
        Block* block = CreateGenesisBlock(data,hash,verificationLevel);
        headBlock = block;
        tailBlock = block;
        block = NULL;  
    } else 
    {
        Block* block = new Block(data,hash, getTail()->getHash(),verificationLevel);
        tailBlock->setNextBlock(block);
        tailBlock = block;  
    }

    
}

/**
 * Return the last added block 
**/
Block* LinkedList::getTail()
{
    return tailBlock;
}

/**
 * Return the head block of the list 
**/
Block* LinkedList::getHead()
{
    return headBlock;
}


/**
 * Return true if the list 
 * is empty
**/
bool LinkedList::isListEmpty()
{
    return (headBlock == NULL);
}

/**
 * Return true if the list is valid 
*/
bool LinkedList::isListValid() 
{
    Block* block = headBlock;
    
    while (block != NULL)
    {
       
        if (block->getNextBlock() != NULL && block->getHash()!= block->getNextBlock()->getPreviousHash())
        {
            return false;
        }
        block = block->getNextBlock();
    }

    return true;
}


/**
 * Display the entire list
 * 
**/ 
void LinkedList::DisplayList()
{
    Block* block = headBlock;
    int i = 0;
    while (block != NULL)
    {
        cout << "Block#" << i << endl;
        cout << "data: ";
        //block->PrintData(); 
        cout << "hash: " << block->getHash() << endl;
        cout << "previous: " << block->getPreviousHash() << endl;
        cout << "verificationLevel: " << block->getVerificationLevel() << endl;
        block = block->getNextBlock();
        i++;
    }
}