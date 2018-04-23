template = Import('template.py')
bdd = Import('../data/bdd.py')
conf = Import('../data/config.py')
cookies = Import('../python/cookies.py')
chemin = conf.chemin()
import random as rd



def index():
    if "nom" in COOKIE and int(COOKIE["admin"].value)==1:
        result = template.entete(chemin,'CB-Ajouter')
        result += template.main_header(chemin)
        result += template.sidebar(5, chemin, COOKIE["admin"].value)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def ajouter_membre_card():
    idMembre = str(int(bdd.get_idMembre()[0]) + 1)
    amc='''  <div class="card">
            <div class="card-header">
                <div class="card-title">Ajouter un membre</div>
            </div>
            <div class="card-body">
                 <form method="post" action="'''+chemin+'''/python/ajouter_equipe.py/ajouter_membre">
                    <div class="form-group">
                        <input type="nom" class="form-control" name="nom" placeholder="Nom">
                    </div>
                    <div class="form-group">
                        <input type="prenom" class="form-control" name="prenom" placeholder="Prénom">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control" name="login" placeholder="Email">
                    </div>
                    <div class="form-group">
                        <input type="idEquipe" class="form-control" name="idEquipe" placeholder="Identifiant de l'équipe">
                    </div>
                    <div class="form-group">
                        <label class="control-label">
                            Le mot de passe provisoire de ce nouveau membre sera :
                        </label> 
                        <!----> <p class="form-control-static text-danger"> pwd : '''+save_mdp()+'''</p> <!---->  
                    </div>
                    <div class="form-group">
                        <label class="control-label">
                            L'identifiant de ce nouveau membre sera :
                        </label> <!----> <p class="form-control-static text-primary"> idMembre : '''+idMembre+'''</p> <!---->  
                    </div>
                    <div class="card-action">
                        <button class="btn btn-success">Ajouter membre</button>
                    </div>
                </form>
            </div>
        </div>'''
    return amc

def save_mdp():
    mdp_provisoire = str(rd.randint(1000, 9999))
    cookies.set_cookie("mdp_provisoire",mdp_provisoire )
    return mdp_provisoire

def ajouter_membre(nom='',prenom='',login='',idEquipe=''):
    idMembre = int(bdd.get_idMembre()[0]) + 1
    if (nom,prenom,login,idEquipe)!=('','','',''):
        bdd.ajouter_membre_bdd(idMembre,nom,prenom,login,str(COOKIE["mdp_provisoire"].value),idEquipe)
    raise HTTP_REDIRECTION(chemin + '/python/ajouter_equipe.py')


def liste_membre_card():
    dico_membres = bdd.get_membres()
    lmc= '''<div class="card">
                <div class="card-header">
                    <div class="card-title">Liste des membres</div>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="exampleFormControlSelect2">Id membre - Nom - Prenom</label>
                        <select multiple class="form-control" id="exampleFormControlSelect2">
                            '''+afficher_membres(dico_membres)+'''
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="comment">Informations complémentaires</label>
                         <select multiple class="form-control" id="exampleFormControlSelect2">
                        </select>
                    </div>
                    <div class="card-action">
                        <button class="btn btn-success">Submit</button>
                        <button class="btn btn-danger">Cancel</button>
                    </div>
                </div>
            </div>'''
    return lmc

def afficher_membres(dico={}):
    html_code=""
    for id in dico:
        html_code+="<option>"+str(id)+" - "+dico[id]["nom"]+" - "+dico[id]["prenom"]+"</option>"
    return html_code

def creer_equipe_card():
    idEquipe = str(int(bdd.get_idEquipe()[0]) + 1)
    cec='''<div class="card">
                <div class="card-header">
                    <div class="card-title">Créer une équipe</div>
                </div>
                <div class="card-body">
                    <form method="post" action="'''+chemin+'''/python/ajouter_equipe.py/ajouter_eq">
                        <div class="form-group">
                            <input type="text" class="form-control" name="nom_eq" placeholder="Nom de l'équipe">
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" name="idAvion" placeholder="Identifiant de l'avion">
                        </div>
                        <div class="form-group">
                        <label class="control-label">
                            L'identifiant de cette nouvelle équipe sera :
                        </label> <!----> <p class="form-control-static text-primary"> idEquipe : '''+idEquipe+'''</p> <!---->  
                        </div>
                        <div class="form-group"></div><div class="form-group"></div><div class="form-group"></div>
                        <div class="form-group"></div><div class="form-group"></div>
                        <div class="card-action">
                            <button class="btn btn-success">Créer l'équipe</button>
                        </div>	
                    </form>							
                </div>
            </div>'''
    return cec

def ajouter_eq(nom_eq='',idAvion=''):
    idEquipe = int(bdd.get_idEquipe()[0])+1
    if nom_eq!='' and idAvion!='':
        bdd.ajouter_equipe_bdd(idEquipe, nom_eq, idAvion)
    raise HTTP_REDIRECTION(chemin + '/python/ajouter_equipe.py')

def liste_equipe_card():
    dico_equipes = bdd.get_equipes()
    lec='''<div class="card">
                <div class="card-header">
                    <div class="card-title">Liste des équipes</div>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="exampleFormControlSelect2">Id equipe - Nom equipe - Id avion</label>
                        <select multiple class="form-control" id="exampleFormControlSelect2">
                            '''+afficher_equipes(dico_equipes)+'''
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="comment">Membres de l'équipe</label>
                         <select multiple class="form-control" id="exampleFormControlSelect2">
                        </select>
                    </div>
                    <div class="card-action">
                        <button class="btn btn-success">Submit</button>
                        <button class="btn btn-danger">Cancel</button>
                    </div>
                </div>
            </div>'''
    return lec

def afficher_equipes(dico={}):
    html_code=""
    for id in dico:
        html_code+="<option>"+str(id)+" - "+dico[id]["nom"]+" - "+dico[id]["idAvion"]+"</option>"
    return html_code

def footer():
    f='''<footer class="footer">
            <div class="container-fluid">
                <nav class="pull-left">
                    <ul class="nav">
                        <li class="nav-item">
                            <a class="nav-link" href="http://www.themekita.com">
                                ThemeKita
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">
                                Help
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">
                                Licenses
                            </a>
                        </li>
                    </ul>
                </nav>
                <div class="copyright ml-auto">
                    2018, made with <i class="la la-heart heart text-danger"></i> by <a href="http://www.themekita.com">ThemeKita</a>
                </div>				
            </div>
        </footer>'''
    return f

def main_panel():
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Ajouter un membre ou une équipe</h4>
                                <div class="row">
                                    <div class="col-md-6">'''
    vmain_panel+=ajouter_membre_card()
    vmain_panel+=liste_membre_card()
    vmain_panel+='</div> <div class="col-md-6">'
    vmain_panel+=creer_equipe_card()
    vmain_panel+=liste_equipe_card()
    vmain_panel+='</div></div></div>'
    vmain_panel+=footer()
    vmain_panel+='</div></div>'
    return vmain_panel
