#!/usr/bin/python

"""
Shared configuration-level variables.
"""

from glob import glob
import os
import os.path

debian_releases = ['squeeze', 'wheezy']
ubuntu_releases = ['precise', 'quantal', 'raring', 'saucy']
releases = debian_releases + ubuntu_releases

debian_tags = { 'squeeze' : '6.0', 'wheezy' : '7.0', 'jessie' : '8.0~0.1' }
ubuntu_tags = { 'precise' : '12.04', 'quantal' : '12.10', 'raring' : '13.04', 'saucy' : '13.10' }

package_search_paths = ['athena/*', 'debathena/*', 'third/*']
package_root = os.environ['DEBATHENA_CHECKOUT_HOME']

package_paths = [ os.path.join(package_root, path) for path in package_search_paths ]
package_paths = sum(map(glob, package_paths), [])
package_map = { path.split('/')[-1] : path for path in package_paths }

arches = ['i386', 'amd64', 'armel', 'armhf', 'sparc']
builders = {
    'i386' : 'local',
    'amd64' : 'local',
    'armel' : 'hecatoncheires.mit.edu',
    'armhf' : 'hecatoncheires.mit.edu',
    'sparc' : 'package-fusion.mit.edu',
}
def arch_for_release(arch, release):
    "Check if we build the specified arch for given suite."

    # We currently don't have the infrastructure for others
    return arch == 'i386' or arch == 'amd64'

source_package_dir = os.environ['DEBATHENA_SOURCE_DIR']
orig_tarball_dir = os.environ['DEBATHENA_ORIG_DIR']
apt_root_dir = '/mit/debathena/apt'

release_tag_key = "0D8A9E8F"
