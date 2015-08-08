#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################
# Tesla Control plugin for indigo
# Based on sample code that is:
# Copyright (c) 2014, Perceptive Automation, LLC. All rights reserved.
# http://www.indigodomo.com

import indigo
import teslajson


################################################################################
class Plugin(indigo.PluginBase):
	########################################
	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
		indigo.PluginBase.__init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
		self.vehicles = []
		self.debug = True

	def __del__(self):
		indigo.PluginBase.__del__(self)

	########################################
	def startup(self):
		# self.debugLog(u"startup called")
		self.debugLog("Username: %s" % self.pluginPrefs['username'])
		# TODO: exception handling
		connection = teslajson.Connection(self.pluginPrefs['username'],
										  self.pluginPrefs['password'])
		self.vehicles = connection.vehicles
		self.debugLog("%i vehicles found" % len(connection.vehicles))

	def shutdown(self):
		# self.debugLog(u"shutdown called")
		pass
	
	def carListGenerator(self, filter="", valuesDict=None, typeId="", targetId=0):
		# From the example above, filter = “stuff”
		# You can pass anything you want in the filter for any purpose
		# Create an array where each entry is a list - the first item is
		# the value attribute and last is the display string that will 
		# show up in the control. All parameters are read-only.
# 		myArray = [("option1", "First Option"),("option2","Second Option")]
# 		return myArray
		return [(str(v['id']), "%s (%s)" % (v['display_name'], v['vin'])) for v in self.vehicles]
