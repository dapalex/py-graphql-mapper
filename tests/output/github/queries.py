from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

NonNull_EnterpriseAdministratorRole = EnterpriseAdministratorRole

NonNull_URI = URI

NonNull_SearchType = SearchType

class codeOfConduct(GQLQuery):
   """
   codeOfConduct - Look up a code of conduct by its key

   """
   class CodeOfConductArgs(GQLArgsSet, GQLObject): 
      """
      key - The code of conduct's key

      """
      key: NonNull_str

   _args: CodeOfConductArgs


   type: CodeOfConduct

class codesOfConduct(GQLQuery):
   """
   codesOfConduct - Look up a code of conduct by its key

   """
   type: List[CodeOfConduct]

class enterprise(GQLQuery):
   """
   enterprise - Look up an enterprise by URL slug.

   """
   class EnterpriseArgs(GQLArgsSet, GQLObject): 
      """
      slug - The enterprise URL slug.

      invitationToken - The enterprise invitation token.

      """
      slug: NonNull_str
      invitationToken: str

   _args: EnterpriseArgs


   type: Enterprise

class enterpriseAdministratorInvitation(GQLQuery):
   """
   enterpriseAdministratorInvitation - Look up a pending enterprise administrator invitation by invitee, enterprise and role.

   """
   class EnterpriseAdministratorInvitationArgs(GQLArgsSet, GQLObject): 
      """
      userLogin - The login of the user invited to join the business.

      enterpriseSlug - The slug of the enterprise the user was invited to join.

      role - The role for the business member invitation.

      """
      userLogin: NonNull_str
      enterpriseSlug: NonNull_str
      role: NonNull_EnterpriseAdministratorRole

   _args: EnterpriseAdministratorInvitationArgs


   type: EnterpriseAdministratorInvitation

class enterpriseAdministratorInvitationByToken(GQLQuery):
   """
   enterpriseAdministratorInvitationByToken - Look up a pending enterprise administrator invitation by invitation token.

   """
   class EnterpriseAdministratorInvitationArgs(GQLArgsSet, GQLObject): 
      """
      invitationToken - The invitation token sent with the invitation email.

      """
      invitationToken: NonNull_str

   _args: EnterpriseAdministratorInvitationArgs


   type: EnterpriseAdministratorInvitation

class license(GQLQuery):
   """
   license - Look up an open source license by its key

   """
   class LicenseArgs(GQLArgsSet, GQLObject): 
      """
      key - The license's downcased SPDX ID

      """
      key: NonNull_str

   _args: LicenseArgs


   type: License

class licenses(GQLQuery):
   """
   licenses - Return a list of known open source licenses

   """
   type: License

class marketplaceCategories(GQLQuery):
   """
   marketplaceCategories - Get alphabetically sorted list of Marketplace categories

   """
   class MarketplaceCategoryArgs(GQLArgsSet, GQLObject): 
      """
      includeCategories - Return only the specified categories.

      excludeEmpty - Exclude categories with no listings.

      excludeSubcategories - Returns top level categories only, excluding any subcategories.

      """
      includeCategories: List[NonNull_str]
      excludeEmpty: bool
      excludeSubcategories: bool

   _args: MarketplaceCategoryArgs


   type: MarketplaceCategory

class marketplaceCategory(GQLQuery):
   """
   marketplaceCategory - Look up a Marketplace category by its slug.

   """
   class MarketplaceCategoryArgs(GQLArgsSet, GQLObject): 
      """
      slug - The URL slug of the category.

      useTopicAliases - Also check topic aliases for the category slug

      """
      slug: NonNull_str
      useTopicAliases: bool

   _args: MarketplaceCategoryArgs


   type: MarketplaceCategory

class marketplaceListing(GQLQuery):
   """
   marketplaceListing - Look up a single Marketplace listing

   """
   class MarketplaceListingArgs(GQLArgsSet, GQLObject): 
      """
      slug - Select the listing that matches this slug. It's the short name of the listing used in its URL.

      """
      slug: NonNull_str

   _args: MarketplaceListingArgs


   type: MarketplaceListing

class marketplaceListings(GQLQuery):
   """
   marketplaceListings - Look up Marketplace listings

   """
   class MarketplaceListingConnectionArgs(GQLArgsSet, GQLObject): 
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
      slugs: List[str]
      primaryCategoryOnly: bool
      withFreeTrialsOnly: bool

   _args: MarketplaceListingConnectionArgs


   type: MarketplaceListingConnection

class meta(GQLQuery):
   """
   meta - Return information about the GitHub instance

   """
   type: GitHubMetadata

class node(GQLQuery):
   """
   node - Fetches an object given its ID.

   """
   class NodeArgs(GQLArgsSet, GQLObject): 
      """
      id - ID of the object.

      """
      id: NonNull_ID

   _args: NodeArgs


   type: Node

class nodes(GQLQuery):
   """
   nodes - Lookup nodes by a list of IDs.

   """
   class NodeArgs(GQLArgsSet, GQLObject): 
      """
      ids - The list of node IDs.

      """
      ids: NonNull_List[NonNull_ID]

   _args: NodeArgs


   type: Node

class organization(GQLQuery):
   """
   organization - Lookup a organization by login.

   """
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      """
      login - The organization's login.

      """
      login: NonNull_str

   _args: OrganizationArgs


   type: Organization

class rateLimit(GQLQuery):
   """
   rateLimit - The client's rate limit information.

   """
   class RateLimitArgs(GQLArgsSet, GQLObject): 
      """
      dryRun - If true, calculate the cost for the query without evaluating it

      """
      dryRun: bool

   _args: RateLimitArgs


   type: RateLimit

class relay(GQLQuery):
   """
   relay - Hack to workaround https://github.com/facebook/relay/issues/112 re-exposing the root query object

   """
   type: None

class repository(GQLQuery):
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

class repositoryOwner(GQLQuery):
   """
   repositoryOwner - Lookup a repository owner (ie. either a User or an Organization) by login.

   """
   class RepositoryOwnerArgs(GQLArgsSet, GQLObject): 
      """
      login - The username to lookup the owner by.

      """
      login: NonNull_str

   _args: RepositoryOwnerArgs


   type: RepositoryOwner

class resource(GQLQuery):
   """
   resource - Lookup resource by a URL.

   """
   class UniformResourceLocatableArgs(GQLArgsSet, GQLObject): 
      """
      url - The URL.

      """
      url: NonNull_URI

   _args: UniformResourceLocatableArgs


   type: UniformResourceLocatable

class search(GQLQuery):
   """
   search - Perform a search across resources, returning a maximum of 1,000 results.

   """
   class SearchResultItemConnectionArgs(GQLArgsSet, GQLObject): 
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
      query: NonNull_str
      type: NonNull_SearchType

   _args: SearchResultItemConnectionArgs


   type: SearchResultItemConnection

class securityAdvisories(GQLQuery):
   """
   securityAdvisories - GitHub Security Advisories

   """
   class SecurityAdvisoryConnectionArgs(GQLArgsSet, GQLObject): 
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
      classifications: List[NonNull_SecurityAdvisoryClassification]
      after: str
      before: str
      first: int
      last: int

   _args: SecurityAdvisoryConnectionArgs


   type: SecurityAdvisoryConnection

class securityAdvisory(GQLQuery):
   """
   securityAdvisory - Fetch a Security Advisory by its GHSA ID

   """
   class SecurityAdvisoryArgs(GQLArgsSet, GQLObject): 
      """
      ghsaId - GitHub Security Advisory ID.

      """
      ghsaId: NonNull_str

   _args: SecurityAdvisoryArgs


   type: SecurityAdvisory

class securityVulnerabilities(GQLQuery):
   """
   securityVulnerabilities - Software Vulnerabilities documented by GitHub Security Advisories

   """
   class SecurityVulnerabilityConnectionArgs(GQLArgsSet, GQLObject): 
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
      severities: List[NonNull_SecurityAdvisorySeverity]
      classifications: List[NonNull_SecurityAdvisoryClassification]
      after: str
      before: str
      first: int
      last: int

   _args: SecurityVulnerabilityConnectionArgs


   type: SecurityVulnerabilityConnection

class sponsorables(GQLQuery):
   """
   sponsorables - Users and organizations who can be sponsored via GitHub Sponsors.

   """
   class SponsorableItemConnectionArgs(GQLArgsSet, GQLObject): 
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

   _args: SponsorableItemConnectionArgs


   type: SponsorableItemConnection

class topic(GQLQuery):
   """
   topic - Look up a topic by name.

   """
   class TopicArgs(GQLArgsSet, GQLObject): 
      """
      name - The topic's name.

      """
      name: NonNull_str

   _args: TopicArgs


   type: Topic

class user(GQLQuery):
   """
   user - Lookup a user by login.

   """
   class UserArgs(GQLArgsSet, GQLObject): 
      """
      login - The user's login.

      """
      login: NonNull_str

   _args: UserArgs


   type: User

class viewer(GQLQuery):
   """
   viewer - The currently authenticated user.

   """
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
