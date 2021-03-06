# coding: utf-8

"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dfirtrackapi_client.configuration import Configuration


class Company(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'company_id': 'int',
        'company_name': 'str',
        'division': 'int'
    }

    attribute_map = {
        'company_id': 'company_id',
        'company_name': 'company_name',
        'division': 'division'
    }

    def __init__(self, company_id=None, company_name=None, division=None, local_vars_configuration=None):  # noqa: E501
        """Company - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company_id = None
        self._company_name = None
        self._division = None
        self.discriminator = None

        if company_id is not None:
            self.company_id = company_id
        self.company_name = company_name
        self.division = division

    @property
    def company_id(self):
        """Gets the company_id of this Company.  # noqa: E501


        :return: The company_id of this Company.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this Company.


        :param company_id: The company_id of this Company.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this Company.  # noqa: E501


        :return: The company_name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Company.


        :param company_name: The company_name of this Company.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and company_name is None:  # noqa: E501
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) > 50):
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `50`")  # noqa: E501

        self._company_name = company_name

    @property
    def division(self):
        """Gets the division of this Company.  # noqa: E501


        :return: The division of this Company.  # noqa: E501
        :rtype: int
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this Company.


        :param division: The division of this Company.  # noqa: E501
        :type: int
        """

        self._division = division

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Company):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Company):
            return True

        return self.to_dict() != other.to_dict()
