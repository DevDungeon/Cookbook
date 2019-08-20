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

## Initializer a buildozer spec file

```bash
python3 -m buildozer init
```

## Build

```bash
# Build debug
python3 -m buildozer --verbose android debug
# Build release
python3 -m buildozer --verbose android release
```

## Install

```bash
# Install to device
python3 -m buildozer --verbose android deploy
```
