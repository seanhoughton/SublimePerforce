import sublime, sublime_plugin
import os, stat


class PerforceCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		fileToCheckout = view.file_name()
		if fileToCheckout != None:
			fileMode = os.stat(fileToCheckout)[stat.ST_MODE]
			if (not fileMode & stat.S_IWRITE):
				cmd = "p4 edit " + fileToCheckout
				workingDir = os.path.dirname(fileToCheckout)
				oldDir = os.getcwd()
				os.chdir(workingDir)
				output = os.popen(cmd).read()
				os.chdir(oldDir)
				print output;
