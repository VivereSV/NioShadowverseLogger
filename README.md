# NioShadowverseLogger
An automatic match logger for Shadowverse. Just start it up before your no life ladder session and you're good to go!


## What does it do?
Nio helps you keep track of your Shadowverse matches by allowing quick and easy logging. Nio will write your class, your opponent's class, who went first, and who won to a log file. And you don't even have to do anything after you start it! To exit, just hit ctrl c on the command prompt/terminal.


## Okay, what's the catch?
The catch is that Nio only supports 2 resolutions if you download it straight from here: 1280x800 and 1920x1080 (1080p). Therefore, if you want to use Nio, you have 2 options. 

The first is just to change your resolution to one of the supported ones. If you do, open config.txt in the resources folder and make sure that the first line in it is your chosen resolution (don't touch the False). Afterwards, make sure full screen is disabled in Shadowverse. 

The second is to keep your resolution at whatever jank numbers you have it at and do a little leg work to make Nio work. All you have to do is take a look inside the resources folder, check one of the default resolution folders, and take 20 screenshots similar to what is in those folders, create a new folder with the name being your resolution and put the screenshots you've taken (with the same names as those in the other folders) into the new folder. Don't forget to edit config.txt afterwards. The second option will take around 15-20 minutes (I suggest conceding to the solo practice AI to get the screenshots).

Also it only works with text on english. If you do not play with text on english, you will need to replace the 1st.png and 2nd.png files in your chosen resolution.


## Important note about screenshots
If you do decide to take your own screenshots and think that you would like to help that other poor soul playing on 782x451 resolution, you can message the folder that you created as a zip file to VLV#5047 and I will add it to the user made folders sections. 


## Quick note to Mac users

Firstly, you will probably not be able to run nio_mac right away because it is from an unidentified developer (according to Apple anyways). To resolve that, double click the executable, go to System Preferences, go to Security & Privacy, and allow nio_mac to be run.

Secondly, the config file contains one extra line, which is False by default. If, and only if, you are using a Mac with retina display (ie Macbook Pro), you need to change that to True. You also need to check and make sure that your resolution is "Default for display". If you are using retina display and are having issues, please message VLV#5047 because I'm honestly kind of bamboozled by Apple here. Also worthy to note that if you do decide to take your own screenshots, that line needs to be False. 

Also, if you want to use the supported 1152x720, you need to have a retina display and have the config line be False. Don't ask.


## What can I do with this data?
If you would like to contribute your data to the public pool, simply head over to the [Team Dawnbreakers Discord server](https://discord.gg/BjeFkVS), ask one of the moderators for a "Data Logger" role, and send a message in the #data_log channel in the proper format (covered in next section). While we understand that rank does not always correlate to skill, we ask that you also attach a screenshot of your Shadowverse profile and be rank A and above.

All messages sent to SAlter will be recorded and should we find that you are submitting fraudulent data or abusing the function, you will receive one warning before being banned.


## Okay, so about that format?
Simply submit it like so:
+data;(copy paste of the log.txt file found in resources)

See the example below:

![example](https://i.imgur.com/KVIB0Kv.png)


## What will be done with the data?
Every week, Team Dawnbreakers will post the data on r/Shadowverse along with some analysis. If you have any other ideas or suggestions, feel free to message VLV#5047 on Discord.


## I'm in, sign me up!
Follow these links to download Nio!

[OSX](http://www.mediafire.com/file/nylloktb5hd3cbd/nio_mac.zip/file)

[Windows](http://www.mediafire.com/file/88n2xgfc873z689/nio_windows.zip/file)

Linux: As of now, there is no Linux version of Nio. If you use Linux and are interested in helping, please message VLV#5047.


## User made folders
Listed below are image folders kindly supplied by other users.

N/A


## List of confirmed issues

N/A


# FAQ

## Is this against the TOS?

I mean it's just continuously taking pictures of your screen, so it's pretty much a shitty twitch stream with an audience of 0. It does not modify SV in any way, nor does it inject anything. It does not monitor or interfere with any data being sent to or from the servers. Mostly because I'm too much of a monkey to figure out how to do that. Final answer: I'm not aware of any reason for why this would be violating the TOS, and yes, I did read it.


## It's not working???
If you are experiencing technical difficulties, please inform VLV#5047. Please provide as much detail as you can about the issues that you are having. One great trick is to open the terminal/command prompt, drag the executable file into it, hit enter, and take a screenshot of the output.

Common errors are: incorrect resolution, playing in full screen, covering up parts of the SV window, and not have your config file set properly. 


## Where are my data files??
Check the resources folder. Each log is dated in the format month-day-year-log.txt. 


## How are the data files formatted?
If you're just curious or if you want to make your own program to parse it (feel free to do so by the way), the format is: (your class) (opponent class) (true if you went first, false otherwise) (true if you won, false otherwise). Without the parentheses of course. 


## Does this track deck archetypes?

As of now, it does not. However, that is indeed one of the future goals. Soon TM omegaLUL.


## Hey, can you make it do ____?

If you have any feedback, feel free to message VLV#5047. Please keep in mind that it is very likely that your suggestion will not be implemented in the near future for a variety of reasons. Mostly because I'm really bad at python.


## Hey man you sure this isn't a virus?
Haha you sure caught me I was just about to steal that tier 0 homebrew deck with 25 8 drops that you just made. No of course it's not a virus. The source code is included in this repository. Even if you don't trust that, you can trust that I'm too shitty of a programmer to make a virus after you see it. If you're absolutely paranoid, you can just build the executable yourself from the .py file supplied here with pyinstaller.


## Wow man you're so cool how can I ever repay your broke college student ass
[Pay me with real money](https://www.paypal.me/vlvsv)


# Special thanks to...
FaceTorched#5219 for making the Windows distribution, bugtesting, and giving suggestions. If it were not for him, this would be an OSX only application omegaLUL. Feel free to send him pictures of french fries with no explanation.

HSK PancakeReaper for his advice on which screens to take and control suggestions. And saving me from going down a path that would have taken a lot more time and probably not worked.

DB Praetorian for being the first to wonder "why isn't this working"?

DB Blum, DB xninebreaker, DB meladog, HSK Szerro, DB Gouletateur2, and TO 5x2=9 for testing the windows version.

HSK Bravehood for the bugtesting and getting the screenshots for 1080p. 

SE | TK Dubski for the OSX testing and Macbook Air testing.

DB randomystery for suffering through my caps lock spam and getting the 1280x800 images. 

Rhekar for shaming me into making this fully automatic.

And of course, ~~my guinea pigs~~ Team Dawnbreakers for all their support.

