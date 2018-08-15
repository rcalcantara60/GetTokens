import cherrypy

config = {
  'global' : {
    'server.socket_host' : 'site1.mydomain.com',
    'server.socket_port' : 8099,
    'server.thread_pool' : 8
  },
}

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
            return """<html>
          <head>
            <script src='https://www.google.com/recaptcha/api.js?render=6LduKmoUAAAAAE8SL0TkV2INpWX1BHcXpa0AiwWc'></script>
            <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="  crossorigin="anonymous"></script>
            <script>
            var len = 50;
            var i = 0;
            
            function chamar()
            {
                //var animate = function(){
                    setTimeout(function () {                    
                        grecaptcha.execute('6LduKmoUAAAAAE8SL0TkV2INpWX1BHcXpa0AiwWc', {action: 'action_name'})
                                .then(function(token) {
                                    $.post( "post_token", { token: token}, function(data) {
                                            $(".result").html(data);
                                    });
                        });                    
                        if (i++ < len) chamar();
                    }, 1000);
                //};
            }
            </script>
          </head>
          <body>
            <p class='result'></p>
            <button onclick=chamar()>Teste</button>
          </body>
        </html>"""
    @cherrypy.expose
    def post_token(self, token):
        file=open("tokens.txt","a")        
        file.writelines(token + "\n")
        file.close()
        return token



if __name__ == '__main__':
  cherrypy.quickstart(HelloWorld(), '/', config)
