import bottle 

from bottle import route
from bottle import run
from bottle import request
from bottle import template


@route('/')
def index():  
    data = {}
    data['host']      = request.headers.get('HOST')
    data['directory'] = request.headers.get('X-DOCROOT')
    data['port']      = request.headers.get('X-PORT')

    return template("vhost_installer.template",
           data = data )

@route('/get_debian')
@route('/get_ubuntu')
def get_debian():
    return template("apache_debian_vhost.template")

@route('/get_rhel')
@route('/get_cent')
def get_rhel():
    return template("apache_redhat_vhost.template")

bottle.TEMPLATE_PATH.insert(0,'/var/www/vhosts/catchall/templates/')

run(host='0.0.0.0', port=8080, debug=True)
