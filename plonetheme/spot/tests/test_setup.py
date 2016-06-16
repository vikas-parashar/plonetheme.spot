# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.spot.testing import PLONETHEME_SPOT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.spot is properly installed."""

    layer = PLONETHEME_SPOT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.spot is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.spot'))

    def test_browserlayer(self):
        """Test that IPlonethemeSpotLayer is registered."""
        from plonetheme.spot.interfaces import (
            IPlonethemeSpotLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeSpotLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_SPOT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.spot'])

    def test_product_uninstalled(self):
        """Test if plonetheme.spot is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.spot'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeSpotLayer is removed."""
        from plonetheme.spot.interfaces import IPlonethemeSpotLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeSpotLayer, utils.registered_layers())
