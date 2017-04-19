import sublime
import sublime_plugin
import os
import subprocess


class OpenOsxItermCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_timeout_async(self.run_async)

    def run_async(self):
        view = self.view
        window = view.window()
        file = view.file_name()
        thefolder = None
        if file:
            thefolder = os.path.dirname(file)
        else:
            pd = window.project_data()
            if pd and "folders" in pd and len(pd["folders"]) > 0:
                project_path = pd["folders"][0].get("path")
                if project_path:
                    thefolder = project_path

        if thefolder:
            thefolder = os.path.realpath(thefolder)
            script = sublime.load_resource(
                        "Packages/OSXTerminal/iTerm.applescript")
            p = subprocess.Popen(['osascript', '-e', script, thefolder],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            if stderr:
                print(stderr)
