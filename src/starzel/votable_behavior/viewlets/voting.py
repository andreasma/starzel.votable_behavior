# encoding=utf-8
from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.permissions import ViewManagementScreens
from plone.app.layout.viewlets import common as base
from plone.app.layout.viewlets import interfaces as viewletIFs
from starzel.votable_behavior.interfaces import IVotable, IVoting


class Vote(base.ViewletBase):

    @property
    def _vote(self):
        return IVoting(self.context)

    @property
    def _membership_tool(self):
        return getToolByName(self.context, 'portal_membership')

    @property
    def voted(self):
        return self._vote.already_voted(self.request)

    @property
    def average(self):
        return self._vote.average_vote()

    @property
    def is_manager(self):
        return self._membership_tool.checkPermission(ViewManagementScreens,
                                                     self.context)

    @property
    def has_votes(self):
        return self._vote.has_votes()
