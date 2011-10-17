import sublime, sublime_plugin
import os, stat


class PerforceCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		fileToCheckout = view.file_name()
		if fileToCheckout != None:
			fileMode = os.stat(fileToCheckout)[stat.ST_MODE]
			if (not fileMode & stat.S_IWRITE):
				cmd = "p4 edit " + fileToCheckout
				output = os.popen(cmd).read()
				print output;
