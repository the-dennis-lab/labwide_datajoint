import datajoint as dj

from element_lab import lab
from element_animal import subject
from element_session import session

from element_animal.subject import Subject

if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix','')

__all__ = ['session','Subject','Lab','Protocol','User','Project',
           'ProjectKeywords','ProjectPublication','ProjectSourceCode',
           'ProjectUser','Session','SessionDirectory','SessionExperimenter',
           'SessionNote','ProjectSession']

lab.activate(db_prefix + 'lab')

subject.activate(db_prefix + 'subject', linking_module=__name__)

Experimenter = lab.User
session.activate(db_prefix + 'session', linking_module = __name__)
