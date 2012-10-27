from .main import SceneHD

def start():
    return SceneHD()

config = [{
    'name': 'scenehd',
    'groups': [
        {
            'tab': 'searcher',
            'subtab': 'torrent_providers',
            'name': 'SceneHD',
            'description': 'See <a href="https://scenehd.org">SceneHD</a>',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
            ],
        },
    ],
}]
