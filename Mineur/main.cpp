#include "./BDHandler/HandlerMinorDB.h"
#include "MinorManager.h"
#include <nlohmann/json.hpp>
#include <fstream>

using json = nlohmann::json;
// test of the current implementation 
int main() 
{
    //HandlerMinorDB handler("BlockChain");
    //handler.CreateTableDB();
    //cout <<"the result in main is :" << handler.CheckIfTheTableExists("COURS")<<endl;
    // Minor* myMinor = new Minor();
    // char outputbuffer[65];
    // myMinor->CalculateHash("testSarra", outputbuffer, 5);
    // cout << "le outputbuffer est : "<<outputbuffer << endl;
    // // myMinor->AddBlock("sarra");
    // // myMinor->AddBlock("philippe");
    // // myMinor->AddBlock("prof");

    // //cout << myMinor.isBlockChainValid() << endl;

    // myMinor->PrintBlockChain();
    //Minor* myMinor =  new Minor();
    //MinorManager manager = MinorManager(myMinor);
    //manager.ResquestHandler();
const std::string TRANSACTION_MOCK_JSON = "{\"sigle\":\"INF3995\",\"nom\":\"Gestion_de_projet\",\"trimestre\":2093,\"resultats\":[{\"nom\":\"Someone\",\"prenom\":\"Someone\",\"matricule\":\"1111111\",\"note\":\"100\"}]}";
    PayloadRequestType rq = TransactionReq;
    CommunicationHandler handlerCommunication;
    //ifstream file("transaction.json");
    //string Json = json::parse(file).dump() ;
    handlerCommunication.SendRequest(TRANSACTION_MOCK_JSON, "test",rq);


}