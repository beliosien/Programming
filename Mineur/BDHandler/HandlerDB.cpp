#include "HandlerDB.h"

static int callback(void *NotUsed, int argc, char **argv, char **azColName) {
   int i;
   for(i = 0; i<argc; i++) {
      printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
   }
   printf("\n");
   return 0;
}


HandlerDB::HandlerDB(char* _dataBaseName)
{
    dataBaseName = _dataBaseName;
    ConnectDB();
}

HandlerDB::~HandlerDB(){}

void HandlerDB::ConnectDB() 
{
    rc = sqlite3_open(dataBaseName, &db);
    if( rc ) {
      fprintf(stderr, "Impossible d'ouvrir la base de donnee: %s\n", sqlite3_errmsg(db));
    } else {
        fprintf(stderr, "Connection reussie\n");
    }
}

int HandlerDB::ExecutionSQLCommand(const char *sqlCommand)
{
    rc = sqlite3_exec(db, sqlCommand, callback, 0, &zErrMsg);
   
   if( rc != SQLITE_OK ){
      fprintf(stderr, "La commande ne fonctionne pas : %s\n", zErrMsg);
      sqlite3_free(zErrMsg);
   } else {
      fprintf(stdout, "Commande executee avec succes\n");
   }
   return rc;
}

void HandlerDB::CloseDB()
{
    sqlite3_close(db);
    fprintf(stdout, "Base de donnee ferme\n");
}


