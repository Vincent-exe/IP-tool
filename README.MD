# IP INFO TOOL
#### Video Demo:  <URL HERE>
#### Description:

This program is a tool that provides information about IPv4 addresses
that is inspired by the time when I learned networking and would look
up a bunch of different tools instead of having it all in one place.

By default the program launches with all functions enabled:

1. ip_class
    - returns what class the IP is in
2. boundary
    - returns if the IP is an internal or external network
3. binary
    - converts IP octets to binary format
4. hex
    - converts IP octets to hexidecimal format
 5. octal
    - converts IP octets to octal format

The user can enable or disable all by entering _"enable/disable all"_.
These functions can be toggled in selected batches by entering one
or more of the commands following _enable_ or _disable_. You can enter
_"help"_ to pull up a quick guide on how to use the program while it's
running. Entering _exit_ will also close the program, among other similar terms.
The program runs continously until the user terminates the program using _"exit"_.

project.py is the main program file.

test_project.py is a test file using pytest.

requirements.txt covers what needs to be done in order to run this program.
No pip installs required.

guide.txt is printed to the terminal upon launching the program and whenever
the user enters _"help"_ providing guidance on how to use the program.

Future updates will include more functions as I find more things to add.
I tried including a Whois lookup but it slowed the program down.