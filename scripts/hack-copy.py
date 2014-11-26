import itertools
import os
import re
import sys

SSH_CONFIG_FILE = '/home/saltycrane/.ssh/config'

def main():
    host1, path1 = sys.argv[1].split(':', 1)
    host2, path2 = sys.argv[2].split(':', 1)

    o = get_ssh_options(host2)
    keyfile_remote = '/tmp/%s' % os.path.basename(o['identityfile'])
    ssh_options = ' -o'.join(['='.join([k, v]) for k, v in o.iteritems()
                              if k != 'hostname' and k != 'identityfile'])

    run('scp %s %s:%s' % (o['identityfile'], host1, keyfile_remote))
    run('ssh %s scp -p -i %s -oStrictHostKeyChecking=no -o%s %s %s:%s' % (
            host1, keyfile_remote, ssh_options, path1, o['hostname'], path2))

def get_ssh_options(host):
    """Parse ~/.ssh/config file and return a dict of ssh options for host
    Note: dict keys are all lowercase
    """
    def remove_comment(line):
        return re.sub(r'#.*$', '', line)
    def get_value(line, key_arg):
        m = re.search(r'^\s*%s\s+(.+)\s*$' % key_arg, line, re.I)
        if m:
            return m.group(1)
        else:
            return ''
    def not_the_host(line):
        return get_value(line, 'Host') != host
    def not_a_host(line):
        return get_value(line, 'Host') == ''

    lines = [line.strip() for line in file(SSH_CONFIG_FILE)]
    comments_removed = [remove_comment(line) for line in lines]
    blanks_removed = [line for line in comments_removed if line]
    top_removed = list(itertools.dropwhile(not_the_host, blanks_removed))[1:]
    goodpart = itertools.takewhile(not_a_host, top_removed)
    return dict([line.lower().split(None, 1) for line in goodpart])

def run(cmd):
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    main()
