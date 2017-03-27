try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser
import os

def find_config_file(project):
    """\
    Find config files in this order:

        ~/.project/project.conf
        ~/project.conf
        /etc/project/project.conf
        /etc/project.conf

    :param project:
    :return: config file path
    """
    config_dir = [os.path.expanduser(os.path.join('~', '.' + project)),
                  os.path.expanduser(os.path.join('~')),
                  os.path.join('/etc', project),
                  '/etc']

    for d in config_dir:
        file_path = os.path.join(d, project + '.conf')
        if os.path.isfile(file_path):
            return file_path


CONF = RawConfigParser()
CONF.read(find_config_file('example'))