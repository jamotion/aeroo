Aeroo Reports for OpenERP / Odoo 8.0
====================================

This Repository contains the following OpenERP / Odoo Plugins:
--------------------------------------------------------------

- **report_aeroo:** The main Aeroo Reports Module
- **report_aeroo_ooo:** Module for OpenOffice Integration of Aeroo Reports
- **report_aeroo_sample:** Sample Report for testing the Aeroo Reports

These plugins are available as separate git repositories for direct usage without copying. All of them are included into this repository as subtree's.

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
    
Please check the official documentation for Aeroo Reports Installation
(see http://www.alistek.com/wiki/index.php/Aeroo_Reports_Linux_server).

### Download depending modules
    
    git clone https://github.com/Sandwych/equinox.git
    
    
Instead of downloading the official aeroo modules (bzr branch https://launchpad.net/aeroo) please use this git repository (git clone https://github.com/jamotion/aeroo.git)


Warning!
--------

There is no warranty for this modules. We have upgraded Aeroo Reports for our own requirements and customers and it is working there. But we haven't tested it powerful. So please be careful when using it!
