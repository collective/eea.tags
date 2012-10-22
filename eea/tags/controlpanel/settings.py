""" EEATags Settings Module
"""
from plone.app.registry.browser import controlpanel

from eea.tags.controlpanel.interfaces import IEEATagsSettings, _


class EEATagsSettingsEditForm(controlpanel.RegistryEditForm):
    """ ControlPanel RegistryEditForm
    """

    schema = IEEATagsSettings
    label = _(u"EEA Tags settings")

    def updateFields(self):
        """ Update Fields
        """
        super(EEATagsSettingsEditForm, self).updateFields()
        

    def updateWidgets(self):
        """ Update Widgets
        """
        super(EEATagsSettingsEditForm, self).updateWidgets()

class EEATagsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """ ControlPanel FormWrapper
    """
    form = EEATagsSettingsEditForm
