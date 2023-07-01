from typing import List
from pygqlmap import GQLSubscription
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
# from .type_refs import *

class repository(GQLSubscription):
   """
   repository - Lookup a given repository by the owner and repository name.

   """
   class RepositoryArgs(GQLArgsSet, GQLObject):
      """
      owner - The login field of a user or organization

      name - The name of the repository

      followRenames - Follow repository renames. If disabled, a repository referenced by its old name will return an error.

      """
      owner: NonNull_str
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs


   type: Repository
