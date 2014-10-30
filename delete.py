def delete( filename , critical=False ):
"""This module deletes a file within the local OS and reports if that fails"""
    import os
    try:
        os.remove( filename )
    except:
        "Could not delete : "+filename
        if critical:
            print "Cannot continue. Exiting."
            sys.exit(1)
