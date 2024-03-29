from configparser import ConfigParser

def configParser(filename='database.ini', section='postgresql'):
        
    #Creates a parser
    parser = ConfigParser()
    #Read config file
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception('Section {0} does not exist in the {1} file'.format(section, filename))

    return db