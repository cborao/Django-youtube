"""Views for YouTube app
"""
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token

from .ytchannel import YTChannel
from . import data


def id_info(request, video_id):
    html1 = ""

    if len(data.selected) == 0:
        html1 = """
                <h2><b>List with selected items is empty. Go back and add content:</b></h2>
                <a href='/'>Go back</a>
                """

    for video in data.selected:
        if video['id'] == video_id:
            html1 = data.VIDEO_INFO.format(link=video['link'],
                                           title=video['title'],
                                           channel=data.channel['channel_url'],
                                           name=data.channel['channel_name'],
                                           img_url=video['img_url'],
                                           img_type=video['img_type'],
                                           img_width=video['img_width'],
                                           img_height=video['img_height'],
                                           date=video['date'],
                                           description=video['description'])

            break

        html1 = """
        <h2><b>This video is not in selected list. Go back and add it:</b></h2>
        <a href='/'>Go back</a>
        """

    return HttpResponse(html1)


def build_html(name, list, action, token):

    html = ""
    for video in list:
        html = html + data.VIDEO.format(video_id=video['id'],
                                        title=video['title'],
                                        id=video['id'],
                                        name=name,
                                        action=action,
                                        token=token)
    return html


def move_video(from_list, to_list, id):

    found = None
    for i, video in enumerate(from_list):
        if video['id'] == id:
            found = from_list.pop(i)
    if found:
        to_list.append(found)


def main(request):

    if request.method == 'POST':
        if 'id' in request.POST:
            if request.POST.get('select'):
                move_video(from_list=data.selectable,
                           to_list=data.selected,
                           id=request.POST['id'])
            elif request.POST.get('deselect'):
                move_video(from_list=data.selected,
                           to_list=data.selectable,
                           id=request.POST['id'])
    csrf_token = get_token(request)
    selected = build_html(name='deselect', list=data.selected,
                          action='Deselect', token=csrf_token)
    selectable = build_html(name='select', list=data.selectable,
                            action='Select', token=csrf_token)

    htmlBody = data.PAGE.format(selected=selected,
                                selectable=selectable)
    return HttpResponse(htmlBody)
