#!C:\\python34
# -*- coding: UTF-8 -*-
# enable debugging
import mysql.connector
from mysql.connector import errorcode

conf=Import('../data/config.py')
config=conf.configBD()

def connexion():
    cnx=""
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    return cnx

def close_bd(cursor,cnx):
    cursor.close()
    cnx.close()

# insertion dans la table commentaires


def verif_connect(login,pwd):
    sql = "SELECT membre.idMembre, membre.nom,membre.prenom FROM membre where membre.login=%s and membre.pwd= %s;"
    param = (login, pwd)

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql, param)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_aerodromes():
    sql = "SELECT idAerodrome, lat, lon FROM aerodrome"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idAerodrome, lat, lon in cursor:
            dict[idAerodrome] = "{lat: "+str(lat)+", lng: "+str(lon)+"}"

    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict
