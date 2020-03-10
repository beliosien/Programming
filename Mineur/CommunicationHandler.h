#ifndef COMMUNICATION_HANDLER_H
#define COMMUNICATION_HANDLER_H

#include <stdexcept>
#include <iostream>
#include <thread> 
#include <csignal>
#include <boost/program_options.hpp>
#include "cppkafka/consumer.h"
#include "cppkafka/producer.h"
#include "cppkafka/configuration.h"
#include "Constant.h"
#include "../../src/cpp/services/serializationService/serializationService.hpp"
#include <chrono>
#include <vector>
#include <map>
//#include "../src/cpp/services/serializationService/serializationService.cpp"

using std::cout;
using std::endl;
using std::getline;
using std::cin;
using std::thread;
using std::string;
using std::exception;

using cppkafka::Consumer;
using cppkafka::Producer;
using cppkafka::Message;
using cppkafka::Configuration;
using cppkafka::MessageBuilder;
using cppkafka::TopicPartitionList;

class  CommunicationHandler
{
    private:
        Producer* producer;
        MessageBuilder* builder;

    public:
                
        CommunicationHandler();
        ~CommunicationHandler();

        // Initialize topics for communication
        void Initialize();

        // Send message in a topic
        void Produce(string topic, string message, string key);

        // Send the Resquest
        void SendRequest(string Json, string topic, PayloadRequestType type);

        //send the response
        void SendResponse(void* payload, PayloadResponseType type);

        //Create consumer for a topic
        Consumer* createConsumer(string host, int group_id, string topic);

        // get the request 
        PayloadRequestType getRequest(int type);

        // get the response
        string getResponse(PayloadResponseType type);
};
#endif
