import os,sys
import argparse
from dropbox import dropbox

about = 'This program deletes all public links from files shared in Dropbox'
parser = argparse.ArgumentParser(description = about)
parser.add_argument("-t", "--token", help="Dropbox app security token (key) to use for authentication (see https://www.dropbox.com/developers/apps)")
parser.add_argument("-d", "--dryrun", help="don't delete just print links that would be removed", action="store_true")
args = parser.parse_args()

TOKEN = args.token
if not TOKEN:
    print('please provide Dropbox API TOKEN (KEY) via -t argument')
    sys.exit(1)

dbx = dropbox.Dropbox(TOKEN)

try:
    link_results = dbx.sharing_list_shared_links()
except dropbox.BadInputError as e:
    print(f'app not found: {str(e.message)}')
    sys.exit(1)
except dropbox.AuthError as e:
    print(f'could not authenticate: {str(e)}')
    sys.exit(1)

if not link_results.links:
    print('no shared links found')
    sys.exit(0)

for i in link_results.links:
    try:
        if args.dryrun:
            print(f'would remove link for {i.name}')
            continue
        dbx.sharing_revoke_shared_link(i.url)
        print(f'successfully removed link for {i.name}')
    except dropbox.ApiError as e:
        print(f'error deleting link for {i.name}: {str(e)}')
        continue
    