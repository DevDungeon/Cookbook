```bash
# Build mypkg directory in to .deb package
dpkg -b ./mypkg ./mypkg_1.0.0-0_amd64.deb

# Naming format: <name>_<version>-<release>_<arch>.deb
# Version is the version number of the app being packaged
# Release number is the version number of the *packaging* itself.
# The release number might increment if the package maintainer
# updated the packaging, while the version number of the application
# being packaged did not change.

# Inspect information like size, version, dependencies
dpkg -I mypkg.deb
```