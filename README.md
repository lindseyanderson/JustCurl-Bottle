JustCurl - Virtual host creation script for Apache
================================

[JustCurl](http://justcurl.com/) - currently exists as a combination of Bottle and BASH

This is an automated script for virtual host creation in Apache. 

Features
-------------------------
* Apache Virtual Host creation

To Do
-------------------------
* MySQL Database creation
* MongoDB Database creation
* Wordpress installation
* Drupal installation

Usage 
-------------------------

    bash  <( curl -H "host: example.com" \
        -H "x-port: 80" \
        -H "x-docroot: /var/www/vhosts/example.com" \
        justcurl.com )

Defaults
-------------------------

A host header must always be specified when attempting a virtual host installation.  The following are default values for the remaining headers:

* x-port:    80
* x-docroot: /var/www/vhosts/{{host}}

License
-------------------------

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Contact
-------------------------

Email: lindsey.anderson@rackspace.com
