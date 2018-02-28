# webpreview

Installation
----
*Will make it ```pip``` installable*
```bash
git clone https://github.com/sdushantha/webpreview.git
```

Example usage
----
```python
import webpreview

# returns a desktop preview of the website [179x320 pixles]
webpreview.desktop("https://www.github.com", filename="image1.jpg")

# returns a mobile preview of the website [568x320 pixles]
webpreview.mobile("https://www.github.com", filename="image2.jpg")
```

Limititations
----
- Image width is 320px
- Web fonts can prove tricky
- There's no way to pass authentication or cookie data, so you just get the "public" view of the page.
- Plugins like Flash and Java may not work.
- Complex JavaScript pages won't always work.
- It's a bit slow to generate the image.
- Only one rendering, so you can't use it to see how Firefox compares to Chrome.
