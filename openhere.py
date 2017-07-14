import sublime
import sublime_plugin
import subprocess
import os


class FinderCommand:
    def _get_path(self):
        if self.window.active_view():
            file = self.window.active_view().file_name()
            if file:
                return file

        if self.window.folders():
            return self.window.folders()[0]

        pd = self.window.project_data()
        if pd and "folders" in pd and len(pd["folders"]) > 0:
            project_path = pd["folders"][0].get("path")
            if project_path:
                return project_path

        return os.path.expanduser("~")

    def get_path(self):
        return os.path.realpath(self._get_path())

    def execute_command(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if stderr:
            print(stderr)


class OpenFinderHereCommand(sublime_plugin.WindowCommand, FinderCommand):
    def run(self):
        sublime.set_timeout_async(self.run_async)

    def run_async(self):
        path = self.get_path()

        if os.path.isfile(path):
            cmd = ['open', '-R', path]
        else:
            cmd = ['open', path]

        self.execute_command(cmd)


class OpenTerminalHereCommand(sublime_plugin.WindowCommand, FinderCommand):
    def run(self):
        sublime.set_timeout_async(self.run_async)

    def run_async(self):
        path = self.get_path()
        if os.path.isfile(path):
            path = os.path.dirname(path)

        script = sublime.load_resource("Packages/OpenHere/Terminal.applescript")
        self.execute_command(['osascript', '-e', script, path])


class OpenItermHereCommand(sublime_plugin.WindowCommand, FinderCommand):
    def run(self):
        sublime.set_timeout_async(self.run_async)

    def run_async(self):
        path = self.get_path()
        if os.path.isfile(path):
            path = os.path.dirname(path)

        script = sublime.load_resource("Packages/OpenHere/iTerm.applescript")
        self.execute_command(['osascript', '-e', script, path])
