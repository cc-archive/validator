"""Pylons environment configuration"""
import os

from pylons import config

import validator.lib.app_globals as app_globals
import validator.lib.helpers
from validator.config.routing import make_map

def load_environment(global_conf, app_conf):
    """Configure the Pylons environment via the ``pylons.config``
    object
    """
    # Pylons paths
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths = dict(root=root,
                 controllers=os.path.join(root, 'controllers'),
                 static_files=os.path.join(root, 'public'),
                 templates=[os.path.join(root, 'templates')])

    # Initialize config with the basic options
    config.init_app(global_conf, app_conf, package='validator',
                    template_engine='genshi', paths=paths)

    config['routes.map'] = make_map()
    config['pylons.g'] = app_globals.Globals()
    config['pylons.h'] = validator.lib.helpers
    
    # Customize templating options via this variable
    tmpl_options = config['buffet.template_options']
    tmpl_options['genshi.default_doctype'] = 'xhtml'
    tmpl_options['genshi.default_encoding'] = 'utf-8'
    tmpl_options['genshi.default_format'] = 'xhtml'    

    # CONFIGURATION OPTIONS HERE (note: all config options will override
    # any Pylons config options)
