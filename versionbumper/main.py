import argparse
import os

class Version(object):

    def __init__(self, version_string):
        self.version = []
        if version_string:
            self.version = version_string.split(".")
        self._major = 0
        self._minor = 0
        self._patch = 0

    @property
    def version_string(self):
        return ".".join([str(self.major), str(self.minor), str(self.patch)])

    @property
    def major(self):
        if not self._major and len(self.version) > 0:
            self._major = int(self.version[0])
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    @property
    def minor(self):
        if not self._minor and len(self.version) > 1:
            self._minor = int(self.version[1])
        return self._minor

    @minor.setter
    def minor(self, value):
        self._minor = value

    @property
    def patch(self):
        if not self._patch and len(self.version) > 2:
            self._patch = int(self.version[2])
        return self._patch

    @patch.setter
    def patch(self, value):
        self._patch = value


def read_version(versionfile):
    with open(versionfile) as f:
        version = f.read().strip()
    return version


def write_version(versionfile, version_string):
    with open(versionfile, "w") as f:
        f.write(version_string)


def bump_version(versionfile, bump):
    version = read_version(versionfile)
    v = Version(version)
    setattr(v, args.version_bump, getattr(v, args.version_bump) + 1)
    write_version(versionfile, v.version_string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("versionfile",
                        help="File containing version string.")
    parser.add_argument("version_bump",
                        help="Bump major, minor or patch version.",
                        choices=['major', 'minor', 'patch'])
    args = parser.parse_args()
    bump_version(args.versionfile, args.version_bump)
