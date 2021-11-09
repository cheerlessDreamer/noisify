from setuptools import setup

# To build a new application, run: python3 setup.py py2app

APP = ['noisify.py']
DATA_FILES = [('', ['icon.png']),
              ('', ['noise.webm']),
              ('', ['playPadded.png']),
              ('', ['stopPadded.png']),
              ('', ['whiteNoise.icns']),
              ('', ['playing.png']),
              ]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.png',
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='Noisify',
    author='Danny Taylor',
    author_email='danny@dannytaylor.se',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps']
)
