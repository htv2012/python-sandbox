import logging

logfile = 'suspense.log'
logging.basicConfig(filename=logfile, filemode='w',
                    level=numlevel,
                    format='%(asctime)s - %(levelname)s - %(name)s:%(funcName)s - %(message)s')
