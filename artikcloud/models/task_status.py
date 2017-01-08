# coding: utf-8

"""
    ARTIK Cloud API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class TaskStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, num_attempts=None, error_message=None, error_code=None, did=None, status=None, ts=None):
        """
        TaskStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'num_attempts': 'int',
            'error_message': 'str',
            'error_code': 'str',
            'did': 'str',
            'status': 'str',
            'ts': 'int'
        }

        self.attribute_map = {
            'num_attempts': 'numAttempts',
            'error_message': 'errorMessage',
            'error_code': 'errorCode',
            'did': 'did',
            'status': 'status',
            'ts': 'ts'
        }

        self._num_attempts = num_attempts
        self._error_message = error_message
        self._error_code = error_code
        self._did = did
        self._status = status
        self._ts = ts

    @property
    def num_attempts(self):
        """
        Gets the num_attempts of this TaskStatus.
        Number of attempts

        :return: The num_attempts of this TaskStatus.
        :rtype: int
        """
        return self._num_attempts

    @num_attempts.setter
    def num_attempts(self, num_attempts):
        """
        Sets the num_attempts of this TaskStatus.
        Number of attempts

        :param num_attempts: The num_attempts of this TaskStatus.
        :type: int
        """

        self._num_attempts = num_attempts

    @property
    def error_message(self):
        """
        Gets the error_message of this TaskStatus.
        Error Message

        :return: The error_message of this TaskStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this TaskStatus.
        Error Message

        :param error_message: The error_message of this TaskStatus.
        :type: str
        """

        self._error_message = error_message

    @property
    def error_code(self):
        """
        Gets the error_code of this TaskStatus.
        Error Code

        :return: The error_code of this TaskStatus.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this TaskStatus.
        Error Code

        :param error_code: The error_code of this TaskStatus.
        :type: str
        """

        self._error_code = error_code

    @property
    def did(self):
        """
        Gets the did of this TaskStatus.
        Device ID

        :return: The did of this TaskStatus.
        :rtype: str
        """
        return self._did

    @did.setter
    def did(self, did):
        """
        Sets the did of this TaskStatus.
        Device ID

        :param did: The did of this TaskStatus.
        :type: str
        """

        self._did = did

    @property
    def status(self):
        """
        Gets the status of this TaskStatus.
        Status

        :return: The status of this TaskStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TaskStatus.
        Status

        :param status: The status of this TaskStatus.
        :type: str
        """

        self._status = status

    @property
    def ts(self):
        """
        Gets the ts of this TaskStatus.
        Timestamp of most recent status change

        :return: The ts of this TaskStatus.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this TaskStatus.
        Timestamp of most recent status change

        :param ts: The ts of this TaskStatus.
        :type: int
        """

        self._ts = ts

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
