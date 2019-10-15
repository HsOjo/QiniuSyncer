from os import walk

from qiniu import Auth, put_file


class SevenCow:
    def __init__(self):
        self._auth = None  # type: Auth
        self.bucket = ''

    def use(self, bucket):
        self.bucket = bucket

    def auth(self, access_key, secret_key):
        self._auth = Auth(access_key, secret_key)

    def put(self, path_local, path_remote):
        token = self._auth.upload_token(self.bucket, path_remote)
        ret, info = put_file(token, path_remote, path_local)
        return ret, info

    def sync_dir(self, dir, top_only=False, callback=None):
        up_list = []
        for np, ds, fs in walk(dir):
            for f in fs:
                p_local = '%s/%s' % (np, f)
                p_remote = p_local.replace(dir + '/', '')

                up_list.append({'local': p_local, 'remote': p_remote})
            if top_only:
                break

        l_up_list = len(up_list)
        if callback is not None:
            callback(0, l_up_list)
        for i in range(l_up_list):
            p = up_list[i]
            self.put(p['local'], p['remote'])
            if callback is not None:
                callback(i + 1, l_up_list)
