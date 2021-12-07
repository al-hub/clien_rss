import platform
import sys

Envs = {
   'U18PB1-0717': {
       'OutPath': '/home-mc/core.choi/workspace/temp/clien_rss/',
       'db': 'TEST_DB',
       'table': 'rss'
   },
  'PCName': {
       'OutPath': 'YourOutPathForPC/',
       'db': 'YourTestDBname',
       'table': 'YourTestTableNameForPC'
   },
   'NasName': {
       'OutPath': '/YourOutPathForNas/',
       'db': 'YourDBname',
       'table': 'YourTableNameForNas'
   }
}

Tasks = {
    'clien': {
        'site_url': 'https://www.clien.net',
        'site_bbs': '/service/board/',
        'feed_url': 'http://feeds.feedburner.com/',
        'rss_item': {
            'stock': {
                'bbs_list': {'cm_stock'},
                'rss_desc': 'Clien: Stock',
                'r_cond': 0,
                's_page': 1,
                'f_name': 'c_news'
            },
            'jirum': {
                'bbs_list': {'jirum'},
                'rss_desc': 'Clien: Good Shoping',
                'r_cond': 0,
                's_page': 1,
                'f_name': 'c_news'
            }
        }
    }
}


def getWorkDict():
    run_loc = platform.node()
    # print(run_loc)
    if run_loc in Envs:
        WorkEnv = Envs[run_loc]
    else:
        # WorkEnv = Envs['others']
        print('Unexpected Location: <%s>, Script Stoped' % run_loc)
        sys.exit(...)
    return WorkEnv


# atom1 = getWorkDict()
# print(atom1['OutPath'])
