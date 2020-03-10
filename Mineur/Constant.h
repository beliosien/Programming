#ifndef CONSTANT_H
#define CONSTANT_H

#include <string>

using namespace std;

const string IP_ADDR_HOST = "10.200.22.29:5001";
const string HANDLE_MESSAGE_TOPIC = "Validation";
const string REQUEST_TOPIC = "test";
const string RESPONSE_TOPIC = "response";
const string UPDATING_TOPIC = "update";
const int MINOR_1 = 1;
const int MINOR_2 = 2;
const int MINOR_3 = 3;
const int TIME_OUT_PRODUCER = 5;
static const char MINOR_1_KEY = '1';
static const char MINOR_2_KEY = '2';
static const char MINOR_3_KEY = '3';

enum VerificationLevel {
    RED = 1,
    YELLOW = 2,
    GREEN = 3,
    WHITE = 0
};

const string insertCours = "INSERT INTO COURS(SIGLE, NOM, TRIMESTRE)"\
                            "VALUES";
const string insertEtudiant = "INSERT INTO ETUDIANT(MATRICULE, NOM, PRENOM)"\
                                "VALUES";
const string insertResultat="INSERT INTO RESULTAT(MATRICULE, SIGLE)"\
                            "VALUES";

const string inserthistorique= "INSERT INTO HISTORIQUE(TYPETRANS, SIGLE, MATRICULE, IDRES)"\
                            "VALUES";

enum nameTableSQLite3 {cours, etudiant, resultat, historique};

const string sqlComCreate[] = {
    "CREATE TABLE "\
    "IF NOT EXISTS COURS("\
    "SIGLE TEXT PRIMARY KEY NOT NULL,"\
    "NOM TEXT NOT NULL,"\
    "TIMESTRE CHAR(5));", 

    "CREATE TABLE "\
    "IF NOT EXISTS ETUDIANTS("\
    "MATRICULE INT PRIMARY KEY NOT NULL,"\
    "NOM TEXT NOT NULL,"\
    "PRENOM TEXT NOT NULL);",


    "CREATE TABLE "\
    "IF NOT EXISTS RESULTAT("\
    "IDRES INT NOT NULL PRIMARY KEY AUTOINCREMENT,"\
    "MATRICULE INT NOT NULL,"\
    "SIGLE TEXT NOT NULL,"\
    "FOREIGN KEY (MATRICULE) REFERENCES ETUDIANTS(MATRICULE),"\
    "FOREIGN KEY (SIGLE) REFERENCES COURS(SIGLE));",

    "CREATE TABLE "\
    "IF NOT EXISTS HISTORIQUE("\
    "IDTRANS INT NOT NULL PRIMARY KEY  AUTOINCREMENT,"\
    "TYPETRANS TEXT NOT NULL,"\
    "SIGLE TEXT NOT NULL,"\
    "MATRICULE INT NOT NULL,"\
    "IDRES INT NOT NULL,"\
    "FOREIGN KEY (MATRICULE) REFERENCES ETUDIANTS(MATRICULE),"\
    "FOREIGN KEY (SIGLE) REFERENCES COURS(SIGLE),"\
    "FOREIGN KEY (IDRES) REFERENCES RESULTAT(IDRES))"
};
#endif