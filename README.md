# django-short-codes
## Wordpress like short codes support for Django.
Django doenst natively supports shortcodes like wordpress does so this app gives you the same behaviour. It currently supports youtube, vimeo, local hosted videos and images
## Usage
To use the short codes first include the app inside settings.py inside INSTALLED_APPS
```
INSTALLED_APPS = (
.......
'django-short-codes'
)
```
Please note that you will need to restart the server if you are running Apache or similar(not applicable for the development server)

To display it inside the content use it as bellow
```
 {{post|shortcodes|safe}}
```

On the admin site you can call your shortcode as follows
### Vimeo videos
>[vimeo video_id="http://link.to.vimeo.video" width="200" height="200"]
### YouTube videos
>[youtube id="http://youtube.com/video/link" width="200" height="200"]
### Local video files
>[video id="http://link.to.your.mp4.or.similar.video" width="200" height="200"]
### Local image files
>[img id="http://link.to.your.local.image"]
