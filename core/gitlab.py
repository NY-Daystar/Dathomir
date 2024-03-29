'''Handle Repositories for gitlab'''

import logging
from typing import List

import helper

from git import Repo
from git.exc import GitCommandError
from gitlab import Gitlab, GitlabAuthenticationError
from gitlab.base import RESTObject
from gitlab.v4.objects import Project

from .exc import AuthGitException
from .git import Git

log = logging.getLogger("dathomir")


class GitLab(Git):
    '''Gitlab instance to handle project'''
    remote: Gitlab

    '''if it's self host instance gitlab true (like company.gitlab.com),
    or only directly https://gitlab.com
    '''
    hosted: bool

    def __init__(self, url, token):
        super().__init__(url, token)
        # Check if it's a self-host Gitlab instance
        self.hosted = bool(self.url != "https://gitlab.com")

    def connect(self) -> tuple[str, Exception]:
        '''Get access to self-hosted GitLab instance
        with private token or personal token authentication'''
        if self.hosted:
            log.info("Connected to self host instance")
            self.remote = Gitlab(url=self.url, private_token=self.token)
        else:
            log.info("Connect to Gitlab.com")
            self.remote = Gitlab(private_token=self.token)

        try:
            self.remote.auth()
        except GitlabAuthenticationError as exc:
            return (False, AuthGitException(exc.response_code, exc.error_message))
        return True, None

    def get_projects(self) -> List[RESTObject]:
        '''Get all project with your authentication'''
        if self.hosted:
            return self.remote.projects.list(all=True)
        return self.remote.projects.list(owned=True)

    def clone_project(self, project: Project, dest_folder: str):
        '''Clone the project into dest folder using git clone'''
        log.debug("Project info: %s - id=%d - url=%s",
                  project.name, project.id, project.ssh_url_to_repo)

        repo_path = helper.get_path(dest_folder, project.ssh_url_to_repo)
        log.info("Cloning into project %s", repo_path)

        try:
            Repo.clone_from(project.ssh_url_to_repo, repo_path)
            log.info("%s cloned", repo_path)
        except GitCommandError:
            self.update_project(repo_path)

    def update_project(self, repo_path: str):
        '''Update repo project using git pull'''
        log.info("Repo already exists updating it")
        repo = Repo(repo_path)

        if not repo.bare:
            log.debug('Repo at %s successfully loaded.', repo_path)
            try:
                repo.remotes.origin.pull()
                log.info("Repo %s updated", repo_path)
            except GitCommandError:
                log.warning("Repo can't be updated may be it's empty")
        else:
            log.debug('Could not load repository at %s', repo_path)

    def __str__(self):
        return f"GitLab instance of {self.dns}"
