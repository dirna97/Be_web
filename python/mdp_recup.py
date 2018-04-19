conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
chemin=conf.chemin()

def index():
    result = '''  <!DOCTYPE html>
                <html lang="en">
                <head>
                    <title>CB-Récupération</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                <!--===============================================================================================-->	
                    <link rel="icon" type="image/png" href="''' + chemin + '''/login/images/icons/favicon.ico"/>
                <!--===============================================================================================-->
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/vendor/bootstrap/css/bootstrap.min.css">
                <!--===============================================================================================-->
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
                <!--===============================================================================================-->
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/vendor/animate/animate.css">
                <!--===============================================================================================-->	
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/vendor/css-hamburgers/hamburgers.min.css">
                <!--===============================================================================================-->
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/vendor/select2/select2.min.css">
                <!--===============================================================================================-->
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/css/util.css">
                    <link rel="stylesheet" type="text/css" href="''' + chemin + '''/login/css/main.css">
                <!--===============================================================================================-->
                </head>
                <body>
                    
                    <div class="limiter">
                        <div class="container-login100">
                            <div class="wrap-login100">
                                <div class="login100-pic js-tilt" data-tilt>
                                    <img src="''' + chemin + '''/login/images/img-01.png" alt="IMG">
                                </div>
                
                                <form class="login100-form validate-form">
                                    <span class="login100-form-title">
                                        Récupération de votre mot de passe
                                    </span>
                
                                    <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                                        <input class="input100" type="text" name="idEquipage" placeholder="Email">
                                        <span class="focus-input100"></span>
                                        <span class="symbol-input100">
                                            <i class="fa fa-envelope" aria-hidden="true"></i>
                                        </span>
                                    </div>					
                                    <div class="container-login100-form-btn">
                                        <a href="#" class="login100-form-btn">
                                            Envoyer 
                                        </a>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    
                    
                
                    
                <!--===============================================================================================-->	
                    <script src="''' + chemin + '''/login/vendor/jquery/jquery-3.2.1.min.js"></script>
                <!--===============================================================================================-->
                    <script src="''' + chemin + '''/login/vendor/bootstrap/js/popper.js"></script>
                    <script src="''' + chemin + '''/login/vendor/bootstrap/js/bootstrap.min.js"></script>
                <!--===============================================================================================-->
                    <script src="''' + chemin + '''/login/vendor/select2/select2.min.js"></script>
                <!--===============================================================================================-->
                    <script src="''' + chemin + '''/login/vendor/tilt/tilt.jquery.min.js"></script>
                    <script >
                        $('.js-tilt').tilt({
                            scale: 1.1
                        })
                    </script>
                <!--===============================================================================================-->
                    <script src="''' + chemin + '''/login/js/main.js"></script>
                
                </body>'''
    return result
