#!/usr/bin/env python


# Copyright 2016 RAPP

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Authors: Konstantinos Panayiotou
# contact: klpanagi@gmail.com


## @file Objects/File.py
#
#  @copyright Rapp Projecty EU 2016
#  @author Konstantinos Panayiotou, [klpanagi@gmail.com]
#

from RappCloud.Utils import RandStrGen
from os import path


class File(object):
    """ File object class """

    def __init__(self, filepath="", postfield=""):
        """! Constructor

        @param string path -The filepath
        @param string httpField - The post field name.
        """

        self.__boundarySize = 30
        self.__path = path.expanduser(path.realpath(filepath))
        if postfield is not "":
            self.__postfield = postfield
        else:
            self.__postfield = "file"


    def __eq__(self, other):
        """! Equality method """
        return self.serialize() == other.serialize()


    @property
    def path(self):
        """! file path getter

        @return string - The file path.
        """
        return self.__path


    @path.setter
    def path(self, path):
        """! file path setter

        @param path (String) - The file path.
        """
        self.__path = path


    @property
    def postfield(self):
        """! Post field name getter

        @return string - The post field name.
        """
        return self.__postfield


    @postfield.setter
    def postfield(self, fieldname):
        """! Post field name setter

        @param fieldname (String) - The post field name.
        """
        self.__postfield = fieldname


    def serialize(self):
        return {'path': self.__path, 'field_name': self.__postfield}


    def make_tuple(self):
        name = RandStrGen.create(self.__boundarySize)
        return (self.__postfield, (name, open(self.__path)))

