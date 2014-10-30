def process_cmd(command_line):
"""Attempts to execute a command, reports on fail"""
    import shlex,subprocess
    args=shlex.split(command_line)
    try:
        subprocess.call( args ) #tderr=subprocess.STDOUT , stdout=subprocess.PIPE )
    except:
        print "Python found error when trying to run:"
        print command_line
