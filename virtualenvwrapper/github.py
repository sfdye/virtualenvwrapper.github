import logging
import os
import subprocess

log = logging.getLogger(__name__)


def run(*args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    p.wait()
    return p


def get_url(project):
    """Return the URL for the given project.
    """
    p = run('git', 'config', '--global', 'github.user')
    try:
        user = tuple(p.stdout)[0].strip()
    except (TypeError, IndexError):
        user = os.environ.get('VIRTUALENVWRAPPER_GITHUB_USER', os.environ.get('USER'))
    if not user:
        log.error('Set USER or VIRTUALENVWRAPPER_GITHUB_USER')
        return None
    url = 'git@github.com:{user}/{project}.git'.format(user=user, project=project)
    return url


def template(args):
    project, project_dir = args
    url = get_url(project)
    url = get_url(project)
    outdir = os.path.join(project_dir, project)
    if url:
        log.info('Cloning %s', url)
        subprocess.call(['git', 'clone', url, outdir], shell=False)
    return 

