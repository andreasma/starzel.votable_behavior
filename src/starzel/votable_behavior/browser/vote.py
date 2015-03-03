from Products.Five.browser import BrowserView
from starzel.votable_behavior.interfaces import IVotable
from starzel.votable_behavior.interfaces import IVoting
from zope.event import notify


class Vote(BrowserView):
    def __call__(self, rating=None):
        if rating is None:
            raise KeyError('None is not a valid rating')

        voting = IVoting(self.context)
        voting.vote(rating, self.request)
        notify(ObjectModifiedEvent(self.context, "A vote has been submitted"))
        return 'success'

class ClearVotes(BrowserView):
    def __call__(self):
        voting = IVoting(self.context)
        voting.clear()
        notify(ObjectModifiedEvent(self.context,
                                   "All votes have been removed"))
        return 'sucess'
