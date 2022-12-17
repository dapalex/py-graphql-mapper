from typing import TypeVar
from pygqlmap.components import GQLObject

PullRequestConnection = TypeVar('PullRequestConnection', bound=GQLObject)

Repository = TypeVar('Repository', bound=GQLObject)

Project = TypeVar('Project', bound=GQLObject)

Topic = TypeVar('Topic', bound=GQLObject)

CommitCommentConnection = TypeVar('CommitCommentConnection', bound=GQLObject)

Issue = TypeVar('Issue', bound=GQLObject)

PullRequest = TypeVar('PullRequest', bound=GQLObject)

Ref = TypeVar('Ref', bound=GQLObject)

ProjectV2ItemConnection = TypeVar('ProjectV2ItemConnection', bound=GQLObject)

ProjectNextItemConnection = TypeVar('ProjectNextItemConnection', bound=GQLObject)

SponsorsActivityConnection = TypeVar('SponsorsActivityConnection', bound=GQLObject)

SponsorshipConnection = TypeVar('SponsorshipConnection', bound=GQLObject)

Organization = TypeVar('Organization', bound=GQLObject)

IpAllowListEntryConnection = TypeVar('IpAllowListEntryConnection', bound=GQLObject)

WorkflowRunConnection = TypeVar('WorkflowRunConnection', bound=GQLObject)

