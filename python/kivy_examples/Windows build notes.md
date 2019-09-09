# Windows build notes

Read more notes at the official: [https://kivy.org/doc/stable/guide/packaging-windows.html](https://kivy.org/doc/stable/guide/packaging-windows.html)

## PyInstaller notes

### Include SDL and glew DLLs

To use PyInstaller to get a properly built package with the right DLLs,
modify the PyInstaller `.spec` file to have at the top:

```python
from kivy_deps import sdl2, glew
```

And in the `coll` object, after the last positional argument, add:

```python
*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
```

This will allow it to find and include the right dependencies since they are included in the code.
This helps with errors like 'unable to get window'.
