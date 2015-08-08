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
		self.debug = True

	def __del__(self):
		indigo.PluginBase.__del__(self)

	########################################
	def startup(self):
		# self.debugLog(u"startup called")
		self.debugLog("Username: %s" % self.pluginPrefs['username'])
		pass

	def shutdown(self):
		# self.debugLog(u"shutdown called")
		pass
