#ifndef MINOR_H
#define MINOR_H

#include "LinkedList.h"
#include <vector>
#include <string>
#include <iostream>

//#include "Minor.cpp"

using namespace std;

class Minor
{
    private:
        //  list of all the blocks created
        LinkedList blockChain;
        int minorNumber = 2;


    public:
        // constructor 
        Minor();
        ~Minor();

        // Add new block in the list 
        void AddBlock(string data, char hash[65], VerificationLevel verifLevel);
        
        void EncryptSHA256 (char *string, char outputbuffer[65]);

        //Calculate the hash of the block according to the level of difficulties
        void CalculateHash(char *string, char outputBuffer[65], int levelDiff);

        // Validate the hash of the block
        VerificationLevel ValidateHashBlock(int validatedTime);

        // Update verification level 
        void UpdateVerificationLevel(int verifLevel, string message);

        // Check if the blockChain is empty
        bool isBlockChainEmpty();

        // check if the chain is valid
        bool isBlockChainValid();

        // print the value inside the block chain
        void PrintBlockChain();

        // get the number of the minor 
        int getMinorNumber();
};
#endif



