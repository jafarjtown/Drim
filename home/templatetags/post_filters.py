from django import template

register = template.Library()


def file_type(value):
    result = ''
    if len(value) == 2:
        result += '<div class="two_file">'
        for v in value:
            if v.file.url != '':
                ty = v.file.url.split('.')
                t = ty[-1].lower()
                musics = ['mp3']
                videos = ['mp4']
                pictures = ['png', 'jpg', 'jpeg']
                if t in musics:
                    result += f'<audio src="{v.file.url}" /></audio>'
                elif t in videos:
                    result += f'<video src="{v.file.url}" controls preload="metadata" class="post_video"/></video>'
                elif t in pictures:
                    result += f'<img src="{v.file.url}" loading="lazy"/></img>'
                else:
                    result += v.file.url
        result += '</div>'
    elif len(value) == 3:
        result += '<div class="three_file">'
        count = 0
        for v in value:
            count += 1
            if count == 2:
                result += '<div class="three_file_2">'
            if v.file.url != '':
                ty = v.file.url.split('.')
                t = ty[-1].lower()
                musics = ['mp3']
                videos = ['mp4','3gp']
                pictures = ['png', 'jpg', 'jpeg']
                if t in musics:
                    result += f'<audio src="{v.file.url}" /></audio>'
                elif t in videos:
                    result += f'<video src="{v.file.url}" controls preload="metadata" class="post_video"/></video>'
                elif t in pictures:
                    result += f'<img src="{v.file.url}" loading="lazy"/></img>'
                else:
                    result += v.file.url
        result += '</div></div>'
    elif len(value) > 3:
        result += '<div class="more_file">'
        count = 0
        for v in value:
            count += 1
            if count == 2:
                result += '<div class="three_file_2">'
            if count > 3:
                break
            if v.file.url != '':
                ty = v.file.url.split('.')
                t = ty[-1].lower()
                musics = ['mp3']
                videos = ['mp4','3gp']
                pictures = ['png', 'jpg', 'jpeg']
                if t in musics:
                    result += f'<audio src="{v.file.url}" /></audio>'
                elif t in videos:
                    result += f'<video src="{v.file.url}" controls preload="metadata" class="post_video"/></video>'
                elif t in pictures:
                    result += f'<img src="{v.file.url}" loading="lazy"/></img>'
                else:
                    result += v.file.url
        result += f'<div class="more_file_count">{value.count() - 3}</div></div></div>'
    else: 
        result += '<div class="one_file">'
        for v in value:
            if v.file.url != '':
                ty = v.file.url.split('.')
                t = ty[-1].lower()
                musics = ['mp3']
                videos = ['mp4']
                pictures = ['png', 'jpg', 'jpeg']
                if t in musics:
                    result += f'<audio src="{v.file.url}" /></audio>'
                elif t in videos:
                    result += f'''
                    <video id='video-{v.file.url}' controlsList="nofullscreen nodownload noremoteplayback noplay" preload="metadata" max-height="200" class="post_video"/>
                        <source src="{v.file.url}" />
                    </video>
                    <div class='video_controls'>
                        <button onclick='PlayVideo(this,"video-{v.file.url}")' class='fa fa-3x fa-play'></button>
                       
                    </div>
                    '''
                elif t in pictures:
                    result += f'<img src="{v.file.url}" loading="lazy"/></img>'
                else:
                    print(v.file)
                    result += f'<button onclick="saveFile({v.file.url},{v.file.url},'')">Download file</button>v.file.url'
        result += '</div>'
    return result
import re

def word(value):
    if value[0].startswith('http'):
        return f"<a href='{value[0]}' target='blank'>click link</a>"
    ky = value[0][0]
    vl = value[0][1:-1]
    if ky == '*':
        return f"<b class='filter_b'>{vl}</b>"
    elif ky == '`':
        return f"<code class='filter_code'>{vl}</code>"
    elif  ky == '\"':
        return f"<em class='filter_em'>{vl}</em>"
    elif  ky == ':':
        return f'<mark class="filter_mark" >{vl[1:-1]}</mark>'
    elif  ky == '-':
        return f'<del class="filter_del" >{vl}</del>'
    elif  ky == '~':
        return f'<strike class="filter_strike" >{vl}</strike>'
    else:
        return str(value[0])

def text_format(text):
    text = re.sub('http(.+)', word, text)
    text = re.sub('\*(.+)\*', word, text) #bold
    text = re.sub(r'\`\`\s?(.+)\`\`', word, text) #code
    text = re.sub('\"(.+)\"', word, text) #itali
    text = re.sub('\::(.+)\::', word, text) #mark
    text = re.sub('\~(.+)\~', word, text) #strike
    
    return text

register.filter('file_type', file_type)
register.filter('text_format', text_format)