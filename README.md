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

# returns a desktop preview of the website [179x320]
webpreview.desktop("https://www.hackerone.com", filename="image1.jpg")

# returns a mobile preview of the website [568x320]
webpreview.mobile("https://www.hackerone.com", filename="image2.jpg")
```
Example preview
----
**Desktop [179x320]**

![img1](https://user-images.githubusercontent.com/27065646/36830391-bf6aa646-1d23-11e8-994f-266bfd75d4e8.jpg "Desktop")

**Mobile [568x320]**

![img2](https://user-images.githubusercontent.com/27065646/36830450-effb5d8c-1d23-11e8-8887-56ce78178ce9.jpg "mobile")

Limititations
----
- Image width is 320px
- Web fonts can prove tricky
- There's no way to pass authentication or cookie data, so you just get the "public" view of the page.
- Plugins like Flash and Java may not work.
- Complex JavaScript pages won't always work.
- It's a bit slow to generate the image.
- Only one rendering, so you can't use it to see how Firefox compares to Chrome.
