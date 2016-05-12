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


## @file RappCloud/CloudServices/QrDetection.py
#
#  @copyright Rapp Projecty EU 2016
#  @author Konstantinos Panayiotou, [klpanagi@gmail.com]
#


from Service import *
from RappCloud.Objects import (
    File,
    Payload
    )


class QrDetection(Service):
  """ QrDetection Cloud Service class """

  def __init__(self, **kwargs):
    """!
    Constructor

    @param **kwargs - Keyword arguments. Apply values to the request attributes.
      - @ref image
    """

    # Cloud Service request arguments
    # -------------------------------------------------------------
    ## Path to the image file.
    self.image = ''
    # -------------------------------------------------------------

    super(QrDetection, self).__init__(
        svcname='qr_detection', **kwargs)


  def _make_payload(self):
    """ Make request payload object """
    return Payload()


  def _make_files(self):
    """ Create array of file object(s) """
    return [File(self.image, 'file')]