from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class list_CodeOfConduct(list, CodeOfConduct): pass

class NonNull_EnterpriseAdministratorRole(GQLObject): pass

class NonNull_URI(URI): pass

class NonNull_SearchType(GQLObject): pass

class codeOfConduct(GQLQuery):
   class CodeOfConductArgs(GQLArgsSet, GQLObject):
      key: NonNull_str

   _args: CodeOfConductArgs


   type: CodeOfConduct

class codesOfConduct(GQLQuery):
   type: list_CodeOfConduct[CodeOfConduct]

class enterprise(GQLQuery):
   class EnterpriseArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str
      invitationToken: str

   _args: EnterpriseArgs


   type: Enterprise

class enterpriseAdministratorInvitation(GQLQuery):
   class EnterpriseAdministratorInvitationArgs(GQLArgsSet, GQLObject):
      userLogin: NonNull_str
      enterpriseSlug: NonNull_str
      role: NonNull_EnterpriseAdministratorRole

   _args: EnterpriseAdministratorInvitationArgs


   type: EnterpriseAdministratorInvitation

class enterpriseAdministratorInvitationByToken(GQLQuery):
   class EnterpriseAdministratorInvitationArgs(GQLArgsSet, GQLObject):
      invitationToken: NonNull_str

   _args: EnterpriseAdministratorInvitationArgs


   type: EnterpriseAdministratorInvitation

class license(GQLQuery):
   class LicenseArgs(GQLArgsSet, GQLObject):
      key: NonNull_str

   _args: LicenseArgs


   type: License

class licenses(GQLQuery):
   type: License

class marketplaceCategories(GQLQuery):
   class MarketplaceCategoryArgs(GQLArgsSet, GQLObject):
      includeCategories: list[NonNull_str]
      excludeEmpty: bool
      excludeSubcategories: bool

   _args: MarketplaceCategoryArgs


   type: MarketplaceCategory

class marketplaceCategory(GQLQuery):
   class MarketplaceCategoryArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str
      useTopicAliases: bool

   _args: MarketplaceCategoryArgs


   type: MarketplaceCategory

class marketplaceListing(GQLQuery):
   class MarketplaceListingArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: MarketplaceListingArgs


   type: MarketplaceListing

class marketplaceListings(GQLQuery):
   class MarketplaceListingConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      categorySlug: str
      useTopicAliases: bool
      viewerCanAdmin: bool
      adminId: ID
      organizationId: ID
      allStates: bool
      slugs: list[str]
      primaryCategoryOnly: bool
      withFreeTrialsOnly: bool

   _args: MarketplaceListingConnectionArgs


   type: MarketplaceListingConnection

class meta(GQLQuery):
   type: GitHubMetadata

class node(GQLQuery):
   class NodeArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: NodeArgs


   type: Node

class nodes(GQLQuery):
   class NodeArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: NodeArgs


   type: Node

class organization(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: OrganizationArgs


   type: Organization

class rateLimit(GQLQuery):
   class RateLimitArgs(GQLArgsSet, GQLObject):
      dryRun: bool

   _args: RateLimitArgs


   type: RateLimit

class relay(GQLQuery):
   type: None

class repository(GQLQuery):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      owner: NonNull_str
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs


   type: Repository

class repositoryOwner(GQLQuery):
   class RepositoryOwnerArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: RepositoryOwnerArgs


   type: RepositoryOwner

class resource(GQLQuery):
   class UniformResourceLocatableArgs(GQLArgsSet, GQLObject):
      url: NonNull_URI

   _args: UniformResourceLocatableArgs


   type: UniformResourceLocatable

class search(GQLQuery):
   class SearchResultItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: NonNull_str
      type: NonNull_SearchType

   _args: SearchResultItemConnectionArgs


   type: SearchResultItemConnection

class securityAdvisories(GQLQuery):
   class SecurityAdvisoryConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: SecurityAdvisoryOrder
      identifier: SecurityAdvisoryIdentifierFilter
      publishedSince: DateTime
      updatedSince: DateTime
      classifications: list[NonNull_SecurityAdvisoryClassification]
      after: str
      before: str
      first: int
      last: int

   _args: SecurityAdvisoryConnectionArgs


   type: SecurityAdvisoryConnection

class securityAdvisory(GQLQuery):
   class SecurityAdvisoryArgs(GQLArgsSet, GQLObject):
      ghsaId: NonNull_str

   _args: SecurityAdvisoryArgs


   type: SecurityAdvisory

class securityVulnerabilities(GQLQuery):
   class SecurityVulnerabilityConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: list[NonNull_SecurityAdvisorySeverity]
      classifications: list[NonNull_SecurityAdvisoryClassification]
      after: str
      before: str
      first: int
      last: int

   _args: SecurityVulnerabilityConnectionArgs


   type: SecurityVulnerabilityConnection

class sponsorables(GQLQuery):
   class SponsorableItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorableOrder
      onlyDependencies: bool
      orgLoginForDependencies: str
      dependencyEcosystem: SecurityAdvisoryEcosystem
      ecosystem: DependencyGraphEcosystem

   _args: SponsorableItemConnectionArgs


   type: SponsorableItemConnection

class topic(GQLQuery):
   class TopicArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: TopicArgs


   type: Topic

class user(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: UserArgs


   type: User

class viewer(GQLQuery):
   type: User


class Queries(Enum):
   codeOfConduct = codeOfConduct
   codesOfConduct = codesOfConduct
   enterprise = enterprise
   enterpriseAdministratorInvitation = enterpriseAdministratorInvitation
   enterpriseAdministratorInvitationByToken = enterpriseAdministratorInvitationByToken
   license = license
   licenses = licenses
   marketplaceCategories = marketplaceCategories
   marketplaceCategory = marketplaceCategory
   marketplaceListing = marketplaceListing
   marketplaceListings = marketplaceListings
   meta = meta
   node = node
   nodes = nodes
   organization = organization
   rateLimit = rateLimit
   relay = relay
   repository = repository
   repositoryOwner = repositoryOwner
   resource = resource
   search = search
   securityAdvisories = securityAdvisories
   securityAdvisory = securityAdvisory
   securityVulnerabilities = securityVulnerabilities
   sponsorables = sponsorables
   topic = topic
   user = user
   viewer = viewer
