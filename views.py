import bottle 

from bottle import route
from bottle import run
from bottle import request
from bottle import template


@route('/')
def index():  
    base_directory = "/var/www/vhosts/"

    data = {}
    data['host']      = request.headers.get('HOST').lower()
    data['directory'] = request.headers.get('X-DOCROOT').lower()
    data['port']      = request.headers.get('X-PORT', "80")
    
    if data['host'].startswith("www."):
        data['host'] = data.get(host).replace("www.", "")

    if not data['directory']:
        data['directory'] = base_directory + data['host']

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
