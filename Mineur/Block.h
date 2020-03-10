#ifndef BLOCK_H
#define BLOCK_H

#include <string>
#include <iostream>
#include <stdlib.h>     
#include <time.h>   
#include <openssl/sha.h>  
#include <stdio.h>
#include <string.h>  
#include "Constant.h"
//#include "../src/cpp/objects/payloads/reqPayloads.hpp"

using namespace std;

// header of Block class
class Block
{
    // attributes of the class 
    private:
        string data;   // pour l'instant ce sera un string comme donnée
        char hash[65];             // in the future it will be a string
        char previousHash[65];  // le hash du block vers lequel le bloc actuel pointe 
        Block* nextBlock;
        VerificationLevel verificationLevel = RED; 

    public:
        

        // constructor 
        Block(string _data, char _hash[65], char _previousHash[65], VerificationLevel _verificationLevel);
        ~Block();

        // Calcul of the hash of the block      // in the future it will be a string
        //void CalculateHash(char *string, char outputBuffer[65]);

        // Retreive the nextBLock
        Block* getNextBlock();

        // Retrieve the data of the block 
        string getData();

        // Set the data of the block
        void setData(string _data);

        // Set the next block
        void setNextBlock(Block* block);

        char* getHash();
        // Set the previous hash
        void setPreviousHash(char _previousHash[65]); 
        
        // Retrieve the hash of the block
        // char[] getHash();          // in the future it will be a string

        // Retrieve the previous hash
       char* getPreviousHash();       // in the future it will be a string

       //Get verification Level
       string getVerificationLevel();

       // print the data
       void PrintData();

       // set the verification level of a block  
       void setVerificationLevel(VerificationLevel verif);
};
#endif


