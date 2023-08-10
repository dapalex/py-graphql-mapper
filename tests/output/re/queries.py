from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class NonNull_GetMemberMissingInvoiceDataInputs(GetMemberMissingInvoiceDataInputs): pass

class NonNull_PaginationInput(PaginationInput): pass

class NonNull_SearchInput(SearchInput): pass

class NonNull_SearchCountInput(SearchCountInput): pass

class list_Coop(list, Coop): pass

class NonNull_SearchAndFilterInput(SearchAndFilterInput): pass

class list_User(list, User): pass

class NonNull_SearchCountAndFilterInput(SearchCountAndFilterInput): pass

class list_Supplier(list, Supplier): pass

class list_OctopusApiAddress(list, OctopusApiAddress): pass

class NonNull_SupplierMemberInfoInput(SupplierMemberInfoInput): pass

class list_SurveyType(list, SurveyType): pass

class list_PublicGenerationData(list, PublicGenerationData): pass

class list_Faq(list, Faq): pass

class list_Currency(list, Currency): pass

class list_Product(list, Product): pass

class NonNull_CalculateOrderPaymentInput(CalculateOrderPaymentInput): pass

class NonNull_CalculateUnitsForCostInput(CalculateUnitsForCostInput): pass

class list_GiftCardDesign(list, GiftCardDesign): pass

class version(GQLQuery):
   type: str

class tribeUrl(GQLQuery):
   type: str

class me(GQLQuery):
   type: User

class branding(GQLQuery):
   type: Branding

class publicPageBranding(GQLQuery):
   class BrandingArgs(GQLArgsSet, GQLObject):
      brand: NonNull_str

   _args: BrandingArgs


   type: Branding

class getMissingInvoiceData(GQLQuery):
   class GetMemberMissingInvoiceDataArgs(GQLArgsSet, GQLObject):
      input: NonNull_GetMemberMissingInvoiceDataInputs

   _args: GetMemberMissingInvoiceDataArgs


   type: GetMemberMissingInvoiceData

class allNews(GQLQuery):
   class NewsArgs(GQLArgsSet, GQLObject):
      input: NonNull_PaginationInput

   _args: NewsArgs


   type: list_News[News]

class searchNews(GQLQuery):
   class NewsArgs(GQLArgsSet, GQLObject):
      input: NonNull_SearchInput

   _args: NewsArgs


   type: list_News[News]

class searchNewsCount(GQLQuery):
   class intArgs(GQLArgsSet, GQLObject):
      input: NonNull_SearchCountInput

   _args: intArgs


   type: int

class getNewsItem(GQLQuery):
   class NewsArgs(GQLArgsSet, GQLObject):
      id: NonNull_str

   _args: NewsArgs


   type: News

class allNewsCount(GQLQuery):
   type: int

class allCoops(GQLQuery):
   type: list_Coop[Coop]

class searchUsers(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject):
      input: NonNull_SearchAndFilterInput

   _args: UserArgs


   type: list_User[User]

class searchUsersCount(GQLQuery):
   class intArgs(GQLArgsSet, GQLObject):
      input: NonNull_SearchCountAndFilterInput

   _args: intArgs


   type: int

class getUser(GQLQuery):
   class UserCRMArgs(GQLArgsSet, GQLObject):
      id: NonNull_str

   _args: UserCRMArgs


   type: UserCRM

class supplier(GQLQuery):
   class SupplierArgs(GQLArgsSet, GQLObject):
      id: NonNull_str

   _args: SupplierArgs


   type: Supplier

class partnerSuppliers(GQLQuery):
   type: list_Supplier[Supplier]

class addressLookup(GQLQuery):
   class OctopusApiAddressArgs(GQLArgsSet, GQLObject):
      postcode: NonNull_str

   _args: OctopusApiAddressArgs


   type: list_OctopusApiAddress[OctopusApiAddress]

class mpanSupplier(GQLQuery):
   class SupplierArgs(GQLArgsSet, GQLObject):
      mpan: NonNull_str

   _args: SupplierArgs


   type: Supplier

class mprnSupplier(GQLQuery):
   class SupplierArgs(GQLArgsSet, GQLObject):
      mprn: NonNull_str

   _args: SupplierArgs


   type: Supplier

class member(GQLQuery):
   type: Member

class pendingSupplierQuotes(GQLQuery):
   type: MemberSupplierQuotes

class supplierMemberInfo(GQLQuery):
   class SupplierMemberInfoArgs(GQLArgsSet, GQLObject):
      input: NonNull_SupplierMemberInfoInput

   _args: SupplierMemberInfoArgs


   type: SupplierMemberInfo

class address(GQLQuery):
   type: MemberAddress

class consumption(GQLQuery):
   type: MemberConsumption

class checkEmail(GQLQuery):
   class EmailInfoArgs(GQLArgsSet, GQLObject):
      input: NonNull_str

   _args: EmailInfoArgs


   type: EmailInfo

class getMemberOctopusConsumption(GQLQuery):
   type: GetMemberOctopusConsumptionInfo

class memberConsumptionApproval(GQLQuery):
   type: MemberConsumptionApproval

class getSurvey(GQLQuery):
   type: list_SurveyType[SurveyType]

class generationData(GQLQuery):
   type: list_PublicGenerationData[PublicGenerationData]

class coop(GQLQuery):
   type: Coop

class pendingQuote(GQLQuery):
   type: CoopCapacityQuote

class activeCoopStats(GQLQuery):
   type: CoopStats

class quoteCalculator(GQLQuery):
   class QuoteCalculatorArgs(GQLArgsSet, GQLObject):
      consumptionKwh: NonNull_float

   _args: QuoteCalculatorArgs


   type: QuoteCalculator

class coopTimelineProgression(GQLQuery):
   class CoopTimelineProgressionArgs(GQLArgsSet, GQLObject):
      coopCode: NonNull_str

   _args: CoopTimelineProgressionArgs


   type: CoopTimelineProgression

class getNews(GQLQuery):
   type: NewsOutput

class faqs(GQLQuery):
   """
   faqs - if you want to display all faqs, pass an empty string into tag

   """
   class FaqArgs(GQLArgsSet, GQLObject):
      tag: str

   _args: FaqArgs


   type: list_Faq[Faq]

class searchFaqs(GQLQuery):
   class FaqArgs(GQLArgsSet, GQLObject):
      search: NonNull_str

   _args: FaqArgs


   type: list_Faq[Faq]

class monthlySavingsData(GQLQuery):
   class SavingsDataArgs(GQLArgsSet, GQLObject):
      date: NonNull_str

   _args: SavingsDataArgs


   type: SavingsData

class cumulativeSavingsData(GQLQuery):
   type: CumulativeSavingsData

class currencies(GQLQuery):
   class CurrencyArgs(GQLArgsSet, GQLObject):
      codes: NonNull_list[str]

   _args: CurrencyArgs


   type: list_Currency[Currency]

class currency(GQLQuery):
   class CurrencyArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: CurrencyArgs


   type: Currency

class payments(GQLQuery):
   type: list_Payment[Payment]

class products(GQLQuery):
   type: list_Product[Product]

class orders(GQLQuery):
   type: list_Order[Order]

class calculateOrder(GQLQuery):
   class CalculatePayOrderArgs(GQLArgsSet, GQLObject):
      input: NonNull_CalculateOrderPaymentInput

   _args: CalculatePayOrderArgs


   type: CalculatePayOrder

class calculateUnitsForCost(GQLQuery):
   class CalculateUnitsForCostArgs(GQLArgsSet, GQLObject):
      input: NonNull_CalculateUnitsForCostInput

   _args: CalculateUnitsForCostArgs


   type: CalculateUnitsForCost

class getPaymentMethods(GQLQuery):
   type: PaymentMethodPayload

class checkVouchers(GQLQuery):
   class strArgs(GQLArgsSet, GQLObject):
      codes: NonNull_list[str]

   _args: strArgs


   type: str

class vouchers(GQLQuery):
   class VoucherArgs(GQLArgsSet, GQLObject):
      codes: NonNull_list[str]

   _args: VoucherArgs


   type: list_Voucher[Voucher]

class buyer(GQLQuery):
   type: Buyer

class giftCardDesigns(GQLQuery):
   type: list_GiftCardDesign[GiftCardDesign]

class basket(GQLQuery):
   type: Basket

class ambassador(GQLQuery):
   type: Ambassador

class referAFriend(GQLQuery):
   type: ReferAFriendPayload

class billSavingsForecastsChartData(GQLQuery):
   type: BillSavingsForecastsChartData


class Queries(Enum):
   version = version
   tribeUrl = tribeUrl
   me = me
   branding = branding
   publicPageBranding = publicPageBranding
   getMissingInvoiceData = getMissingInvoiceData
   allNews = allNews
   searchNews = searchNews
   searchNewsCount = searchNewsCount
   getNewsItem = getNewsItem
   allNewsCount = allNewsCount
   allCoops = allCoops
   searchUsers = searchUsers
   searchUsersCount = searchUsersCount
   getUser = getUser
   supplier = supplier
   partnerSuppliers = partnerSuppliers
   addressLookup = addressLookup
   mpanSupplier = mpanSupplier
   mprnSupplier = mprnSupplier
   member = member
   pendingSupplierQuotes = pendingSupplierQuotes
   supplierMemberInfo = supplierMemberInfo
   address = address
   consumption = consumption
   checkEmail = checkEmail
   getMemberOctopusConsumption = getMemberOctopusConsumption
   memberConsumptionApproval = memberConsumptionApproval
   getSurvey = getSurvey
   generationData = generationData
   coop = coop
   pendingQuote = pendingQuote
   activeCoopStats = activeCoopStats
   quoteCalculator = quoteCalculator
   coopTimelineProgression = coopTimelineProgression
   getNews = getNews
   faqs = faqs
   searchFaqs = searchFaqs
   monthlySavingsData = monthlySavingsData
   cumulativeSavingsData = cumulativeSavingsData
   currencies = currencies
   currency = currency
   payments = payments
   products = products
   orders = orders
   calculateOrder = calculateOrder
   calculateUnitsForCost = calculateUnitsForCost
   getPaymentMethods = getPaymentMethods
   checkVouchers = checkVouchers
   vouchers = vouchers
   buyer = buyer
   giftCardDesigns = giftCardDesigns
   basket = basket
   ambassador = ambassador
   referAFriend = referAFriend
   billSavingsForecastsChartData = billSavingsForecastsChartData
