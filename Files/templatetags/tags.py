from django import template

register = template.Library()

def file(f):
    l = f.get_name().split('.')
    if len(l) == 2:
        n = l[0]
        t = l[1]
    else:
        t = l[len(l) - 1]
        n = f.get_name()[0:len(f.get_name())-4]
    size = f.file.size / 1024
    
    if size > 1000:
        s = f'{round(size / 1024)}mb' 
    else: s = f'{round(size)}kb'
    if t == 'mp4':
        return f'''
    <b class='fa fa-file-video-o'> {n} {s}</b>
    <button class='fa fa-download'></button>
    '''
    if t == 'mp3':
        return f'''
    <b class='fa fa-file-audio-o'> {n} {s}</b>
    <button class='fa fa-download'></button>
    '''
    if t == 'png'or t == 'jpg':
        return f'''
    <b class='fa fa-file-image-o'> {n} {s}</b>
    <button class='fa fa-download'></button>
    '''
    if t == 'pdf':
        return f'''
    <b class='fa fa-file-pdf-o'> {n} {s}</b>
    <button class='fa fa-download'></button>
    '''
    
    return f'''<b>{n} {s}</b>'''

register.filter('file', file)