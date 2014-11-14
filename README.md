Aeroo Reports for OpenERP / Odoo 8.0
====================================

Parts of Aeroo Reports
----------------------

Aeroo Reports is splitted into three Odoo plugins:

- **report_aeroo:** The main Aeroo Reports Module
- **report_aeroo_ooo:** Module for OpenOffice Integration of Aeroo Reports
- **report_aeroo_sample:** Sample Report for testing the Aeroo Reports

These plugins are available as separate git repositories for direct usage. 
Here are the specified repositories:

- https://github.com/jamotion/report_aeroo.git
- https://github.com/jamotion/report_aeroo_ooo.git
- https://github.com/jamotion/report_aeroo_sample.git

Installation instructions
-------------------------

### Install required packages

    sudo apt-get install libreoffice python-genshi python-cairo python-lxml python-setuptools
    sudo apt-get install libreoffice-script-provider-python
    easy_install uno
    
### Install aeroolib

    git clone https://github.com/jamotion/aeroolib.git
    cd aeroolib
    python setup.py install
    
Please check the official documentation for further informations on Aeroo Reports Installation
(see http://www.alistek.com/wiki/index.php/Aeroo_Reports_Linux_server).

### Download and install depending modules
    
    git clone https://github.com/jamotion/base_field_serialized
    
Because of Odoo has removed the field type "serialized" the above plugin is needed to reimplement this field type.

### Install Aeroo Reports    
Instead of downloading the official aeroo modules (bzr branch https://launchpad.net/aeroo) please use these Repositories:

    cd /your/addons/dir/
    git clone https://github.com/jamotion/report_aeroo.git
    git clone https://github.com/jamotion/report_aeroo_ooo.git
    git clone https://github.com/jamotion/report_aeroo_sample.git

Warning!
--------

There is no warranty for this modules. We have upgraded Aeroo Reports for our own requirements and customers and it is working there. But we haven't tested it powerful. So please be careful when using it!
