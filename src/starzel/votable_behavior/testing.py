# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import starzel.votable_behavior


class StarzelVotableBehaviorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            starzel.votable_behavior,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'starzel.votable_behavior:default')


STARZEL_VOTABLE_BEHAVIOR_FIXTURE = StarzelVotableBehaviorLayer()


STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(STARZEL_VOTABLE_BEHAVIOR_FIXTURE,),
    name='StarzelVotableBehaviorLayer:IntegrationTesting'
)


STARZEL_VOTABLE_BEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(STARZEL_VOTABLE_BEHAVIOR_FIXTURE,),
    name='StarzelVotableBehaviorLayer:FunctionalTesting'
)


STARZEL_VOTABLE_BEHAVIOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        STARZEL_VOTABLE_BEHAVIOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='StarzelVotableBehaviorLayer:AcceptanceTesting'
)
