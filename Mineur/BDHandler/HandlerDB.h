#ifndef HANDLER_DB_H
#define HANDLER_DB_H

#include <sqlite3.h> 
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std ;


class HandlerDB
{
private:
    char* dataBaseName;
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
public:
    HandlerDB(char* _dataBaseName );
    ~HandlerDB();

    void ConnectDB() ;
    int  ExecutionSQLCommand(const char* sqlCommand) ;
    void CloseDB();
};
#endif