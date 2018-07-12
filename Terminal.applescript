on appIsRunning(appName)
	tell application "System Events" to (name of processes) contains appName
end appIsRunning

on urldecode(URLpath)
	set URLpath to do shell script "x=" & quoted form of URLpath & ";x=${x/#file:\\/\\/};x=${x/#localhost}; printf ${x//%/\\\\x}"
	return URLpath
end urldecode

on run argv
	set detected to false
	set thefolder to item 1 of argv & "/"

	if my appIsRunning("Terminal") then
		tell application "System Events" to tell process "Terminal"
			repeat with w in windows
				try
					set thetitle to name of w
					set termfolder to my urldecode(value of attribute "AXDocument" of w)
					if termfolder is thefolder and (thetitle contains "bash" or thetitle contains "zsh") then
						set detected to true
						perform action "AXRaise" of w
						exit repeat
					end if
				end try
			end repeat
		end tell
	end if

	if not detected then
		do shell script "open -a terminal " & quoted form of thefolder
	end if
end run
