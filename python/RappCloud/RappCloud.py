#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright 2015 RAPP

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Authors: Konstantinos Panayiotou, Manos Tsardoulias
# contact: klpanagi@gmail.com, etsardou@iti.gr


## @file RappCloud/RappCloud.py
#
#  @copyright Rapp Projecty EU 2015
#  @author Konstantinos Panayiotou, [klpanagi@gmail.com]
#

import json
import os
import sys
import yaml
import base64

from ServiceController import ServiceControllerSync
from RandStrGen import RandStrGen
from Utils import Net
#import magic

__path__ = os.path.dirname(__file__)


## @class RappCloud
#
#  Rapp Platform API class. API calls for Platform HOP Web Services.
#
class RappCloud(object):

    ##  Default constructor.
    def __init__(self):
        self.__randStrSize = 5
        self.serviceController = ServiceControllerSync()



    ## Append a random string as a postFix to the input filePath.
    #
    #  @param self The object pointer.
    #  @param filePath File's system path to append the random postfix string.
    #
    #  @return The new file name.
    #
    def __appendRandStr(self, filePath):
        randStr = RandStrGen.create(self.__randStrSize)
        splStr = filePath.split('/')
        splStr = splStr[len(splStr) - 1].split('.')
        newName = splStr[0] + '-' + randStr + '.' + splStr[1]
        return newName


    ## API call for Speech-Detection-Sphinx4 RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param language Language to be used by the speech_detection_sphinx4
    #    module. Currently valid language values are ‘gr’ for Greek and
    #    ‘en’ for English.
    #  @param audio_source A value that presents the information for the
    #    audio source data. e.g "nao_wav_1_ch".
    #  @param words A vector that carries the "under-detection" words.
    #  @param sentences The under consideration sentences.
    #  @param grammar Grammar to be used.
    #  @param file_uri Path to the audio/speech file to be given as input
    #    to the speech_detection_sphinx4 Platform Service.
    #
    #  @return Rapp Platform Service response object.
    #
    def speech_detection_sphinx4(self, language, audio_source, words, \
                                 sentences, grammar, filepath):
        # -- Craft the data payload for the post request
        payload = {
            'language': language,
            'audio_source': audio_source,
            'words': words,
            'sentences': sentences,
            'grammar': grammar
        }

        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'speech_detection_sphinx4', payload, files)
        return returnData


    ## API call for Speech-Detection-Google RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param language Language to be used by the speech_detection_sphinx4
    #    module. Currently valid language values are ‘gr’ for Greek and
    #    ‘en’ for English.
    #  @param audio_source A value that presents the information for the
    #    audio source data. e.g "nao_wav_1_ch".
    #  @param file_uri Path to the audio/speech file to be given as input
    #    to the speech_detection_google Platform Service.
    #
    #  @return Rapp Platform Service response object.
    #
    def speech_detection_google(self, filepath, audio_source, language):
        # -- Craft the data payload for the post request
        payload = {
            'audio_source': audio_source,
            'language': language
        }

        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'speech_detection_google', payload, files)
        return returnData


    ## API call for Set-Noise-Profile RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param audio_source A value that presents the information for the
    #    audio source data. e.g "nao_wav_1_ch".
    #  @param file_uri Path to the audio/speech file to be given as input
    #    to the speech_detection_google Platform Service.
    #
    #  @return Rapp Platform Service response object.
    #
    def set_noise_profile(self, filepath, audio_source):
        # -- Craft the data payload for the post request
        payload = {
            'audio_source': audio_source
        }
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'set_noise_profile', payload, files)
        return returnData


    ## API call for Qr-Detection RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param file_uri Path to the image file to be given as input
    #    to the qr_detection Platform Service.
    #
    #  @return Rapp Platform Service response object.
    #
    def qr_detection(self, filepath):
        payload = {}
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'qr_detection', payload, files)
        return returnData


    ## API call for Human-Detection RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param file_uri Path to the image file to be given as input
    #    to the human_detection Platform Service.
    #
    #  @return Rapp Platform Service response object.
    #
    def human_detection(self, filepath):
        payload = {}
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'human_detection', payload, files)
        return returnData

    ## API call for Face-Detection RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param file_uri Path to the image file to be given as input
    #    to the face_detection Platform Service.
    #
    #  @return Rapp Platform Service response object.
    #
    def face_detection(self, filepath, fast = False):
        payload = {
            'fast': fast
        }
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'face_detection', payload, files)
        return returnData



    ## API call for Ontology-Subclasses-Of RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param query Ontology query string.
    #
    #  @return Rapp Platform Service response object.
    #
    def ontology_subclasses_of(self, query):
        payload = {
            'query': query,
        }
        files = []

        returnData = self.serviceController.run_job( \
                'ontology_subclasses_of', payload, files)
        return returnData


    ## API call for Ontology-Superclasses-Of RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param query Ontology query string.
    #
    #  @return Rapp Platform Service response object.
    #
    def ontology_superclasses_of(self, query):
        payload = {
            'query': query,
        }
        files = []

        returnData = self.serviceController.run_job( \
                'ontology_superclasses_of', payload, files)
        return returnData


    ## API call for Ontology-Subsuperclass-Of RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param parent_class Ontology parent class name.
    #  @param child_class Ontology child calss name.
    #  @param recursive Defines if a recursive procedure will be used (bool).
    #
    #  @return Rapp Platform Service response object.
    #
    def ontology_is_subsuperclass_of(self, parent_class, child_class, recursive):
        rec = False
        if recursive != None:
            rec = recursive

        payload = {
            'parent_class': parent_class,
            'child_class': child_class,
            'recursive': rec
        }
        files = []

        returnData = self.serviceController.run_job( \
                'ontology_is_subsuperclass_of', payload, files)
        return returnData


    ## API call for Ontology-Subsuperclass-Of RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #
    #  @return Rapp Platform Service response object.
    #
    def available_services(self):
        #  There seems to be an error with Hop-server on empty payload post
        #  requests. The use of the dummyVar into the payload field resolves
        #  the bug.
        #  TODO Report this bug to HOP developers/maintainers

        payload = {
            'dummyVar': ''
        }
        files = []

        returnData = self.serviceController.run_job( \
                'available_services', payload, files)
        return returnData


    ## API call for Text-To-Speech RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param text String to perform TTS on.
    #  @param language Supported translation language. 'el' -> Greek,
    #   'en' -> English.
    #  @param dest If provided the returned audio data will be stored in this
    #   destination file. Otherwise the audio data are returned as part of
    #   return object.
    #
    #  @return Rapp Platform Service API call response object.
    #
    def text_to_speech(self, text, language, dest):
        files = []
        payload = {
            'text': text,
            'language': language
        }

        response = self.serviceController.run_job( \
                'text_to_speech', payload, files)
        returnData = {}
        # Parse response error field.
        if response['error']:
            returnData['error'] = response['error']
            return returnData
        else:
            try:
                # Decode base64 encoded payload
                audioRawData = base64.b64decode(response['payload'])
            except Exception as e:
                returnData['error'] = 'Failed to base64.decode payload data'
                print e
                return returnData
            finally:
                pass
        returnData['error'] = ''
        # Parse dest parameter.
        if not dest:
            returnData['audioData'] = audioRawData
            returnData['basename'] = response['basename']
            #returnData['mime'] = magic.from_buffer(returnData['audioData'],
            #                                       mime=True)
        else:
            try:
                # Write audio data to given destination file path.
                with open(dest, 'wb') as f1:
                    f1.write(audioRawData)
            except Exception as e:
                returnData['error'] = \
                    'Failed to write data at destination file [%s]' % dest
            finally:
                pass
        return returnData



    # ======================= Cognitive Exercises ========================= #
    #=======================================================================#

    ## API call for Cognitive-Test-Chooser RAPP Platform front-end service.
    #
    #  @param self The object pointer.
    #  @param testType Cognitive Test Type. ArithmeticCts, AwarenessCts,
    #    ReasoningCts.
    #
    #  @return Rapp Platform Service API call response object.
    #
    def cognitive_test_chooser(self, testType):
        files = []
        payload = {
            'test_type': testType
        }

        returnData = self.serviceController.run_job( \
                'cognitive_test_chooser', payload, files)
        return returnData


    ## API call for Record-Cognitive-Test-Performance RAPP Platform
    #    front-end service
    #
    #  @param self The object pointer.
    #  @param test Test full name as obtained from a call to
    #    cognitive_test_chooser Platform service.
    #  @param score User's score for given test in range [0-100].
    #
    #  @return Rapp Platform Service API call response object.
    #
    def record_cognitive_test_performance(self, test, score):
        files = []
        payload = {
            'test_instance': test,
            'score': score
        }

        returnData = self.serviceController.run_job( \
                'cognitive_record_performance', payload, files)
        return returnData

    ## API call for cognitive-get-user-cores RAPP Platform
    #    front-end service
    #
    #  @param self The object pointer.
    #  @param upToTime the timestamp up to which scores will be calculated
    #
    #  @return Rapp Platform Service API call response object.
    #
    def cognitive_get_scores(self, upToTime, testType):
        files = []
        payload = {
            'up_to_time': upToTime,
            'test_type': testType
        }

        returnData = self.serviceController.run_job( \
                'cognitive_get_scores', payload, files)
        return returnData


    def user_personal_info(self):
        files = {}
        payload = {}

        returnData = self.serviceController.run_job( \
                'user_personal_info', payload, files)
        return returnData



    ## API call for cognitive-get-user-cores RAPP Platform
    #    front-end service
    #
    #  @param self The object pointer.
    #  @param upToTime the timestamp up to which scores will be calculated
    #
    #  @return Rapp Platform Service API call response object.
    #
    def cognitive_get_history(self, fromTime, toTime, testType):
        files = []
        payload = {
            'from_time': fromTime,
            'to_time': toTime,
            'test_type': testType
        }

        returnData = self.serviceController.run_job( \
                'cognitive_get_history', payload, files)
        return returnData


    ## API call for email-send RAPP Platform service
    #
    #  @param email
    #  @param passwd
    #  @param server
    #  @param port
    #  @param recipients
    #  @param body
    #  @param subject
    #  @param file_uri Can be a zip file!
    ##
    def send_email(self, email, passwd, server, port, recipients, body,\
            subject, filepath):
        payload = {
            'email': email,
            'passwd': passwd,
            'server': server,
            'port': port,
            'recipients': recipients,
            'body': body,
            'subject': subject
        }
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'email_send', payload, files)
        return returnData


    def email_fetch(self, email, passwd, server, port="", from_date=0, \
            to_date=10000000, email_status="", num_emails=25):
        payload = {
            'email': email,
            'passwd': passwd,
            'server': server,
            'port': port,
            'from_date': from_date,
            'to_date': to_date,
            'email_status': email_status,
            'num_emails': num_emails
        }

        resp = self.serviceController.run_job( \
                'email_fetch', payload, [])


        for i in range(0, len(resp['emails'])):
            for j in range(0, len(resp['emails'][i]['attachments'])):
                try:
                    # Decode base64 str to raw data
                    rawData = base64.b64decode( \
                            resp['emails'][i]['attachments'][j]['data'])

                    resp['emails'][i]['attachments'][j]['data'] = rawData
                except Exception as e:
                    print e
        return resp


    def news_stories_fetch(self, newsEngine='', keywords=[], excludeTitles=[], \
            region='', topic='', numNews=25):
        payload = {
            'news_engine': newsEngine,
            'keywords': keywords,
            'exclude_titles': excludeTitles,
            'region': region,
            'topic': topic,
            'num_news': numNews
        }

        returnData = self.serviceController.run_job( \
                'news_explore', payload, [])
        return returnData


    def geolocation(self, ipaddr='', engine=''):
        if ipaddr == '':
          ipaddr = Net.ipaddr_connected()

        payload = {
            'ipaddr': ipaddr,
            'engine': engine
        }

        returnData = self.serviceController.run_job('geolocation', payload, [])
        return returnData


    def weather_report_forecast(self, city, weatherReporter='', metric=0):
        payload = {
            'city': city,
            'weather_reporter': weatherReporter,
            'metric': metric
        }

        returnData = self.serviceController.run_job( \
                'weather_report_forecast', payload, [])
        return returnData


    def weather_report_current(self, city, weatherReporter='', metric=0):
        payload = {
            'city': city,
            'weather_reporter': weatherReporter,
            'metric': metric
        }

        returnData = self.serviceController.run_job( \
                'weather_report_current', payload, [])
        return returnData


    def object_recognition(self, filepath):
        payload = {}
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
                'object_recognition', payload, files)
        return returnData


    ##
    #   @brief Calls hazard_detection_light_check() RAPP Platform service.
    #   @return Return answer from RAPP Platform.
    ##
    def hazard_detection_light_check(self, filepath):
        payload = {}
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
            'hazard_detection_light_check', payload, files)

        return returnData


    ##
    #   @brief Calls hazard_detection_door_check() RAPP Platform  service.
    #   @return Return answer from RAPP Platform.
    ##
    def hazard_detection_door_check(self, filepath):
        payload = {}
        files = [{'path': filepath, 'field_name': 'file'}]

        returnData = self.serviceController.run_job( \
            'hazard_detection_door_check', payload, files)

        return returnData


    def path_planning_upload_map(self, pngFile, yamlFile, map_name):
        payload = {
          'map_name': map_name
        }
        files = [
            {'path': yamlFile, 'field_name': 'yaml_file'},
            {'path': pngFile, 'field_name': 'png_file'}
        ]

        response = self.serviceController.run_job( \
                'path_planning_upload_map', payload, files)
        return response


    def path_planning_plan_path_2d(self, map_name, robot_type, \
            algorithm, start, goal):
        payload = {
          'map_name': map_name,
          'robot_type': robot_type,
          'algorithm': algorithm,
          'start': start,
          'goal': goal
        }
        files = []

        response = self.serviceController.run_job( \
                'path_planning_plan_path_2d', payload, files)
        return response

