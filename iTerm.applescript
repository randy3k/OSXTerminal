on appIsRunning(appName)
    tell application "System Events" to (name of processes) contains appName
end appIsRunning

on urldecode(URLpath)
    set URLpath to do shell script "x=" & quoted form of URLpath & ";x=${x/#file:\\/\\/};x=${x/#localhost}; printf ${x//%/\\\\x}"
    return URLpath
end urldecode

on pwd_tty(tty_name)
    -- Based on http://genbastechthoughts.wordpress.com/2012/07/10/how-to-duplicate-an-iterm-tab-using-applescript/
    set pid to do shell script ("ps -f | grep " & tty_name & " | grep 'zsh\\|bash' | head -n 1 | awk '{ print $2; }'")
    set ret to do shell script ("lsof -a -d cwd -F n -p " & pid & " | grep ^n | awk '{ sub(/^n/, \"\"); print; }'")
    return ret
end pwd_tty

on run argv
    set thefolder to item 1 of argv & "/"
    set detected to false
    --display dialog thefolder

    if my appIsRunning("iTerm2") then
        tell application "iTerm"
            repeat with w in windows
                if (count of (tabs of w)) is 0 then
                    exit repeat
                end if
                set s to w's current tab's current session
                set thetitle to get name of s
                set tty_name to do shell script "basename " & (get tty of s)
                set working_dir to my pwd_tty(tty_name)
                if working_dir & "/" is thefolder and (thetitle contains "bash" or thetitle contains "zsh") then
                    set detected to true
                    exit repeat
                end if
            end repeat
        end tell
    end if

    if detected then
        tell application "System Events"
            tell process "iTerm2"
                set frontmost to true
                perform action "AXRaise" of (first window whose title is thetitle)
            end tell
        end tell
        tell application "iTerm" to activate
    else
        tell application "iTerm"
            open thefolder
            activate
        end tell
    end if
end run
