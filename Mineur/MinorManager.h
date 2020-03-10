#ifndef MINOR_MANAGER_H
#define MINOR_MANAGER_H

#include "CommunicationHandler.h"
#include "Minor.h"
#include <map>

class MinorManager
{
private:
    Minor* minor;
    map<pair<string,string>, int>* msgs; 
    VerificationLevel verifLevel; 
    CommunicationHandler com;

public:
    MinorManager(Minor*& minor);

    ~MinorManager();

    // Handle all the resquest
    void ResquestHandler();

    // Handle all Response TODO Put this function on the server-side
    void ResponseHandler();

    // Validate hash of the block 
    void Validate();

    // Update the validation level 
    void UpdateValidationLevel();

    // process transaction request
    void ProcessTransreq(string request, int levelDiff);

    // process lesson info request
    void ProcessLessonInfoRep();

    // process student info request
    void ProcessStudentInfoReq();

    // process grades files request
    void ProceesGradesFilesReq();

    // process chains request
    void ProcessChainsReq();

    // process logs request
    void ProcessLogsReq();
};

#endif
