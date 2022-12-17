from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class codeOfConduct(GQLObject):
   class Args(): 
      key: str ##NON NULL

   _args: Args


   type: CodeOfConduct

codesOfConduct = list[CodeOfConduct]

class enterprise(GQLObject):
   class Args(): 
      slug: str ##NON NULL
      invitationToken: str

   _args: Args


   type: Enterprise

class enterpriseAdministratorInvitation(GQLObject):
   class Args(): 
      userLogin: str ##NON NULL
      enterpriseSlug: str ##NON NULL
      role: EnterpriseAdministratorRole ##NON NULL

   _args: Args


   type: EnterpriseAdministratorInvitation

class enterpriseAdministratorInvitationByToken(GQLObject):
   class Args(): 
      invitationToken: str ##NON NULL

   _args: Args


   type: EnterpriseAdministratorInvitation

class license(GQLObject):
   class Args(): 
      key: str ##NON NULL

   _args: Args


   type: License

class licenses(GQLObject):
   type: License ##NON NULL

class marketplaceCategories(GQLObject):
   class Args(): 
      includeCategories: list[str] ##NON NULL
      excludeEmpty: bool
      excludeSubcategories: bool

   _args: Args


   type: MarketplaceCategory ##NON NULL

class marketplaceCategory(GQLObject):
   class Args(): 
      slug: str ##NON NULL
      useTopicAliases: bool

   _args: Args


   type: MarketplaceCategory

class marketplaceListing(GQLObject):
   class Args(): 
      slug: str ##NON NULL

   _args: Args


   type: MarketplaceListing

class marketplaceListings(GQLObject):
   class Args(): 
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

   _args: Args


   type: MarketplaceListingConnection ##NON NULL

class meta(GQLObject):
   type: GitHubMetadata ##NON NULL

class node(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: Node

class nodes(GQLObject):
   class Args(): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: Node ##NON NULL

class organization(GQLObject):
   class Args(): 
      login: str ##NON NULL

   _args: Args


   type: Organization

class rateLimit(GQLObject):
   class Args(): 
      dryRun: bool

   _args: Args


   type: RateLimit

class relay(GQLObject):
   type: Query ##NON NULL

class repository(GQLObject):
   class Args(): 
      owner: str ##NON NULL
      name: str ##NON NULL
      followRenames: bool

   _args: Args


   type: Repository

class repositoryOwner(GQLObject):
   class Args(): 
      login: str ##NON NULL

   _args: Args


   type: RepositoryOwner

class resource(GQLObject):
   class Args(): 
      url: URI ##NON NULL

   _args: Args


   type: UniformResourceLocatable

class search(GQLObject):
   class Args(): 
      after: str
      before: str
      first: int
      last: int
      query: str ##NON NULL
      type: SearchType ##NON NULL

   _args: Args


   type: SearchResultItemConnection ##NON NULL

class securityAdvisories(GQLObject):
   class Args(): 
      orderBy: SecurityAdvisoryOrder
      identifier: SecurityAdvisoryIdentifierFilter
      publishedSince: DateTime
      updatedSince: DateTime
      classifications: list[SecurityAdvisoryClassification] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args


   type: SecurityAdvisoryConnection ##NON NULL

class securityAdvisory(GQLObject):
   class Args(): 
      ghsaId: str ##NON NULL

   _args: Args


   type: SecurityAdvisory

class securityVulnerabilities(GQLObject):
   class Args(): 
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: list[SecurityAdvisorySeverity] ##NON NULL
      classifications: list[SecurityAdvisoryClassification] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args


   type: SecurityVulnerabilityConnection ##NON NULL

class sponsorables(GQLObject):
   class Args(): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorableOrder
      onlyDependencies: bool
      orgLoginForDependencies: str
      dependencyEcosystem: SecurityAdvisoryEcosystem
      ecosystem: DependencyGraphEcosystem

   _args: Args


   type: SponsorableItemConnection ##NON NULL

class topic(GQLObject):
   class Args(): 
      name: str ##NON NULL

   _args: Args


   type: Topic

class user(GQLObject):
   class Args(): 
      login: str ##NON NULL

   _args: Args


   type: User

class viewer(GQLObject):
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
