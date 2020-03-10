#include "HandlerMinorDB.h"


HandlerMinorDB::HandlerMinorDB(char* dataBaseName) : handlerDB(dataBaseName), _dataBaseName(dataBaseName)
{
    //_dataBaseName = dataBaseName;
}


HandlerMinorDB::~HandlerMinorDB()
{
}

void HandlerMinorDB::CreateTableDB()
{
    for (int i = 0 ; i < sizeof(sqlComCreate)/sizeof(string) ;i++)
    {
        cout << "la commande est : " << sqlComCreate[i] <<endl;
        cout << "the CreateTableDB " << i <<" : "
            << handlerDB.ExecutionSQLCommand(sqlComCreate[i].c_str())<<endl;
    }
}

void HandlerMinorDB::InsertElement(nameTableSQLite3 nameTable, string command) {
    //extract the table
    string str[] ={ ""};
    string commandSQL = CreateCommandInsert(nameTable, str);
    handlerDB.ExecutionSQLCommand(commandSQL.c_str());
}

string HandlerMinorDB::CreateCommandInsert(nameTableSQLite3 nameTabe, string str[]){
    string sqlCommand ;
    switch (nameTabe){
        case cours:
            sqlCommand = insertCours ;
            break;
        case etudiant:
            sqlCommand = insertEtudiant;
            break;
        case resultat:
            sqlCommand = insertResultat;
            break;
        case historique:
            sqlCommand = inserthistorique;
            break;
        default:
            break;
    }
    sqlCommand += "(";
    for (int i = 0 ; i < sizeof(str)/sizeof(string); i++) {
        sqlCommand += str[i];
        if (i!=sizeof(str)/sizeof(string)-1)
            sqlCommand+=",";
    }
    sqlCommand += ")";
    cout << " la commande insert est : "<< sqlCommand ;
    return sqlCommand;
}
