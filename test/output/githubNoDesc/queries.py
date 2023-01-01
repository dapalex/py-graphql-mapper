from pygqlmap import GQLQuery
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class codeOfConduct(GQLQuery):
   class CodeOfConductArgs(GQLArgsSet, GQLObject): 
      key: str ##NON NULL

   _args: CodeOfConductArgs


   type: CodeOfConduct

class codesOfConduct(GQLQuery):
   type: CodeOfConduct ##LIST

class enterprise(GQLQuery):
   class EnterpriseArgs(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL
      invitationToken: str

   _args: EnterpriseArgs


   type: Enterprise

class enterpriseAdministratorInvitation(GQLQuery):
   class EnterpriseAdministratorInvitationArgs(GQLArgsSet, GQLObject): 
      userLogin: str ##NON NULL
      enterpriseSlug: str ##NON NULL
      role: EnterpriseAdministratorRole ##NON NULL

   _args: EnterpriseAdministratorInvitationArgs


   type: EnterpriseAdministratorInvitation

class enterpriseAdministratorInvitationByToken(GQLQuery):
   class EnterpriseAdministratorInvitationArgs(GQLArgsSet, GQLObject): 
      invitationToken: str ##NON NULL

   _args: EnterpriseAdministratorInvitationArgs


   type: EnterpriseAdministratorInvitation

class license(GQLQuery):
   class LicenseArgs(GQLArgsSet, GQLObject): 
      key: str ##NON NULL

   _args: LicenseArgs


   type: License

class licenses(GQLQuery):
   type: License ##NON NULL

class marketplaceCategories(GQLQuery):
   class MarketplaceCategoryArgs(GQLArgsSet, GQLObject): 
      includeCategories: str ##NON NULL ##LIST
      excludeEmpty: bool
      excludeSubcategories: bool

   _args: MarketplaceCategoryArgs


   type: MarketplaceCategory ##NON NULL

class marketplaceCategory(GQLQuery):
   class MarketplaceCategoryArgs(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL
      useTopicAliases: bool

   _args: MarketplaceCategoryArgs


   type: MarketplaceCategory

class marketplaceListing(GQLQuery):
   class MarketplaceListingArgs(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL

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
      slugs: str ##LIST
      primaryCategoryOnly: bool
      withFreeTrialsOnly: bool

   _args: MarketplaceListingConnectionArgs


   type: MarketplaceListingConnection ##NON NULL

class meta(GQLQuery):
   type: GitHubMetadata ##NON NULL

class node(GQLQuery):
   class NodeArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: NodeArgs


   type: Node

class nodes(GQLQuery):
   class NodeArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: NodeArgs


   type: Node ##NON NULL

class organization(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: OrganizationArgs


   type: Organization

class rateLimit(GQLQuery):
   class RateLimitArgs(GQLArgsSet, GQLObject): 
      dryRun: bool

   _args: RateLimitArgs


   type: RateLimit

class relay(GQLQuery):
   type: Query ##NON NULL

class repository(GQLQuery):
   class RepositoryArgs(GQLArgsSet, GQLObject): 
      owner: str ##NON NULL
      name: str ##NON NULL
      followRenames: bool

   _args: RepositoryArgs


   type: Repository

class repositoryOwner(GQLQuery):
   class RepositoryOwnerArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: RepositoryOwnerArgs


   type: RepositoryOwner

class resource(GQLQuery):
   class UniformResourceLocatableArgs(GQLArgsSet, GQLObject): 
      url: URI ##NON NULL

   _args: UniformResourceLocatableArgs


   type: UniformResourceLocatable

class search(GQLQuery):
   class SearchResultItemConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      query: str ##NON NULL
      type: SearchType ##NON NULL

   _args: SearchResultItemConnectionArgs


   type: SearchResultItemConnection ##NON NULL

class securityAdvisories(GQLQuery):
   class SecurityAdvisoryConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: SecurityAdvisoryOrder
      identifier: SecurityAdvisoryIdentifierFilter
      publishedSince: DateTime
      updatedSince: DateTime
      classifications: SecurityAdvisoryClassification ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: SecurityAdvisoryConnectionArgs


   type: SecurityAdvisoryConnection ##NON NULL

class securityAdvisory(GQLQuery):
   class SecurityAdvisoryArgs(GQLArgsSet, GQLObject): 
      ghsaId: str ##NON NULL

   _args: SecurityAdvisoryArgs


   type: SecurityAdvisory

class securityVulnerabilities(GQLQuery):
   class SecurityVulnerabilityConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: SecurityAdvisorySeverity ##NON NULL ##LIST
      classifications: SecurityAdvisoryClassification ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: SecurityVulnerabilityConnectionArgs


   type: SecurityVulnerabilityConnection ##NON NULL

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


   type: SponsorableItemConnection ##NON NULL

class topic(GQLQuery):
   class TopicArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: TopicArgs


   type: Topic

class user(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: UserArgs


   type: User

class viewer(GQLQuery):
   type: User ##NON NULL


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
