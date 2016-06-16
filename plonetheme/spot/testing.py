# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.spot


class PlonethemeSpotLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.spot)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.spot:default')


PLONETHEME_SPOT_FIXTURE = PlonethemeSpotLayer()


PLONETHEME_SPOT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_SPOT_FIXTURE,),
    name='PlonethemeSpotLayer:IntegrationTesting'
)


PLONETHEME_SPOT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_SPOT_FIXTURE,),
    name='PlonethemeSpotLayer:FunctionalTesting'
)


PLONETHEME_SPOT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_SPOT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeSpotLayer:AcceptanceTesting'
)
