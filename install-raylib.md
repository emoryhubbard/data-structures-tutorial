# Problems installing Raylib?

Raylib is basic graphics library available for Python. Follow these basic troubleshooting steps if anything goes wrong. If any commands don't work, that's the time to fix those commands first. You may need to add them to your path or update your installations (like Python or pip).

## Easy Method

Install Raylib on your machine like this:

	py -m pip install raylib

## Use different command
"py" command can be different based on OS and python version.
Python supports keeping old command names to support older versions,
and even python commands with old version numbers on the end if
configured by the user. Python3 generally should work.
If your python version is greater than 3, you can
replace "python" with "py" in your commands
if you like.

Also, depending on your OS, the command could be python3, python, py.

## Check Python version

If the above doesn't work, check Python version.

    py --version

Python 3.8.0 or newer should be good enough.

## Upgrade Python.

You can upgrade python by redownloading and reinstalling from
Python's official site.

## Check PIP version

If the above doesn't work, check PIP version.

    pip -V

## Upgrade PIP

    py -m pip install --upgrade pip

## NOT to be confused Pyray LIBRARY

Pyray is a module commonly used from the Raylib library.
However, there is a Pyray LIBRARY, not module, which exists
which can cause confusion. You do not need the Pyray LIBRARY.
You do not need to install Pandas.
Some sources, like this, reccommend, installing pandas, through
something like "pip install pandas". https://www.roseindia.net/answers/viewqa/pythonquestions/195193-ModuleNotFoundError-No-module-named-pyray.html
The issue is that you generally want the Pyray MODULE from
the Raylib Library which is completely different.

## SSL connection error

This is appeared to be some kind of VPN-related error to my friend.
It also shortly precipitated, or came shortly after, failure of
his computer to connect to his wifi. It is possible to
install the needed library even when the computer is offline or
averse to using pip, manually without the automatic pip tool.

Build from source:

    Build from source manually.

Get Homebrew or development libs as mentioned here:

    https://pypi.org/project/raylib/
    
Follow steps in these links:

    https://electronstudio.github.io/raylib-python-cffi/BUILDING.html
    https://electronstudio.github.io/raylib-python-cffi/README.html#installation
    https://www.raylib.com/
    https://stackoverflow.com/questions/13596505/python-command-not-working-in-command-prompt

## Pyray module not found

Also See Exit code 1.
Even if you are sure you have it installed,
it might be that you are running it outside of the terminal.
Code runner extension runs outside of terminal by default so
you can try

    py main.py (or whatever your program file is)

## Exit code: 1

python setup.py bdist_wheel did not run successfully.
The problem may be your platform is unsupported.

    "On most platforms it should install a binary wheel
    (Windows 10 x64, MacOS 10.15 x64, Linux Ubuntu1804 x64).
    
    If yours isn't available then pip will attempt to build from
    source, in which case you will need to have Raylib development
    libs installed, e.g. using homebrew, apt, etc." https://pypi.org/project/raylib/

This happens with Mac M1 (that is, an M1-based Mac that uses the
Apple M1 Max chip), as it did for my friend who had one:
https://www.codeproject.com/Questions/5325132/Installing-and-using-raylib-in-macos-12-2-1-with-P

Error message thrown when this happens:

    0 eastonpulver@Eastons-MacBook-Air cse210-04 % python3 -m pip install raylib Collecting raylib Using cached raylib-4.2.1.2.tar.gz (69 kB) Preparing metadata (setup.py) ... done Requirement already satisfied: cffi>=1.14.6 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from raylib) (1. 15.0) Requirement already satisfied: inflection in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from raylib) (0.5. 1) Requirement already satisfied: pycparser in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from cffi>=1.14.6-> raylib) (2.21) Building wheels for collected packages: raylib Building wheel for raylib (setup.py) ... error error: subprocess-exited-with-error 
    x python setup.py bdist_wheel did not run successfully. 1 exit code: 1 L-> [74 lines of output] not windows, trying Unix build 
    *************** WARNING *************** 
    I 
    /opt/local/include/raygui.h not found. Build will not contain these extra functions. 
    Please copy file from src/extras to /opt/local/include/raygui.h if you want them. 
    ************************************** 
    *************** WARNING *************** 
    /opt/local/include/physac.h not found. Build will not contain these extra functions. 
    Please copy file from src/extras to /opt/local/include/physac.h if you want them.

And so on... with similar warning messages.

You can try building from the source. See SSL connection error for more links to install manually, build from source manually, or build from source automatically.