# Manim Animation — Example

## Copy-paste

```python
from manim import *
class MyScene(Scene):
    def construct(self):
        tex = Tex("Hello").to_edge(UP)
        self.play(Write(tex))
```

## Expected Output

- Renders to `media/MyScene.mp4`
- Requires: `manim`, `ffmpeg`
