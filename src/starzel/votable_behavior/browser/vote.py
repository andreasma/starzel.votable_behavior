from Products.Five.browser import BrowserView
from starzel.votable_behavior.interfaces import IVotable
from starzel.votable_behavior.interfaces import IVoting

class Vote(BrowserView):
    def __call__(self, rating=None):
        if rating is None:
            raise KeyError('None is not a valid rating')

        voting = IVoting(self.context)
        voting.vote(rating, self.request)
        return 'success'

class ClearVotes(BrowserView):
    def __call__(self):
        voting = IVoting(self.context)
        voting.clear()
        return 'sucess'
