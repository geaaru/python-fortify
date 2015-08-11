# -*- coding: utf-8 -*-
'''
fortify.fpr
~~~~~~~~~~~

'''
from .utils import openfpr


class FPR(object):
    def __init__(self, project, **kwargs):
        if isinstance(project, basestring):
            self._project = project = openfpr(project)
        elif isinstance(project, dict):
            self._project = project
        else:
            raise TypeError

        self.FVDL = project['audit.fvdl'].getroot()
        self.Audit = project['audit.xml'].getroot()
        self.FilterTemplate=None

        if 'filtertemplate.xml' in project:
            self.FilterTemplate = project['filtertemplate.xml'].getroot()

        self.ExternalMetadata=None
        if 'externalmetadata.xml' in project:
            self.ExternalMetadata = project['externalmetadata.xml'].getroot()
