#!/usr/bin/env python

import sys
import tempfile
import traceback

if sys.version_info.major < 3:
    import ci_tools as tools
    # import tag_release as tag
    from .ci_constants import *
else:
    from ci_scripts import ci_tools as tools
    # from ci_scripts import tag_release as tag
    from ci_scripts.ci_constants import *


def clone_repository(tempdir, url=GITHUB_URL, repo=GITHUB_REPO):
    tools.run_console_command("git clone {url}{repo} {dir}".format(url=url,
                                                                   repo=repo,
                                                                   dir=tempdir))


def merge_with_production(tempdir,
                          branch_to_merge=BRANCH_TO_MERGE,
                          branch_to_merge_into=BRANCH_TO_MERGE_INTO):
    os.chdir(tempdir)
    tools.run_console_command("git checkout {branch}".format(branch=branch_to_merge))
    tools.run_console_command("git checkout {branch}".format(branch=branch_to_merge_into))
    tools.run_console_command("git merge {branch}".format(branch=branch_to_merge))


def push_to_origin(github_repo=GITHUB_REPO, github_token=GITHUB_TOKEN,
                   branch_to_merge_into=BRANCH_TO_MERGE_INTO):
    print("Pushing changes...")
    push_uri = "https://{token}@github.com/{repo}".format(token=github_token,
                                                          repo=github_repo)
    # Redirect to /dev/null to avoid secret leakage
    # tools.run_console_command("git push {uri} {version} > /dev/null 2>&1".format(uri=push_uri,
    #                                                                              version=version))
    tools.run_console_command("git push {uri} {branch} > /dev/null 2>&1".format(uri=push_uri,
                                                                                branch=branch_to_merge_into))
    print("Pushed.")


if __name__ == '__main__':
    try:
        with tempfile.TemporaryDirectory() as tempdir:
            print("\nCloning repository...")
            clone_repository(tempdir)
            print("Cloned.")
            print("\nMerging staging with master...")
            merge_with_production(tempdir)
            print("Merged.")
            print("\nPushing to origin...")
            # tag.set_contact_data(GIT_USERNAME, GIT_EMAIL)
            # version_string = tag.set_version_tag(VERSION_PREFIX)
            push_to_origin()
            print("Pushed.")
    except:
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)
    else:
        sys.exit(0)