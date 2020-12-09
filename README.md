# Log-Analysis
A log analysis using regular expressions in Python to extract certain information in order to create meaningful reports.

The log is contained in the syslog.log file, which contains logs related to ticky company. 

The log lines follow a pattern similar to the ones we've seen before. Something like this:

    May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)

    Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)

When the service runs correctly, it logs an INFO message to syslog. It then states what it did and states the username and ticket number related to the event. If the service encounters a problem, it logs an ERROR message to syslog. This error message indicates what was wrong and states the username that triggered the action that caused the problem.

In this section, we'll search and view different types of error messages. The error messages for ticky details the problems with the file with a timestamp for when each problem occurred.

These are a few kinds of listed error:

    Timeout while retrieving information
    The ticket was modified while updating
    Connection to DB failed
    Tried to add information to a closed ticket
    Permission denied while closing ticket
    Ticket doesn't exist
