#!/usr/bin/env python
# whatis: Retrieve IMAP message and extract attachment
from __future__ import print_function, unicode_literals
import argparse
import sys
import os
import getopt
import imaplib
import email
import mimetypes


def downloadInboxMessage(server, port, user, password, messageNumber):
    """
    Description:
        Logs into an IMAP server and retrieve a message from the inbox
    Parameters:
        server:        The name or IP of the IMAP server
        port:          Port to communicate with the IMAP server (143)
        user:          User name in the form DOMAIN/username
        password:      Passport to login
        messageNumber: the first message is the inbox is #1
    Return:
        A string representing the entire message
    Exception:
        We are not handling any exception throw, just propagage it to
        the caller
    """
    imap = imaplib.IMAP4(server, port)
    imap.login(user, password)
    imap.select()
    status, data = imap.fetch(messageNumber, '(RFC822)')
    messageText = data[0][1]
    return messageText


def getDefaultFilename(contentType, counter):
    if (contentType == 'text/plain'):
        ext = '.txt'
    else:
        ext = mimetypes.guess_extension(contentType)

    if not ext:
        ext = '.wav'

    filename = 'part-%03d%s' % (counter, ext)
    return filename


def saveAttachments(messageText, outputDir='.'):
    """
    Description:
        Givine a message, extract, decode, and save the attachmentsA to
        the file system. By default, attachments are saved to the
        current directory, unless overrided with the outputDir parameter.
    Paramters:
        message:   Text string that contains the whole message
        outputDir: Where to save the attachment, default to the current dir.
    Exception:
    """

    # Create the directory if necessary
    try:
        os.mkdir(outputDir)
    except:
        pass

    msg = email.message_from_string(messageText)
    counter = 1
    for part in msg.walk():
        # Multipart are just containers
        if part.get_content_maintype() == 'multipart':
            continue

        # Grab the filename
        filename = part.get_filename()

        # If we cannot retrieve the file name, make something up
        if not filename:
            filename = getDefaultFilename(part.get_content_type(),
                                          counter);

        # Add directory to the filename
        filename = os.path.join(outputDir, filename)
        print(">>>filename:%s<<<" % (filename))

        # Save the attachment
        outFile = open(filename, 'wb')
        outFile.write(part.get_payload(decode=True))
        outFile.close()

        # Advance to the next part
        counter += 1


def usage():
    """
    Displays the usage
    """
    scriptName = os.path.split(sys.argv[0])[1]
    print('\n%s -- download IMAP message, then decode the attachments' \
          % scriptName)
    print('\nUsage:')
    print('  %s [options]')
    print('\nOptions:')
    print('  -s, --server        <server name or IP>')
    print('  -t, --port          <port number>')
    print('  -u, --user          <user name>')
    print('  -p, -password       <login password>')
    print('  -m, -message-number <1, 2, .. last>')
    print('  -o, -output-dir     <where to save attachments to')
    print()


def get_arguments():
    """
    Parse the command line and return a argparse.Namespace object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('server', help='Server name or IP')
    parser.add_argument('port', help='Port number')
    parser.add_argument('user', help='Login user name')
    parser.add_argument('password', help='Login password')
    parser.add_argument('message_number', help='Message number')
    parser.add_argument(
            '-o', '--output-dir',
            default='.',
            help='Where to save attachment')
    arguments = parser.parse_args()
    return arguments


def main():
    """ Script Entry """
    arguments = get_arguments()
    try:
        msg = downloadInboxMessage(
                arguments.server,
                arguments.port,
                arguments.user,
                arguments.password,
                arguments.message_number)
        saveAttachments(msg, arguments.output_dir)
        return 0
    except Exception as exc:
        print(exc)
        return 1

if __name__ == '__main__':
    sys.exit(main())
