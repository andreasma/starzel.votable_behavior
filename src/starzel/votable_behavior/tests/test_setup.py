# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""
from starzel.votable_behavior.testing import STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestInstall(unittest.TestCase):
    """Test installation of starzel.votable_behavior into Plone."""

    layer = STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if starzel.votable_behavior is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('starzel.votable_behavior'))

    def test_uninstall(self):
        """Test if starzel.votable_behavior is cleanly uninstalled."""
        self.installer.uninstallProducts(['starzel.votable_behavior'])
        self.assertFalse(self.installer.isProductInstalled('starzel.votable_behavior'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IStarzelVotableBehaviorLayer is registered."""
        from starzel.votable_behavior.interfaces import IStarzelVotableBehaviorLayer
        from plone.browserlayer import utils
        self.assertIn(IStarzelVotableBehaviorLayer, utils.registered_layers())
