import urllib.request

from django.apps import AppConfig
from .ytchannel import YTChannel
from . import data


class YouTubeConfig(AppConfig):
    name = 'youtube'

    def ready(self):
        url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' \
            + 'UC300utwSVAYOoRLEqmsprfg'
        xmlStream = urllib.request.urlopen(url)
        channel = YTChannel(xmlStream)
        data.selectable, data.channel = channel.videos()
