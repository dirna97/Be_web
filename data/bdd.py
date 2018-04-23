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

def verif_connect_admin(login,pwd):
    sql = "SELECT adm.idMembre, adm.nom,adm.prenom FROM administrateur as adm where adm.login=%s and adm.pwd= %s;"
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

def ajouter_membre_bdd(idMembre,nom,prenom,login,pwd,idEquipe):
    sql = "INSERT INTO `membre` (`idMembre`, `nom`, `prenom`, `login`, `pwd`, `idEquipe`) VALUES(%s, %s, %s, %s, %s, %s);"
    param = (idMembre,nom,prenom,login,pwd,idEquipe)

    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def ajouter_equipe_bdd(idEquipe,nom,idAvion):
    sql = "INSERT INTO `equipe` (`idEquipe`, `nom`, `idAvion`) VALUES (%s, %s, %s);"
    param = (idEquipe,nom,idAvion)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def get_idEquipe():
    sql = "SELECT COUNT(eq.idEquipe) from equipe as eq;"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_idMembre():
    sql = "SELECT COUNT(m.idMembre) from membre as m;"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_membres():
    sql = "SELECT * FROM membre"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idMembre, nom, prenom,login,pwd,idEquipe in cursor:
            dict[idMembre] = {"nom": str(nom)[12:-2], "prenom": str(prenom)[12:-2], "login": str(login)[12:-2], "pwd": str(pwd)[12:-2], "idEquipe": str(idEquipe)[12:-2]}
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

def get_equipes():
    sql = "SELECT * FROM equipe"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idEquipe,nom,idAvion in cursor:
            dict[idEquipe] = {"idEquipe": str(idEquipe)[12:-2],"nom": str(nom)[12:-2],"idAvion": str(idAvion)[12:-2] }
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

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
