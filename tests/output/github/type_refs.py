from typing import TypeVar, List
from pygqlmap.components import GQLObject
from pygqlmap.gql_types import ID


ProjectV2ItemConnection = TypeVar('ProjectV2ItemConnection', bound=GQLObject)

PullRequestConnection = TypeVar('PullRequestConnection', bound=GQLObject)

Repository = TypeVar('Repository', bound=GQLObject)

Project = TypeVar('Project', bound=GQLObject)

Topic = TypeVar('Topic', bound=GQLObject)

CommitCommentConnection = TypeVar('CommitCommentConnection', bound=GQLObject)

Issue = TypeVar('Issue', bound=GQLObject)

ProjectV2 = TypeVar('ProjectV2', bound=GQLObject)

PullRequest = TypeVar('PullRequest', bound=GQLObject)

Ref = TypeVar('Ref', bound=GQLObject)

SponsorsActivityConnection = TypeVar('SponsorsActivityConnection', bound=GQLObject)

Sponsorship = TypeVar('Sponsorship', bound=GQLObject)

SponsorshipConnection = TypeVar('SponsorshipConnection', bound=GQLObject)

Organization = TypeVar('Organization', bound=GQLObject)

IpAllowListEntryConnection = TypeVar('IpAllowListEntryConnection', bound=GQLObject)

WorkflowRunConnection = TypeVar('WorkflowRunConnection', bound=GQLObject)
