import urllib.request
import re
import os
import urllib
import ssl


def get_html(url):
    # urlopen打开https链接时，会验证一次SSL证书。这里取消证书的验证。
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')


def get_img(html):
    reg = r'https://[^\s]*?\.jpg'
    image_re = re.compile(reg)
    image_list = image_re.findall(html)
    x = 1
    path = '/Users/baoyongshuai/Documents/pypath'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '/'
    for image_url in image_list:
        image_name = '{0}{1}.jpg'.format(paths, x)
        urllib.request.urlretrieve(image_url, image_name)
        x = x + 1
        print('图片开始下载，注意查看文件夹，图片名称：' + image_name)
    return image_url


html_b = get_html('http://tieba.baidu.com/p/6055320747')
get_img(html_b)
