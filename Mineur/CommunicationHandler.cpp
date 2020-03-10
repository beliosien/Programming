#include "CommunicationHandler.h"

/**
 * Constructor
*/
CommunicationHandler::CommunicationHandler()
{
    //minor = _minor;
    //msgs = new map<pair<string,string>, int>[2];
    //Initialize();
}


/**
 * Destructor  
*/
CommunicationHandler::~CommunicationHandler()
{
    delete producer;
    //delete consumer;
}

/**
 * Initialize Communication
*/ 
void CommunicationHandler::Initialize()
{
   /* if (clientType == Server)
    {
        thread responseHandlerThread(&CommunicationHandler::ResponseHandler,this);
        responseHandlerThread.join();
    } else if (clientType == Minor)
    {
        thread requestHandlerThread(&CommunicationHandler::ResquestHandler,this);
        requestHandlerThread.join();
    } */
}

/**
 * Produce message 
 * @param key the key of the minor
 * @param hash the calculated hash
*/
void CommunicationHandler::Produce(string topic, string message, string key)
{
    // Create a message builder for this topic
    builder = new MessageBuilder(topic);

    // Get the partition we want to write to. If no partition is provided, this will be
    // an unassigned one
    builder->partition(0);

    // Construct the configuration
    Configuration config = {
        { "metadata.broker.list", IP_ADDR_HOST}
    };

    // Create the producer
    producer = new Producer(config);
    cout << "Producing messages into topic " << topic << endl;

    // Set the payload  et the key on this builder
    builder->key(key);
    builder->payload(message);

    // Actually produce the message we've built
    producer->produce(*builder);
    
    sleep(TIME_OUT_PRODUCER);
    // Flush all produced messages
    producer->flush();
}

Consumer* CommunicationHandler::createConsumer(string host, int group_id, string topic)
{
    // Construct the configuration
    Configuration config = {
        { "metadata.broker.list", host },
        { "group.id", group_id },
        // Disable auto commit
        { "enable.auto.commit", false }
    };

     // Create the consumer
    Consumer* consumer = new Consumer(config);

    // Print the assigned partitions on assignment
    consumer->set_assignment_callback([](const TopicPartitionList& partitions) {
        cout << "Got assigned: " << partitions << endl;
    });

    // Print the revoked partitions on revocation
    consumer->set_revocation_callback([](const TopicPartitionList& partitions) {
        cout << "Got revoked: " << partitions << endl;
    });

    // Subscribe to the topic
    consumer->subscribe({topic});

    cout << "Consuming messages from topic " << topic << endl;

    return consumer;
}

PayloadRequestType CommunicationHandler::getRequest(int type)
{
    if(type == TransactionReq)
        return TransactionReq;
    if(type == LessonInfoReq)
        return LessonInfoReq;
    if(type == StudentInfoReq)
        return StudentInfoReq;
    if(type == GradesFileReq)
        return GradesFileReq;
    if(type == ChainsReq)
        return ChainsReq;
    if(type == LogsReq)
        return LogsReq;  
}

string CommunicationHandler::getResponse(PayloadResponseType type)
{
    

}

void CommunicationHandler::SendRequest(string Json, string topic, PayloadRequestType type)
{
    string key = to_string(type);
    Produce(topic, Json, key);
}

void CommunicationHandler::SendResponse(void* payload, PayloadResponseType type)
{
    string response = SerializationService::Serialize(payload, type);
    string key = to_string(type);
    Produce(RESPONSE_TOPIC, response,key);
}