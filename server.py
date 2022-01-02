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
    return os.access(fn, os.F_OK)


@app.errorhandler(404)
def get_page(*args, **kwargs) -> any:
    url = flask.request.url
    path = get_path_from_url(url)
    ext = url.split('.')[-1].lower().strip()
    if ext in ('html', 'htm'):
        if not file_exists(path):
            return error404()
        return fast_read(path), 200
    if file_exists(path) and not os.path.isdir(path):
        return app.send_static_file(path), 200
    if url.endswith('/'):
        url = url[:-1]
    test_path = get_path_from_url(url + '/index.html')
    print(url, path, test_path)
    if file_exists(test_path):
        return fast_read(test_path), 200
    return error404()


if __name__ == '__main__':
    app.run(
        '127.0.0.1',
        port=8000,
        debug=True
    )
