template = Import('template.py')
conf = Import('../data/config.py')
chemin = conf.chemin()


def index():
    if "nom" in COOKIE:
        result = template.entete(chemin,'CB-Classement')
        result += template.main_header(chemin)
        result += template.sidebar(3, chemin,COOKIE["admin"].value)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


def main_panel():
    vmain_panel = '''
    <div class="main-panel">
        <div class="content">
            <div class="container-fluid">
                <h4 class="page-title">Classement</h4>
                <div class="row">
                    <div class="col-md-12">
                        
                        <div class="card">
                            <div class="card-header">
                                <div class="card-title">Classement par équipes</div>
                            </div>
                            <div class="card-body">
                                <table class="table table-head-bg-primary mt-4">
                                    <thead>
                                        <tr>
                                            <th scope="col">#</th>
                                            <th scope="col">Equipe</th>
                                            <th scope="col">Posés décollés</th>
                                            <th scope="col">Distance franchie</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>ENAC</td>
                                            <td>31</td>
                                            <td>461</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                            <td>Airbus Industries</td>
                                            <td>28</td>
                                            <td>455</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                            <td colspan="1">Supaéro</td>
                                            <td>19</td>
                                            <td>358</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    '''
    return vmain_panel
