#ifndef HANDLER_MIONR_H
#define HANDLER_MINOR_H

#include <sqlite3.h> 
#include <stdio.h>
#include <string>
#include <iostream>
#include "HandlerDB.h"
#include "../Constant.h"

using namespace std ;

class HandlerMinorDB
{
    private:
        char* _dataBaseName;
        HandlerDB handlerDB;
       
    public:
        HandlerMinorDB(char* _dataBaseName );
        ~HandlerMinorDB();
        void CreateTableDB();
        void InsertElement (nameTableSQLite3 nameTable, string command);
        string CreateCommandInsert(nameTableSQLite3 nameTabe, string str[] );
        
};
#endif