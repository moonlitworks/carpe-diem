# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):
    add "images/frame.png"

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:

            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("display", "window")
                textbutton _("Fullscreen"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("transitions", "all")
                textbutton _("None"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("skip", "seen")
                textbutton _("All Messages"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("after choices", "stop")
                textbutton _("Keep Skipping"):
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Preference("after choices", "skip")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Language")
                textbutton "{font=DejaVuSans.ttf}English{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language(None)
                textbutton "{font=DejaVuSans.ttf}Español{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("spanish")
                textbutton "{font=DejaVuSans.ttf}Bahasa{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("bahasa")
                textbutton "{font=DejaVuSans.ttf}Deutsch{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("german")
                textbutton "{font=DejaVuSans.ttf}Français{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("french")
                textbutton "{font=DejaVuSans.ttf}Italiano{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("italian")
                textbutton "{font=DejaVuSans.ttf}Polski{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("polish")
                textbutton "{font=DejaVuSans.ttf}Português-Brasil{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("brazilian")
                textbutton "{font=DejaVuSans.ttf}ру́сский{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("russian")
                textbutton "{font=DejaVuSans.ttf}Svenska{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("swedish")
                textbutton "{font=SeoulNamsanM.ttf}한국말{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("korean")
                textbutton "{font=simsun.ttc}日本語{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("japanese")
                textbutton "{font=EkkamaiStandard-Light.ttf}ไทย{/font}":
                    text_color "#fff"
                    text_selected_color "#fff"
                    background None
                    hover_background "#6A88BE"
                    selected_background "#345083"
                    action Language("thai")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"


init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        thumb None
        left_bar "images/GUI/bar_full.png"
        right_bar "images/GUI/bar_empty.png"
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:

    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)
        xsize 902
        ysize 47


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

style mm_textbutton:
    color "#ffffff"
    hover_color "#345083"
    size 40
    background None

screen main_menu():
    tag menu
    window:
        background "#b7d1f2"
        style "mm_root"
    frame:
        background None
        vbox:
            imagebutton:
                focus_mask True
                idle "title-ai-hide.png"
                action None

    frame:
        xpos .66
        ypos .33
        xalign .0
        yalign .0
        background None

        vbox:
            spacing 50

            textbutton _("{font=Xolonium.ttf}START{/font}"):
                background None
                xalign .5
                text_style "mm_textbutton"
                action Start()

            textbutton _("{font=Xolonium.ttf}PREFERENCES{/font}"):
                background None
                xalign .5
                text_style "mm_textbutton"
                action ShowMenu("preferences")

            textbutton _("{font=Xolonium.ttf}QUIT{/font}"):
                background None
                xalign .5
                text_style "mm_textbutton"
                action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        background None
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return"):
            text_color "#fff"
            background None
            selected_background "#345083"
            hover_background "#6A88BE"
            action Return()
        textbutton _("Preferences"):
            text_color "#fff"
            background None
            selected_background "#345083"
            hover_background "#6A88BE"
            action ShowMenu("preferences")
        textbutton _("Quick Save"):
            text_color "#fff"
            background None
            selected_background "#345083"
            hover_background "#6A88BE"
            action QuickSave()
        textbutton _("Quick Load"):
            text_color "#fff"
            background None
            selected_background "#345083"
            hover_background "#6A88BE"
            action QuickLoad()
        textbutton _("Main Menu"):
            text_color "#fff"
            background None
            selected_background "#345083"
            hover_background "#6A88BE"
            action MainMenu()
        textbutton _("Quit"):
            text_color "#fff"
            background None
            selected_background "#345083"
            hover_background "#6A88BE"
            action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    frame:
        style_group "yesno"

        background "#345083"

        xfill True
        xmargin .05
        ypos .5
        yalign .5
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes"):
                text_color "#fff"
                background None
                hover_background "#b7d1f2"
                action yes_action

            textbutton _("No"):
                text_color "#fff"
                background None
                hover_background "#b7d1f2"
                action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign .5
        yalign 0.0

        textbutton _("Home") action MainMenu()
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 10

    style quick_button_text:
        is default
        size 18
        idle_color "#9E9E9E"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

screen choose_date():
    fixed:
        hbox:
            xpos .5
            ypos .6
            xalign .5
            yalign .5
            spacing 50

            vbox:
                button:
                    xsize 200
                    ysize 200
                    background im.Scale("icons/mall.png",200,200)
                    hover_background im.Scale("icons/mall-hover.png",200,200)
                    text _("Mall") color "#345083" xalign .5 yalign .7
                    action Call("menu1")

            vbox:
                button:
                    xsize 200
                    ysize 200
                    background im.Scale("icons/park.png",200,200)
                    hover_background im.Scale("icons/park-hover.png",200,200)
                    text _("Park") color "#345083" xalign .5 yalign .7
                    action Call("menu2")

            vbox:
                button:
                    xsize 200
                    ysize 200
                    background im.Scale("icons/arcade.png",200,200)
                    hover_background im.Scale("icons/arcade-hover.png",200,200)
                    text _("Arcade") color "#345083" xalign .5 yalign .7
                    action Call("menu3")
