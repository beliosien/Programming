#include "MinorManager.h"

bool running = true;

MinorManager::MinorManager(Minor*& _minor)
{
    minor = _minor;
    msgs = new map<pair<string,string>, int>[2];
    verifLevel = RED;

    thread requestHandlerThread(&MinorManager::ResquestHandler,this);
    thread ValidateThread(&MinorManager::Validate,this);
    thread UpdateThread(&MinorManager::UpdateValidationLevel,this);
    
    requestHandlerThread.join();
    ValidateThread.join();
}

MinorManager::~MinorManager()
{
    minor->~Minor();
}

void MinorManager::ResquestHandler()
{
    // Stop processing on SIGINT
    signal(SIGINT, [](int) { running = false; });
    Consumer* consumer = com.createConsumer(IP_ADDR_HOST, 2, REQUEST_TOPIC);
    // Now read lines and write them into kafka
    while (running) {
        // Try to consume a message
        Message msg = consumer->poll();
        if (msg) {
            // If we managed to get a message
            if (msg.get_error()) {
                // Ignore EOF notifications from rdkafka
                if (!msg.is_eof()) {
                    cout << "[+] Received error notification: " << msg.get_error() << endl;
                }
            }
            else {
                // get the request 
                int key = stoi(msg.get_key());
                PayloadRequestType requestType = com.getRequest(key);
                // get the payload
                string request = msg.get_payload();
                TransactionReqPayload* trans = (TransactionReqPayload*)SerializationService::Deserialize(request, requestType); 
                cout << trans->sigle << endl;
                switch (requestType)
                {
                    case TransactionReq:
                        // TODO modify communication for this transaction
                        ProcessTransreq(request, 0);
                        break;
                    case LessonInfoReq:
                        break;
                    case StudentInfoReq:
                        break;
                    case GradesFileReq:
                        break;
                    case ChainsReq:
                        break;
                    case LogsReq:
                        break;  
                    default:
                        cout << "Can't handle the resquest" << endl;
                        break;
                }
                // Now commit the message
                consumer->commit(msg);
            }
        }
    }

}

void MinorManager::ResponseHandler()
{
    // Stop processing on SIGINT
    signal(SIGINT, [](int) { running = false; });
    Consumer* consumer = com.createConsumer(IP_ADDR_HOST, 2, RESPONSE_TOPIC);
    // Now read lines and write them into kafka
    while (running) {
        // Try to consume a message
        Message msg = consumer->poll();
        if (msg) {
            // If we managed to get a message
            if (msg.get_error()) {
                // Ignore EOF notifications from rdkafka
                if (!msg.is_eof()) {
                    cout << "[+] Received error notification: " << msg.get_error() << endl;
                }
            }
            else {
                string key = msg.get_key();
                // Now commit the message
                consumer->commit(msg);

                // get the key of the response

                // get the response 
                string message = msg.get_payload();
                // send the response
            }
        }
    }

}


void MinorManager::Validate()
{
    // Stop processing on SIGINT
    signal(SIGINT, [](int) { running = false;});
    // Create the consumer
    Consumer* consumer = com.createConsumer(IP_ADDR_HOST, 2, HANDLE_MESSAGE_TOPIC);
    while (running) {
        // Try to consume a message
        Message msg = consumer->poll();
        if (msg) {
            // If we managed to get a message
            if (msg.get_error()) {
                // Ignore EOF notifications from rdkafka
                if (!msg.is_eof()) {
                    cout << "[+] Received error notification: " << msg.get_error() << endl;
                }
            }
            else {
                string key = msg.get_key();
                // Now commit the message
                consumer->commit(msg);
                string message = msg.get_payload();

                message.replace(0,1,"");
                string data = message.substr(0, message.find(" "));
                string hash = message.substr(message.find(" ")+1, message.length());
                auto it = msgs->find(make_pair(data,hash));
                if (it->first.first.empty())
                {
                    msgs->insert(make_pair(pair<string,string>(data,hash),1));
                    
                } else
                {
                    it->second++;
                    // add in the map
                    verifLevel = minor->ValidateHashBlock(it->second);
                }
            }
        }
    }
}

void MinorManager::UpdateValidationLevel()
{
    // Stop processing on SIGINT
    signal(SIGINT, [](int) { running = false;});
    // Create the consumer
    Consumer* consumer = com.createConsumer(IP_ADDR_HOST, 2, UPDATING_TOPIC);
    while (running) {
        // Try to consume a message
        Message msg = consumer->poll();
        if (msg) {
            // If we managed to get a message
            if (msg.get_error()) {
                // Ignore EOF notifications from rdkafka
                if (!msg.is_eof()) {
                    cout << "[+] Received error notification: " << msg.get_error() << endl;
                }
            }
            else 
            {
                int key = stoi(msg.get_key());
                string message = msg.get_payload();
                int veriflevel = stoi(message.substr(0, message.find(" ")));
                cout << "--- verif level " << veriflevel << endl;

                if (key != minor->getMinorNumber() && 
                                minor->ValidateHashBlock(veriflevel) != verifLevel)
                {
                    cout << "inside " << endl;
                    message = message.substr(message.find(" ")+1 , message.length());
                    minor->UpdateVerificationLevel(veriflevel, message);
                } else
                {
                    cout << "pas besoin de mettre à jour" << endl;
                }
                
            }
        }
    }

}

void MinorManager::ProcessTransreq(string request, int levelDiff)
{
    auto start = std::chrono::high_resolution_clock::now();
    auto end = start + chrono::microseconds(1);
    char hash[65];
    minor->CalculateHash(const_cast<char*>(request.c_str()), hash, levelDiff);
    //sleep(5);
    string messageToProduce = to_string(minor->getMinorNumber()) + request + " " + hash;
    // send your hash to others
    com.Produce(HANDLE_MESSAGE_TOPIC, messageToProduce, to_string(minor->getMinorNumber()));
    // wait a bit for the validation
    do {
            std::this_thread::yield();
    } while (std::chrono::high_resolution_clock::now() < end);                 
    // add the block 
    // while updating do noting 
    minor->AddBlock(request, hash, verifLevel);
    // empty validation list after
    msgs->clear();
    // if verif level is green update blockain for others
    if (verifLevel == GREEN)
    {
        string message = to_string(verifLevel) + " " + request;
        com.Produce(UPDATING_TOPIC,message,to_string(minor->getMinorNumber()));
    }
}