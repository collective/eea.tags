""" ControlPanel Interfaces
"""
from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('eea')


class IEEATagsSettings(Interface):
    """Global tags settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    tags_links = schema.Bool(title=_(u"Enable Links out of tags keywords"),
                 description=_(u"help_tags_links",
                 default=u"If enabled the tags found in the body text "
                             "will be wrapped with a predefined link"),
                 required=True,
                 default=False,)

    tags_link = schema.TextLine(title=_(u"Tags Link URL"),
                description=_(u"help_tags_link_url",
                            default=u"Enter the URL where the added links "
                                        "will point to"),
                required=False,
                default=u'',)
