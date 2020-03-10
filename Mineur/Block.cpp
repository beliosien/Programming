#include "Block.h"

/*
*** Constructor of the Block class 
***
*/
Block::Block(string _data, char _hash[65], char _previousHash[65], VerificationLevel _verificationLevel)
{
    data = _data;
    verificationLevel = _verificationLevel;
    for (int i = 0 ;i < 65; i++)
    {
        previousHash[i] = _previousHash[i];
    }

    for (int i = 0 ;i < 65; i++)
    {
        hash[i] = _hash[i];
    }
    
    //char *bufferData = new char[_data.length() + 1];
    //strcpy(bufferData, _data.c_str());
    //CalculateHash(bufferData,  hash);
    //cout<<"le hash de la donnee " << _data << " est : " << hash <<endl;
    //delete [] bufferData;
    nextBlock = NULL;
}

Block::~Block()
{
    delete (nextBlock);
}

/*void Block::CalculateHash(char *string, char outputBuffer[65])
{
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, string, strlen(string));
    SHA256_Final(hash, &sha256);
    int i = 0;
    for(i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf(outputBuffer + (i * 2), "%02x", hash[i]);
    }
    outputBuffer[64] = 0;
}*/

/**
 * Retrieve the next block
**/ 
Block* Block::getNextBlock()
{
    return nextBlock;
}


/*
*** function that return the 
*** data inside the block
*/
string Block::getData()
{
    return data;
}

/*
** Set the data of the block
*/
void Block::setData(string _data)
{
    data = _data;
}

/**
 * Set the next block 
*/
void Block::setNextBlock(Block* block)
{
    nextBlock = block;
}

/*
** Set the previous hash of the block
*/
void Block::setPreviousHash(char _previousHash[65])
{
    for (int i = 0 ; i < 65 ; i ++)
    {
        previousHash[i] = _previousHash[i];
    }
}

/*
*** function that return the 
*** the hash of the block
*/
char* Block::getHash()
{
    return hash;
}

/*
*** function that return the 
*** the previous
*/
char* Block::getPreviousHash()
{
    return previousHash;
}

/**
 * Return the verification level of a block 
*/ 
string Block::getVerificationLevel()
{
    if (verificationLevel == RED){
        return "RED";
    } else if (verificationLevel == YELLOW)
    {
        return "YELLOW";
    } else
    {
        return "GREEN";
    }
}

/**
 * print the data 
*/
/*void Block::PrintData()
{
    cout << "Nom: " << data->nom << endl;
    cout << "Sigle:" << data->sigle << endl;
    cout << "Trimestre: " << data->trimestre << endl;
    cout << "Resultat: [" << endl;
    for (auto it = data->resultats.begin(); it != data->resultats.end(); it++)
    {
        cout << "   " << "matricule: " << it->matricule << endl;
        cout << "   " << "nom: " << it->nom << endl;
        cout << "   " << "note: " << it->note << endl;
        cout << "   " << "prenom: " << it->prenom << endl;
    }
    cout << "]" << endl;
}*/

void Block::setVerificationLevel(VerificationLevel verif)
{
    verificationLevel = verif;
}