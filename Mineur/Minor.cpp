#include "Minor.h"

/**
 * Constructor
**/
Minor::Minor()
{
    cout<< "Debut Minor " << endl;
}

/**
 * Destructor
*/
Minor::~Minor()
{
    cout<< "fin Minor " << endl;
}

/**
 * Return the hash of the block
*/
void Minor::EncryptSHA256 (char *string, char outputbuffer[65])
{
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, string, strlen(string));
    SHA256_Final(hash, &sha256);
    int i = 0;
    for(i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf(outputbuffer + (i * 2), "%02x", hash[i]);
    }
    outputbuffer[64] = 0;
}


void Minor::CalculateHash(char *string, char outputBuffer[65], int levelDiff)
{
    std::string levelDiffString ="";
    
    for (int i = 0 ; i < levelDiff ; i++)
    {
        levelDiffString =levelDiffString + '0';
    }
    bool levelDiffValid = false ;
    EncryptSHA256 (string, outputBuffer);
    
    while (!levelDiffValid)
    {
        std::string bufferConvert =  outputBuffer;
        levelDiffValid = (bufferConvert.find( levelDiffString)==0) ;
        if (!levelDiffValid)
        {
            EncryptSHA256 (outputBuffer, outputBuffer);
        }
            
    }

}


/**
 * Function that add a block in 
 * the block chain 
 *  @param data 
**/
void Minor::AddBlock(string data, char hash[65], VerificationLevel verifLevel)
{
    blockChain.AddBlock(data, hash,verifLevel);
}

/**
 * Function that verify if 
 * the block chain is empty or not
 * return true if the block chain is true
**/
bool Minor::isBlockChainEmpty()
{
    return blockChain.isListEmpty();
}

/*
*** Verify if the chain is still valid 
*** return true if it is the case
*/
bool Minor::isBlockChainValid()
{
    return isBlockChainEmpty() ? true : blockChain.isListValid();
}


/*
*** Function that print all the values
*** inside the block chain 
*/
void Minor::PrintBlockChain() 
{
  blockChain.DisplayList();
}

/**
 * Validate the hash 
 * @param hash 
 * @param data
 * @param msgs
*/ 
VerificationLevel Minor::ValidateHashBlock(int validatedTime)
{
    cout << validatedTime << endl;

    if (validatedTime == 1)
    {
        cout << "RED" << endl;
        return RED;
    } else if (validatedTime == 2)
    {
        cout << "YELLOW" << endl;
        return YELLOW;
    } else if (validatedTime == 3)
    {
        cout << "GREEN" << endl;
        return GREEN;
    }
    //should never get here
    cout <<"WHITE" << endl;
    return WHITE;
    
}

/**
 * @return the minor number 
*/
int Minor::getMinorNumber()
{
    return minorNumber;
}

void Minor::UpdateVerificationLevel(int verifLevel, string message)
{
    Block* block = blockChain.getHead();
    int i = 0;
    while (block != NULL)
    {
        if (block->getData() == message) 
        {
            block->setVerificationLevel(ValidateHashBlock(verifLevel));
            cout << "Mise à jour terminé" << endl;
            break;
        }
        
        i++;
    }   
}
