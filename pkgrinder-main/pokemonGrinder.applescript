tell application "System Events"
    set texttosay to "Sample Text"
    set texttosay to {".route 11", "yanma", "skarmory", "corsola", "magby", "bayleef", "4", "3", "3", "y"}
    display dialog "Text to type:" default answer "white: "
    -- set texttosay to the text returned of the result
    repeat
        -- activate application "Safari"
        delay 5
        repeat
            repeat with i from 1 to length of texttosay
                keystroke item i of texttosay
                keystroke return
                delay 4.5
            end repeat
            -- keystroke texttosay
            -- delay 4
            -- keystroke return
        end repeat

        display dialog the "Do you want to quit?" buttons {"Continue", "Quit"} default button 1
        if the button returned of the result is "Quit" then
            exit repeat
        end if
    end repeat
end tell
