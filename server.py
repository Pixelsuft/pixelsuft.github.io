import os
import sys
import flask


encoding = sys.getdefaultencoding()
app = flask.Flask(__name__, static_folder=os.getcwd())


def fast_read(fn: str) -> str:
    f_ = open(fn, 'rb')
    result = f_.read()
    f_.close()
    return result.decode(encoding, errors='replace')


def error404() -> any:
    return fast_read('404.html'), 404


def get_path_from_url(url_: str) -> str:
    return '/'.join(url_.split('/')[3:])


def file_exists(fn: str) -> bool:
    return os.access(fn, os.F_OK) and not os.path.isdir(fn)


def try_render(fn: str) -> None:
    if file_exists(fn):
        return fast_read(fn), 200
    return error404()


@app.errorhandler(404)
def get_page(*args, **kwargs) -> any:
    url = flask.request.url
    path = get_path_from_url(url)
    if not path:
        return try_render('index.html')
    ext = url.split('.')[-1].lower().strip()
    if ext in ('html', 'htm'):
        return try_render(path)
    if file_exists(path):
        return app.send_static_file(path), 200
    return try_render(get_path_from_url(url + 'index.html'))


if __name__ == '__main__':
    app.run(
        '127.0.0.1',
        port=8000,
        debug=True
    )
