# coding: utf-8

"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dfirtrackapi_client
from dfirtrackapi_client.models.contact import Contact  # noqa: E501
from dfirtrackapi_client.rest import ApiException

class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Contact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dfirtrackapi_client.models.contact.Contact()  # noqa: E501
        if include_optional :
            return Contact(
                contact_id = 56, 
                contact_name = '0', 
                contact_email = '0', 
                contact_phone = '0'
            )
        else :
            return Contact(
                contact_name = '0',
                contact_email = '0',
        )

    def testContact(self):
        """Test Contact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()