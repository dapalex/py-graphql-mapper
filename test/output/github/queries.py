from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class codeOfConduct(GQLObject):
   """
   codeOfConduct - Look up a code of conduct by its key

   """
   class Args(): 
      """
      key - The code of conduct's key

      """
      key: str ##NON NULL

   _args: Args


   type: CodeOfConduct

codesOfConduct = list[CodeOfConduct]

class enterprise(GQLObject):
   """
   enterprise - Look up an enterprise by URL slug.

   """
   class Args(): 
      """
      slug - The enterprise URL slug.

      invitationToken - The enterprise invitation token.

      """
      slug: str ##NON NULL
      invitationToken: str

   _args: Args


   type: Enterprise

class enterpriseAdministratorInvitation(GQLObject):
   """
   enterpriseAdministratorInvitation - Look up a pending enterprise administrator invitation by invitee, enterprise and role.

   """
   class Args(): 
      """
      userLogin - The login of the user invited to join the business.

      enterpriseSlug - The slug of the enterprise the user was invited to join.

      role - The role for the business member invitation.

      """
      userLogin: str ##NON NULL
      enterpriseSlug: str ##NON NULL
      role: EnterpriseAdministratorRole ##NON NULL

   _args: Args


   type: EnterpriseAdministratorInvitation

class enterpriseAdministratorInvitationByToken(GQLObject):
   """
   enterpriseAdministratorInvitationByToken - Look up a pending enterprise administrator invitation by invitation token.

   """
   class Args(): 
      """
      invitationToken - The invitation token sent with the invitation email.

      """
      invitationToken: str ##NON NULL

   _args: Args


   type: EnterpriseAdministratorInvitation

class license(GQLObject):
   """
   license - Look up an open source license by its key

   """
   class Args(): 
      """
      key - The license's downcased SPDX ID

      """
      key: str ##NON NULL

   _args: Args


   type: License

class licenses(GQLObject):
   """
   licenses - Return a list of known open source licenses

   """
   type: License ##NON NULL

class marketplaceCategories(GQLObject):
   """
   marketplaceCategories - Get alphabetically sorted list of Marketplace categories

   """
   class Args(): 
      """
      includeCategories - Return only the specified categories.

      excludeEmpty - Exclude categories with no listings.

      excludeSubcategories - Returns top level categories only, excluding any subcategories.

      """
      includeCategories: list[str] ##NON NULL
      excludeEmpty: bool
      excludeSubcategories: bool

   _args: Args


   type: MarketplaceCategory ##NON NULL

class marketplaceCategory(GQLObject):
   """
   marketplaceCategory - Look up a Marketplace category by its slug.

   """
   class Args(): 
      """
      slug - The URL slug of the category.

      useTopicAliases - Also check topic aliases for the category slug

      """
      slug: str ##NON NULL
      useTopicAliases: bool

   _args: Args


   type: MarketplaceCategory

class marketplaceListing(GQLObject):
   """
   marketplaceListing - Look up a single Marketplace listing

   """
   class Args(): 
      """
      slug - Select the listing that matches this slug. It's the short name of the listing used in its URL.

      """
      slug: str ##NON NULL

   _args: Args


   type: MarketplaceListing

class marketplaceListings(GQLObject):
   """
   marketplaceListings - Look up Marketplace listings

   """
   class Args(): 
      """
      after - Returns the elements in the list that come after the specified cursor.

      before - Returns the elements in the list that come before the specified cursor.

      first - Returns the first _n_ elements from the list.

      last - Returns the last _n_ elements from the list.

      categorySlug - Select only listings with the given category.

      useTopicAliases - Also check topic aliases for the category slug

      viewerCanAdmin - Select listings to which user has admin access. If omitted, listings visible to the
viewer are returned.


      adminId - Select listings that can be administered by the specified user.

      organizationId - Select listings for products owned by the specified organization.

      allStates - Select listings visible to the viewer even if they are not approved. If omitted or
false, only approved listings will be returned.


      slugs - Select the listings with these slugs, if they are visible to the viewer.

      primaryCategoryOnly - Select only listings where the primary category matches the given category slug.

      withFreeTrialsOnly - Select only listings that offer a free trial.

      """
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
   """
   meta - Return information about the GitHub instance

   """
   type: GitHubMetadata ##NON NULL

class node(GQLObject):
   """
   node - Fetches an object given its ID.

   """
   class Args(): 
      """
      id - ID of the object.

      """
      id: ID ##NON NULL

   _args: Args


   type: Node

class nodes(GQLObject):
   """
   nodes - Lookup nodes by a list of IDs.

   """
   class Args(): 
      """
      ids - The list of node IDs.

      """
      ids: list[ID] ##NON NULL

   _args: Args


   type: Node ##NON NULL

class organization(GQLObject):
   """
   organization - Lookup a organization by login.

   """
   class Args(): 
      """
      login - The organization's login.

      """
      login: str ##NON NULL

   _args: Args


   type: Organization

class rateLimit(GQLObject):
   """
   rateLimit - The client's rate limit information.

   """
   class Args(): 
      """
      dryRun - If true, calculate the cost for the query without evaluating it

      """
      dryRun: bool

   _args: Args


   type: RateLimit

class relay(GQLObject):
   """
   relay - Hack to workaround https://github.com/facebook/relay/issues/112 re-exposing the root query object

   """
   type: Query ##NON NULL

class repository(GQLObject):
   """
   repository - Lookup a given repository by the owner and repository name.

   """
   class Args(): 
      """
      owner - The login field of a user or organization

      name - The name of the repository

      followRenames - Follow repository renames. If disabled, a repository referenced by its old name will return an error.

      """
      owner: str ##NON NULL
      name: str ##NON NULL
      followRenames: bool

   _args: Args


   type: Repository

class repositoryOwner(GQLObject):
   """
   repositoryOwner - Lookup a repository owner (ie. either a User or an Organization) by login.

   """
   class Args(): 
      """
      login - The username to lookup the owner by.

      """
      login: str ##NON NULL

   _args: Args


   type: RepositoryOwner

class resource(GQLObject):
   """
   resource - Lookup resource by a URL.

   """
   class Args(): 
      """
      url - The URL.

      """
      url: URI ##NON NULL

   _args: Args


   type: UniformResourceLocatable

class search(GQLObject):
   """
   search - Perform a search across resources, returning a maximum of 1,000 results.

   """
   class Args(): 
      """
      after - Returns the elements in the list that come after the specified cursor.

      before - Returns the elements in the list that come before the specified cursor.

      first - Returns the first _n_ elements from the list.

      last - Returns the last _n_ elements from the list.

      query - The search string to look for.

      type - The types of search items to search within.

      """
      after: str
      before: str
      first: int
      last: int
      query: str ##NON NULL
      type: SearchType ##NON NULL

   _args: Args


   type: SearchResultItemConnection ##NON NULL

class securityAdvisories(GQLObject):
   """
   securityAdvisories - GitHub Security Advisories

   """
   class Args(): 
      """
      orderBy - Ordering options for the returned topics.

      identifier - Filter advisories by identifier, e.g. GHSA or CVE.

      publishedSince - Filter advisories to those published since a time in the past.

      updatedSince - Filter advisories to those updated since a time in the past.

      classifications - A list of classifications to filter advisories by.

      after - Returns the elements in the list that come after the specified cursor.

      before - Returns the elements in the list that come before the specified cursor.

      first - Returns the first _n_ elements from the list.

      last - Returns the last _n_ elements from the list.

      """
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
   """
   securityAdvisory - Fetch a Security Advisory by its GHSA ID

   """
   class Args(): 
      """
      ghsaId - GitHub Security Advisory ID.

      """
      ghsaId: str ##NON NULL

   _args: Args


   type: SecurityAdvisory

class securityVulnerabilities(GQLObject):
   """
   securityVulnerabilities - Software Vulnerabilities documented by GitHub Security Advisories

   """
   class Args(): 
      """
      orderBy - Ordering options for the returned topics.

      ecosystem - An ecosystem to filter vulnerabilities by.

      package - A package name to filter vulnerabilities by.

      severities - A list of severities to filter vulnerabilities by.

      classifications - A list of advisory classifications to filter vulnerabilities by.

      after - Returns the elements in the list that come after the specified cursor.

      before - Returns the elements in the list that come before the specified cursor.

      first - Returns the first _n_ elements from the list.

      last - Returns the last _n_ elements from the list.

      """
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
   """
   sponsorables - Users and organizations who can be sponsored via GitHub Sponsors.

   """
   class Args(): 
      """
      after - Returns the elements in the list that come after the specified cursor.

      before - Returns the elements in the list that come before the specified cursor.

      first - Returns the first _n_ elements from the list.

      last - Returns the last _n_ elements from the list.

      orderBy - Ordering options for users and organizations returned from the connection.

      onlyDependencies - Whether only sponsorables who own the viewer's dependencies will be returned. Must be authenticated to use. Can check an organization instead for their dependencies owned by sponsorables by passing orgLoginForDependencies.

      orgLoginForDependencies - Optional organization username for whose dependencies should be checked. Used when onlyDependencies = true. Omit to check your own dependencies. If you are not an administrator of the organization, only dependencies from its public repositories will be considered.

      dependencyEcosystem - Optional filter for which dependencies should be checked for sponsorable owners. Only sponsorable owners of dependencies in this ecosystem will be included. Used when onlyDependencies = true.

**Upcoming Change on 2022-07-01 UTC**
**Description:** `dependencyEcosystem` will be removed. Use the ecosystem argument instead.
**Reason:** The type is switching from SecurityAdvisoryEcosystem to DependencyGraphEcosystem.


      ecosystem - Optional filter for which dependencies should be checked for sponsorable owners. Only sponsorable owners of dependencies in this ecosystem will be included. Used when onlyDependencies = true.

      """
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
   """
   topic - Look up a topic by name.

   """
   class Args(): 
      """
      name - The topic's name.

      """
      name: str ##NON NULL

   _args: Args


   type: Topic

class user(GQLObject):
   """
   user - Lookup a user by login.

   """
   class Args(): 
      """
      login - The user's login.

      """
      login: str ##NON NULL

   _args: Args


   type: User

class viewer(GQLObject):
   """
   viewer - The currently authenticated user.

   """
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
