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


class TasksStatusCounts(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cancelled=None, complete=None, processing=None, requested=None):
        """
        TasksStatusCounts - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cancelled': 'int',
            'complete': 'int',
            'processing': 'int',
            'requested': 'int'
        }

        self.attribute_map = {
            'cancelled': 'CANCELLED',
            'complete': 'COMPLETE',
            'processing': 'PROCESSING',
            'requested': 'REQUESTED'
        }

        self._cancelled = cancelled
        self._complete = complete
        self._processing = processing
        self._requested = requested

    @property
    def cancelled(self):
        """
        Gets the cancelled of this TasksStatusCounts.
        Cancelled

        :return: The cancelled of this TasksStatusCounts.
        :rtype: int
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """
        Sets the cancelled of this TasksStatusCounts.
        Cancelled

        :param cancelled: The cancelled of this TasksStatusCounts.
        :type: int
        """

        self._cancelled = cancelled

    @property
    def complete(self):
        """
        Gets the complete of this TasksStatusCounts.
        Complete

        :return: The complete of this TasksStatusCounts.
        :rtype: int
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """
        Sets the complete of this TasksStatusCounts.
        Complete

        :param complete: The complete of this TasksStatusCounts.
        :type: int
        """

        self._complete = complete

    @property
    def processing(self):
        """
        Gets the processing of this TasksStatusCounts.
        Processing

        :return: The processing of this TasksStatusCounts.
        :rtype: int
        """
        return self._processing

    @processing.setter
    def processing(self, processing):
        """
        Sets the processing of this TasksStatusCounts.
        Processing

        :param processing: The processing of this TasksStatusCounts.
        :type: int
        """

        self._processing = processing

    @property
    def requested(self):
        """
        Gets the requested of this TasksStatusCounts.
        Requested

        :return: The requested of this TasksStatusCounts.
        :rtype: int
        """
        return self._requested

    @requested.setter
    def requested(self, requested):
        """
        Sets the requested of this TasksStatusCounts.
        Requested

        :param requested: The requested of this TasksStatusCounts.
        :type: int
        """

        self._requested = requested

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
