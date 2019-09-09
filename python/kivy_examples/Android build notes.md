# Kivy Android Build Notes

Use `buildozer` to build Android `.apk` files.

Official usage instructions at [https://buildozer.readthedocs.io/en/latest/quickstart.html](https://buildozer.readthedocs.io/en/latest/quickstart.html)

My sample project with live stream:
[https://github.com/DevDungeon/KivyBitcoinPriceChecker](https://github.com/DevDungeon/KivyBitcoinPriceChecker)

## Install buildozer

Intall buildozer package:

```bash
python3 -m pip install buildozer
```

Cython will also be needed:

```bash
dnf install python3-Cython
```

On Fedora, I needed to install `ncurses-compat-libs` to resolve the error:
`$HOME/.buildozer/android/platform/android-ndk-r17c/toolchains/llvm/prebuilt/linux-x86_64/bin/clang: error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory`.

```bash
dnf install ncurses-compat-libs
```

In Ubuntu, others report similar: https://github.com/kivy/buildozer/issues/841

```bash
# Ubuntu fixes
sudo apt-get install libncurses5-dev libncursesw5-dev
sudo apt-get install libtinfo5
```

## Initializer a buildozer spec file

```bash
python3 -m buildozer init
```

Read more about the options at [https://buildozer.readthedocs.io/en/latest/specifications.html](https://buildozer.readthedocs.io/en/latest/specifications.html)

### Change allowed orientations

Default orientation is portrait (tall) mode only. Change it to `all` in the spec file.

### Change icon

In the spec file, set the `icon.filename` setting to a PNG image 512x512.

### Change splash image

In the spec file, set the `presplash.filename` to a PNG/JPG 512x512.

## Build

NOTE: Always run the first build with verbose mode (`-v`) otherwise
you won't see the prompt to accept the EULA to install the tools.

```bash
# Build debug
python3 -m buildozer -v android debug
# Build release (requires signing?) https://github.com/kivy/kivy/wiki/Creating-a-Release-APK
python3 -m buildozer -v android release
```

## Use adb to list devices

You can run `adb` from the SDK like this:

```bash
python3 -m buildozer -v android adb
```

I had some trouble using it that way however, so you can invoke it directly at:

```bash
$HOME/.buildozer/android/platform/android-sdk/platform-tools/adb
```

## Install

NOTE: To deploy and run, you need TCP connectivity so you can't do it from a VM behind a NAT.
Use a bridged network connection.

```bash
python3 -m buildozer -v android deploy
```

## Run

```bash
python3 -m buildozer -v android run
```

## Build, deploy, and run in one step

```bash
python3 -m buildozer -v android debug deploy run
```

## View logs

```bash
buildozer -v android logcat
```



