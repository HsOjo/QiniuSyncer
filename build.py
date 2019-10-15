import platform
import shutil
import subprocess
import sys
from zipfile import ZipFile

from app.res.const import Const
from app.res.language import load_language, LANGUAGES
from app.res.language.translate_language import TranslateLanguage
from app.util.log import Log
from tools.translate import *

sys_type = platform.system()
datas = {}


def add_data(src, dest):
    if os.path.exists(src):
        datas[src] = dest


# build translate language data.
Log.append('Build', 'Info', 'Building translate data now...')
load_language()
for lang_type in LANGUAGES.values():
    if issubclass(lang_type, TranslateLanguage):
        lang = lang_type()
        if not lang._translated:
            if lang._translate_to == 'cn_t':
                translator = zhconv()
            elif '--translate-baidu' in sys.argv:
                translator = baidu_translate()
            else:
                translator = google_translate()
            Log.append('Build', 'Translate', 'Using %s' % translator.__class__.__name__)

            lang.translate(translator)
            lang.save_current_translate()
        add_data(lang._data_path, './app/res/language/translate')

# reset dist directory.
shutil.rmtree('./build', ignore_errors=True)
shutil.rmtree('./dist/%s.app' % Const.app_name, ignore_errors=True)

add_data('./app/res/icon.png', './app/res')

data_str = ''
for k, v in datas.items():
    data_str += ' '
    sep = ';' if sys_type == 'Windows' else ':'
    data_str += '--add-data "%s%s%s"' % (k, sep, v)

Log.append('Build', 'Info', 'Pyinstaller packing now...')

if sys_type == 'Darwin':
    path_icon = './app/res/icon.icns'
else:
    path_icon = './app/res/icon.ico'

icon = ''
if os.path.exists(path_icon):
    icon = '-i "%s"' % path_icon

pyi_cmd = 'pyinstaller -F -w -n "%s" %s %s __main__.py' % (Const.app_name, icon, data_str)
print(pyi_cmd)
p = subprocess.Popen(pyi_cmd, env=os.environ, stdout=sys.stdout, shell=True)
p.wait()
os.unlink('./%s.spec' % Const.app_name)
shutil.rmtree('./build', ignore_errors=True)

Log.append('Build', 'Info', 'Packing release zip file now...')

# pack release zip file.
if sys_type == 'Darwin':
    zf = ZipFile('./dist/%s-%s.zip' % (Const.app_name, Const.version), 'w')
    src_dir = './dist/%s.app' % Const.app_name
    for d, ds, fs in os.walk(src_dir):
        for f in fs:
            path = os.path.join(d, f)
            z_path = path[7:].strip(os.path.sep)
            zf.write(path, z_path)
    zf.close()

Log.append('Build', 'Info', 'Build finish.')
