"""Fill the GenUP template with GEN29 content.

Usage: python3 build.py TEMPLATE.pptx OUT.pptx [images_dir]
Only text in the existing boxes is replaced; speaker script is appended to the
notes. If images_dir has 1.png..6.png (or .jpg), each is centre-cropped to the
picture slot ratio and swapped in for that slide's picture.
"""
import re, sys, os, shutil, zipfile, tempfile
from xml.sax.saxutils import escape
from content import TEAM, SLIDES

SLOT_RATIO = 5.75 / 3.9  # picture slot w/h on every slide

def set_text(xml, shape_name, text):
    # Keep numbers and their units on one line.
    text = re.sub(r'(\d) (?=\d{3}\b)', '\\1\u00a0', text)
    text = re.sub(r'(\d) (?=€)', '\\1\u00a0', text)
    m = re.search(r'<p:sp>(?:(?!</p:sp>).)*?name="%s".*?</p:sp>' % re.escape(shape_name), xml, re.S)
    assert m, shape_name
    sp = m.group(0)
    # Keep only the first run of the first paragraph; drop extra runs and paragraphs.
    first_p = re.search(r'<a:p>.*?</a:p>', sp, re.S).group(0)
    run = re.search(r'<a:r>.*?</a:r>', first_p, re.S).group(0)
    run = re.sub(r'<a:t>.*?</a:t>', lambda _: '<a:t>%s</a:t>' % escape(text), run, flags=re.S)
    ppr = re.search(r'<a:pPr.*?</a:pPr>|<a:pPr[^>]*/>', first_p, re.S)
    para = '<a:p>%s%s</a:p>' % (ppr.group(0) if ppr else '', run)
    body = re.sub(r'<a:p>.*</a:p>', lambda _: para, sp, flags=re.S)
    return xml[:m.start()] + body + xml[m.end():]

def add_notes(xml, script):
    paras = ''.join('<a:p><a:r><a:rPr lang="lt-LT"/><a:t>%s</a:t></a:r></a:p>' % escape(l) for l in script)
    i = xml.index('</p:txBody>', xml.index('type="body"'))
    return xml[:i] + '<a:p><a:endParaRPr lang="lt-LT"/></a:p>' + paras + xml[i:]

def put_image(src, dst):
    from PIL import Image
    im = Image.open(src).convert('RGB')
    w, h = im.size
    if w / h > SLOT_RATIO:
        nw = int(h * SLOT_RATIO); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / SLOT_RATIO); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im.thumbnail((2400, 2400)); im.save(dst, 'PNG')

def main(tpl, out, imgdir=None):
    d = tempfile.mkdtemp()
    zipfile.ZipFile(tpl).extractall(d)
    for i, s in enumerate(SLIDES, 1):
        p = f'{d}/ppt/slides/slide{i}.xml'
        x = open(p, encoding='utf-8').read()
        x = set_text(x, 'section', TEAM)
        for k, t in enumerate(s['text']):
            x = set_text(x, f'replaceable-prompt-{k}', t)
        open(p, 'w', encoding='utf-8').write(x)
        n = f'{d}/ppt/notesSlides/notesSlide{i}.xml'
        notes = add_notes(open(n, encoding='utf-8').read(), s['notes'])
        open(n, 'w', encoding='utf-8').write(notes)
        if imgdir:
            for ext in ('png', 'jpg', 'jpeg', 'webp'):
                src = os.path.join(imgdir, f'{i}.{ext}')
                if os.path.exists(src):
                    put_image(src, f'{d}/ppt/media/image{i + 1}.png'); print('image', i, src)
                    break
    if os.path.exists(out): os.remove(out)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(d):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, d))
    shutil.rmtree(d)
    print('wrote', out)

if __name__ == '__main__':
    main(*sys.argv[1:])
