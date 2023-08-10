from typing import Generic, Union, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from typing import NewType
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class DeleteJSONWebTokenCookie(GQLObject):
   deleted: bool

class Verify(GQLObject):
   payload: GenericScalar

class RemoveGiftCard(GQLObject):
   errors: list[str]

class SenderInput(GQLObject):
   firstName: str
   lastName: str
   isAnonymous: bool

class QuoteInput(GQLObject):
   costTotal: float
   percentageOfConsumptionCovered: float
   firstYearBillSavings: float
   projectLifespanBillSavings: float
   annualCo2Savings: float
   projectLifespanInYears: int

class RequestCallBackOutput(GQLObject):
   success: bool

class EmployerContact(GQLObject):
   id: ID
   company: str
   jobTitle: str
   numberOfEmployees: str
   firstname: str
   lastname: str
   phone: str
   email: str
   currentEnergySupplier: str
   annualConsumptionKwh: str
   numberOfSites: str
   message: str
   pathname: str

class UserContact(GQLObject):
   firstname: str
   lastname: str
   email: str

class CreateContactUsMessage(GQLObject):
   id: int

class DeleteNewsOutput(GQLObject):
   success: bool

class SingleNewsFileUpload(GQLObject):
   success: bool

class AddAdditionalWattsInputs(GQLObject):
   memberId: str
   capacity: float
   coopId: str
   costOfWatts: float
   costOfFeesNet: float
   costOfFeesTax: float
   paid: bool
   addInvoiceOnly: bool
   due: str
   invoiceDate: str
   externalInvoiceUrl: str

class ResponseType(GQLObject):
   id: int
   surveyResponseId: int

class CreateMemberBeneficiaryInput(GQLObject):
   nominatedPerson: str
   email: str
   phone: str
   line1: str
   line2: str
   town: str
   postcode: str

class UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput(GQLObject):
   submissionId: str
   adminNote: str

class ConsumptionEvidenceInput(GQLObject):
   file: Upload
   consumption: int

class AuthLoginSessionInputType(GQLObject):
   email: str
   password: str

class DirectDebitInput(GQLObject):
   accountName: str
   accountSortCode: str
   accountNumber: str
   paymentDay: str

class PasswordResetConfirmInput(GQLObject):
   password: str
   passwordConfirm: str
   token: str
   uidb64: str

class UpdateUserInput(GQLObject):
   id: int
   phoneNumber: str

class PayScheduledPaymentInput(GQLObject):
   paymentId: int

class SetKeyValuePair(GQLObject):
   key: str
   value: str
   expiry: str
   command: str

class SingleFileUploadInput(GQLObject):
   file: Upload
   category: str

class UserInput(GQLObject):
   firstName: str
   lastName: str
   email: str
   phoneNumber: str
   password: str
   passwordConfirm: str

class ConsumptionInput(GQLObject):
   electricityAnnual: float
   fromCalculator: bool
   peopleCount: int
   bedroomsCount: int
   hasElectricVehicle: bool
   hasElectricHeating: bool
   hasHeatPump: bool
   hasSolarPanels: bool
   solarPanelsCapacity: float
   acknowledgesToProvideBillEvidence: bool

class PaymentLineInput(GQLObject):
   amount: int
   units: int
   taxAmount: int
   sku: str
   description: str
   params: JSONString

class StripePaymentInput(GQLObject):
   paymentMethodId: str
   paymentIntentId: str

class RegistrationUpdateUserPersonalDetailsInput(GQLObject):
   firstName: str
   lastName: str
   phoneNumber: str

class BillSavingsForecastReference(GQLObject):
   id: ID
   name: str
   href: str

class ReferAFriendPayload(GQLObject):
   hasReferral: bool
   name: str

class RecipientAddress(GQLObject):
   id: int
   line1: str
   line2: str
   town: str
   county: str
   postcode: str
   country: str

class Image(GQLObject):
   id: int
   name: str
   description: str
   thumbnailUrl: str
   bannerUrl: str
   cardUrl: str
   headerUrl: str

class PaymentMethod(GQLObject):
   paymentMethodId: str
   isDefaultPaymentMethod: bool
   paymentType: StripePaymentType
   isCardExpired: bool
   cardBrandType: CardBrandType
   cardExpMonth: str
   cardExpYear: str
   cardLast4: str

class CalculatePaymentLineInput(GQLObject):
   units: int
   amount: int
   sku: str
   params: JSONString

class ValidatedVoucherInfo(GQLObject):
   voucherCode: str
   isValid: bool
   value: int
   message: str

class CoopTimelineProgression(GQLObject):
   timelineProgression: int

class CoopStats(GQLObject):
   name: str
   code: str
   totalCapacity: str
   allocatedCapacity: str
   members: int

class ChoiceType(GQLObject):
   id: ID
   text: str

class SupplierMemberInfoInput(GQLObject):
   apiKey: str
   memberAccountId: str

class FilterInput(GQLObject):
   filterByBusinessMembers: bool
   filterByApprovalStatus: ApprovalStatus

class SearchInput(GQLObject):
   offset: int
   limit: int
   searchTerm: str

class GetMemberMissingInvoiceDataInputs(GQLObject):
   memberId: str
   coopId: str

class Invoice(GQLObject):
   id: ID
   createdAt: DateTime
   description: str
   net: int
   gross: int
   refunded: bool
   category: str
   invoiceUrl: str
   invoiceType: InvoiceType

class DocumentTag(GQLObject):
   id: ID
   name: str

class UserError(GQLObject):
   field: str
   message: str

class InsightsChartCumulativeData(GQLObject):
   cumulativeSavings: float
   cumulativeGenerationKwh: float
   averageWindSpeedMph: float

class DataSetElement(GQLObject):
   netPowerOutputKwh: float
   dateTime: str
   isForecastData: bool
   savingsForPeriod: float

class Currency(GQLObject):
   id: int
   code: str
   precision: int
   symbol: str

class ConsumptionEvidence(GQLObject):
   id: ID
   createdAt: DateTime
   consumption: int
   name: str
   file: str
   fileSizeFormatted: str
   fileUrl: str
   contentType: str

class Supplier(GQLObject):
   id: ID
   name: str
   isRipplePartner: bool
   highlights: str
   logoUrl: str

class Badge(GQLObject):
   id: ID
   name: str
   code: str
   description: str
   imageUrl: str

class GiftCardDesign(GQLObject):
   id: ID
   name: str
   description: str
   postCardCost: int
   image: Image
   currency: Currency

class Recipient(GQLObject):
   id: ID
   email: str
   firstName: str
   lastName: str
   address: RecipientAddress

class GiftCard(GQLObject):
   id: ID
   design: GiftCardDesign
   sender: Sender
   recipient: Recipient
   isSendPostCard: bool
   deliveryDate: Date
   message: str
   amount: int
   currency: Currency
   code: str
   amountLocale: str
   voucherCode: str

class list_UserError(list, UserError): pass

class UpdateGiftCard(GQLObject):
   userErrors: list_UserError[UserError]
   giftCard: GiftCard

class RecipientInput(GQLObject):
   firstName: str
   lastName: str
   email: str
   address: RecipientAddressInput

class GiftCardInput(GQLObject):
   amount: int
   deliveryDate: str
   designId: str
   message: str
   sender: SenderInput
   recipient: RecipientInput
   isSendPostCard: bool

class AddGiftCard(GQLObject):
   userErrors: list_UserError[UserError]
   giftCard: GiftCard

class list_Error(list, Error): pass

class SendQuoteEmail(GQLObject):
   userContact: UserContact
   errors: list_Error[Error]

class CreateEmployerContactOutput(GQLObject):
   employerContact: EmployerContact
   userErrors: list_UserError[UserError]

class CreateUserContact(GQLObject):
   userContact: UserContact
   userErrors: list_UserError[UserError]

class MemberAddress(GQLObject):
   id: ID
   town: str
   country: str
   line1: str
   line2: str
   county: str
   postcode: str
   mpan: str
   mprn: str
   manuallyEntered: bool
   requiresManualSwitch: bool
   hasPrepaidMeter: bool
   selectedFromDropdown: OctopusApiAddress

class list_ConsumptionEvidence(list, ConsumptionEvidence): pass

class MemberConsumptionEvidenceSubmission(GQLObject):
   id: ID
   createdAt: DateTime
   status: MembersMemberConsumptionEvidenceSubmissionStatusChoices
   approvedEvidence: float
   reviewEvidence: float
   memberNote: str
   evidences: list_ConsumptionEvidence[ConsumptionEvidence]
   adminNote: str
   approvedDate: Date
   approvedBy: UserType

class list_MemberConsumptionEvidenceSubmission(list, MemberConsumptionEvidenceSubmission): pass

class MemberConsumptionApproval(GQLObject):
   id: ID
   approvalStatus: ApprovalStatus
   evidenceSubmissions: list_MemberConsumptionEvidenceSubmission[MemberConsumptionEvidenceSubmission]
   latestSubmission: MemberConsumptionEvidenceSubmission
   expectedGenerationKwh: float
   totalApprovedConsumptionKwh: float
   totalUnapprovedConsumptionKwh: float

class list_DataSetElement(list, DataSetElement): pass

class GenerationData(GQLObject):
   title: GenerationDataTitle
   dataSet: list_DataSetElement[DataSetElement]

class list_InsightsChartDataSet(list, InsightsChartDataSet): pass

class InsightsChartDataOutput(GQLObject):
   chartData: list_InsightsChartDataSet[InsightsChartDataSet]
   cumulativeData: InsightsChartCumulativeData
   input: InsightsChartDataInputObject
   userErrors: list_UserError[UserError]

class GenerationDataPoint(GQLObject):
   id: ID
   generationFarm: NewType('GenerationFarm', GQLObject) ## Circular Reference for GenerationFarm
   timestamp: DateTime
   windSpeedAvg: Decimal
   generatorSpeedAvg: Decimal
   bladeAngleAvg: Decimal
   nacellePositionNorth: Decimal

class list_GenerationData(list, GenerationData): pass

class NonNull_InsightsChartDataInput(InsightsChartDataInput): pass

class OXRUE_InsightsChartDataOutput_Field(InsightsChartDataOutput):
   class InsightsChartDataOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_InsightsChartDataInput

   _args: InsightsChartDataOutputArgs



class GenerationFarm(GQLObject):
   id: ID
   currency: Currency
   name: str
   address: Address
   longitude: float
   latitude: float
   isLocationConfirmed: bool
   model: str
   capacity: BigInt
   generationType: GenerationGenerationFarmGenerationTypeChoices
   operationalStatus: GenerationGenerationFarmOperationalStatusChoices
   startDate: Date
   generationData: list_GenerationData[GenerationData]
   lightShowImage: str
   capacityToGenerationFactor: float
   insightsChartData: OXRUE_InsightsChartDataOutput_Field
   latestGenerationDataPoint: GenerationDataPoint

class list_DocumentTag(list, DocumentTag): pass

class Document(GQLObject):
   id: ID
   updatedAt: DateTime
   name: str
   category: str
   subcategory: str
   description: str
   documentTags: list_DocumentTag[DocumentTag]

class DocumentVersion(GQLObject):
   id: ID
   document: Document
   version: str
   documentUrl: str

class list_DocumentVersion(list, DocumentVersion): pass

class Coop(GQLObject):
   id: ID
   currency: Currency
   name: str
   code: str
   description: str
   generationfarm: GenerationFarm
   status: CoopCoopStatusChoices
   wattageSku: str
   active: bool
   firstYearEstimatedBillSavingsPerWattHour: float
   estimatedBillSavingsPerWattHour: float
   maxCapacityPerMember: BigInt
   minCapacityPerMember: BigInt
   publicCloseDate: DateTime
   percentageFunded: int
   timelineProgression: int
   isAvailableForLocalPurchase: bool
   documents: list_DocumentVersion[DocumentVersion]
   maxGenerationPerMember: int
   minGenerationPerMember: int
   costTotalPerWattHour: float
   localPurchasePostcodes: list[str]

class Voucher(GQLObject):
   id: int
   code: str
   expiry: DateTime
   displayName: str
   payload: VoucherPayload
   error: str
   valid: bool
   allocated: bool

class list_Voucher(list, Voucher): pass

class CoopCapacityQuote(GQLObject):
   id: ID
   currency: Currency
   coop: Coop
   capacity: BigInt
   ownershipMultiplier: float
   capacityCost: int
   arrangementFee: int
   vouchers: list_Voucher[Voucher]
   costTotal: int
   costTotalLocale: str
   electricityConsumptionAnnual: float
   expectedGenerationAnnual: int
   paymentTotal: int
   paymentTotalLocale: str
   instalments: int
   instalmentAmount1: int
   instalmentAmount1Locale: str
   instalmentAmountN: int
   instalmentAmountNLocale: str
   vouchersAmount: int
   vouchersAmountLocale: str
   billSavingsAnnualEstimate: int
   co2SavingsAnnualEstimate: int
   plantedTreesSavingsAnnualEstimate: int
   shareCount: int
   arrangementFeeLocale: str
   arrangementFeeTax: int
   arrangementFeeTaxLocale: str
   arrangementFee1: int
   arrangementFeeLocale1: str
   arrangementFeeTax1: int
   arrangementFeeTaxLocale1: str

class MemberSupplierQuotes(GQLObject):
   id: ID
   supplier: Supplier
   member: NewType('Member', GQLObject) ## Circular Reference for Member
   isAlreadyWithPartnerSupplier: bool
   isAlreadyWithBrandedSupplier: bool
   wantsToSeeTariffs: bool
   switchesToAnotherPartnerSupplier: bool
   electricitySupplierId: int
   postcode: str
   hasEconomy7Meter: bool
   electricityAnnualDayKwh: int
   electricityAnnualNightKwh: int
   gasAnnualKwh: int
   supplierQuotesJson: str
   selectedQuoteCode: str
   switchesGas: bool
   requiresManualSwitch: bool
   isSwitchDelayed: bool
   switchFailed: bool
   switchDisabled: bool
   delayedSwitchDate: Date
   initiated: bool
   acknowledgesTariffsWillBeDifferentInTheFuture: bool
   acknowledgesHeWillLoseSavingsIfHeDoesntSwitchOnTime: bool
   acknowledgesHeNeedsToContactTheSupplierToUpdateAddress: bool
   selectedTariff: JSONString
   currency: Currency
   electricityAnnualStandardKwh: float

class SignUpState(GQLObject):
   id: ID
   createdAt: DateTime
   updatedAt: DateTime
   branding: NewType('Branding', GQLObject) ## Circular Reference for Branding
   address: MemberAddress
   consumption: MemberConsumptionApproval
   quote: CoopCapacityQuote
   supplierQuotes: MemberSupplierQuotes

class list_GQLObject(list, GQLObject): pass

class list_SignUpState(list, SignUpState): pass

class Branding(GQLObject):
   id: ID
   createdAt: DateTime
   updatedAt: DateTime
   cssClassName: str
   displayName: str
   heroImage: ImageGeneral
   howItWorksImage: ImageGeneral
   howDoesItWorkPanelImageFirst: ImageGeneral
   howDoesItWorkPanelImageSecond: ImageGeneral
   howDoesItWorkPanelImageThird: ImageGeneral
   supplier: Supplier
   memberSet: list_GQLObject[GQLObject] ## Circular Reference for Member
   signUpState: list_SignUpState[SignUpState]

class MemberNextOfKin(GQLObject):
   id: ID
   member: NewType('Member', GQLObject) ## Circular Reference for Member
   nominatedPerson: str
   email: str
   phone: str
   line1: str
   line2: str
   town: str
   postcode: str

class MemberConsumption(GQLObject):
   id: ID
   member: NewType('Member', GQLObject) ## Circular Reference for Member
   fromCalculator: bool
   peopleCount: int
   bedroomsCount: int
   hasElectricVehicle: bool
   hasElectricHeating: bool
   hasHeatPump: bool
   hasSolarPanels: bool
   solarPanelsCapacity: float
   acknowledgesToProvideBillEvidence: bool
   electricityAnnualKwh: float

class MemberInvoice(GQLObject):
   id: ID
   quote: CoopCapacityQuote
   category: str
   invoiceUrl: str
   description: str
   gross: int
   net: int

class MemberDocument(GQLObject):
   id: ID
   createdAt: DateTime
   member: NewType('Member', GQLObject) ## Circular Reference for Member
   category: str
   comments: str
   file: str
   documentUrl: str

class MemberSupplier(GQLObject):
   id: ID
   supplier: Supplier
   accountIdentifier: str
   personalApiKey: str
   octopusMpan: str
   octopusMeterSerialNumber: str
   isOctopusApiConnectionVerified: bool
   wantsToSeeOctopusApiConsumptionData: bool

class CoopWaitingList(GQLObject):
   id: ID
   coop: Coop

class MemberCoopWaitingListPlace(GQLObject):
   id: ID
   waitingList: CoopWaitingList
   generationRequestedKwh: int

class list_Badge(list, Badge): pass

class list_MemberNextOfKin(list, MemberNextOfKin): pass

class list_MemberInvoice(list, MemberInvoice): pass

class list_MemberCoopWaitingListPlace(list, MemberCoopWaitingListPlace): pass

class Member(GQLObject):
   id: ID
   registrationCompleted: bool
   communityName: str
   isBusiness: bool
   businessName: str
   businessRegistrationNumber: str
   fullyChargedPreregistered: bool
   badges: list_Badge[Badge]
   branding: Branding
   beneficiaries: list_MemberNextOfKin[MemberNextOfKin]
   address: MemberAddress
   consumption: MemberConsumption
   invoices: list_MemberInvoice[MemberInvoice]
   memberships: list_GQLObject[GQLObject] ## Circular Reference for CoopMembership
   capacityOwnedTotal: BigInt
   ownershipPercentageTotal: float
   memberDocument: MemberDocument
   investmentTotal: int
   billSavingsAcrossAllProjects: int
   expectedGenerationAnnualTotal: BigInt
   hasReservedInActiveCoop: bool
   dateOfReservationInActiveCoop: Date
   dateOfLastSharePurchase: Date
   hasBoughtSharesInActiveCoop: bool
   hasBoughtSharesInGraigFatha: bool
   hasBoughtSharesInKirkHill: bool
   hasBoughtSharesInMultipleCoops: bool
   isSuppliedByOctopusEnergy: bool
   currentMemberSupplier: MemberSupplier
   waitingListPlaces: list_MemberCoopWaitingListPlace[MemberCoopWaitingListPlace]

class CoopMembership(GQLObject):
   id: ID
   createdAt: DateTime
   member: Member
   coop: Coop
   reservedCapacity: BigInt
   ownershipPercentage: float
   investmentTotal: int
   expectedGenerationAnnualTotal: BigInt
   billSavingsFirstYearEstimateTotal: int
   billSavingsForProjectLifespan: int
   firstOwnershipPurchaseDate: Date
   capacity: BigInt
   lightShowImage: str

class UploadLightShowImage(GQLObject):
   coopMembership: CoopMembership
   errors: list_Error[Error]

class Permission(GQLObject):
   id: ID
   name: str
   codename: str
   groupSet: list_GQLObject[GQLObject] ## Circular Reference for Group
   userSet: list_GQLObject[GQLObject] ## Circular Reference for User

class list_Permission(list, Permission): pass

class Group(GQLObject):
   id: ID
   name: str
   permissions: list_Permission[Permission]
   userSet: list_GQLObject[GQLObject] ## Circular Reference for User

class list_Invoice(list, Invoice): pass

class Payment(GQLObject):
   id: ID
   updatedAt: DateTime
   currency: Currency
   amount: int
   description: str
   category: PaymentsPaymentCategoryChoices
   failed: bool
   paid: bool
   refunded: bool
   dueAt: Date
   amountLocale: str
   memberInvoices: list_MemberInvoice[MemberInvoice]
   invoices: list_Invoice[Invoice]
   paymentType: PaymentType
   status: PaymentStatus
   project: str
   date: Date

class DirectDebit(GQLObject):
   id: ID
   createdAt: DateTime
   updatedAt: DateTime
   user: NewType('User', GQLObject) ## Circular Reference for User
   accountName: str
   accountSortCode: str
   accountNumber: str
   paymentDay: str

class Tracking(GQLObject):
   id: ID
   user: NewType('User', GQLObject) ## Circular Reference for User
   recommendedBy: NewType('User', GQLObject) ## Circular Reference for User

class list_Group(list, Group): pass

class list_Payment(list, Payment): pass

class list_Tracking(list, Tracking): pass

class User(GQLObject):
   id: ID
   firstName: str
   lastName: str
   groups: list_Group[Group]
   isStaff: bool
   isActive: bool
   isGuest: bool
   dateJoined: DateTime
   isEmailVerified: bool
   createdAt: DateTime
   updatedAt: DateTime
   email: str
   phoneNumber: str
   member: Member
   payments: list_Payment[Payment]
   directDebit: DirectDebit
   referred: list_Tracking[Tracking]
   isSuperuser: bool
   apiKey: str
   consumptionApproval: MemberConsumptionApproval

class UserMemo(GQLObject):
   id: ID
   createdAt: DateTime
   updatedAt: DateTime
   email: str
   note: str
   open: bool
   actionRequired: bool
   channel: CrmUserMemoChannelChoices
   deadline: DateTime
   createdBy: User
   assignedTo: User

class CreateUserMemoOutput(GQLObject):
   memo: UserMemo
   errors: list_Error[Error]

class NewsDocument(GQLObject):
   id: ID
   createdAt: DateTime
   news: NewType('News', GQLObject) ## Circular Reference for News
   category: str
   comments: str
   file: str
   documentUrl: str

class list_NewsDocument(list, NewsDocument): pass

class News(GQLObject):
   id: ID
   title: str
   body: str
   publishDate: DateTime
   hidden: bool
   coop: Coop
   newsDocuments: list_NewsDocument[NewsDocument]

class CreateOrUpdateNewsOutput(GQLObject):
   errors: list_Error[Error]
   news: News

class UpdateQuote(GQLObject):
   quote: CoopCapacityQuote
   errors: list_Error[Error]

class UpdateMemberCommunityName(GQLObject):
   member: Member
   userErrors: list_UserError[UserError]

class UpdateMemberBeneficiaryOutput(GQLObject):
   beneficiary: MemberNextOfKin
   userErrors: list_UserError[UserError]

class CreateMemberBeneficiaryOutput(GQLObject):
   beneficiary: MemberNextOfKin
   userErrors: list_UserError[UserError]

class AddMemberToCoopWaitingListPayload(GQLObject):
   userErrors: list_UserError[UserError]
   waitingListPlace: MemberCoopWaitingListPlace

class ApproveMemberConsumptionEvidenceSubmissionPayload(GQLObject):
   evidenceSubmission: MemberConsumptionEvidenceSubmission
   userErrors: list_UserError[UserError]

class CreateMemberConsumptionEvidenceSubmissionPayload(GQLObject):
   evidenceSubmission: MemberConsumptionEvidenceSubmission
   userErrors: list_UserError[UserError]

class UpdateOctopusApiConsumptionDataVisibilityPayload(GQLObject):
   memberSupplier: MemberSupplier
   userErrors: list_UserError[UserError]

class DisconnectFromOctopusAPIPayload(GQLObject):
   memberSupplier: MemberSupplier
   userErrors: list_UserError[UserError]

class ConnectToOctopusAPIPayload(GQLObject):
   memberSupplier: MemberSupplier
   userErrors: list_UserError[UserError]

class UpdateMemberSupplierAPIKeyPayload(GQLObject):
   memberSupplier: MemberSupplier
   userErrors: list_UserError[UserError]

class UpdateMemberConsumptionNew(GQLObject):
   consumption: MemberConsumption
   userErrors: list_UserError[UserError]

class UpdateMemberConsumptionPayload(GQLObject):
   consumption: MemberConsumption
   errors: list_Error[Error]

class UpdateMemberAddressNew(GQLObject):
   address: MemberAddress
   userErrors: list_UserError[UserError]

class UpdateMemberAddressPayload(GQLObject):
   address: MemberAddress
   errors: list_Error[Error]

class CreateAccountPayload(GQLObject):
   user: UserType
   member: Member
   errors: list_Error[Error]

class AuthenticationCreateAccountOutput(GQLObject):
   user: UserType
   userErrors: list_UserError[UserError]

class RegistrationUpdateOrCreateMemberAddress(GQLObject):
   address: MemberAddress
   userErrors: list_UserError[UserError]

class RegistrationUpdateUserPersonalDetails(GQLObject):
   user: User
   userErrors: list_UserError[UserError]

class UpdateUserCRMOutput(GQLObject):
   user: User
   errors: list_Error[Error]

class PasswordResetConfirmOutput(GQLObject):
   errors: list_Error[Error]
   user: User

class ChangeUserEmail(GQLObject):
   user: User
   errors: list_Error[Error]

class UpdateUserPhoneNumber(GQLObject):
   user: User
   userErrors: list_UserError[UserError]

class UpdateUserOutput(GQLObject):
   user: User
   errors: list_Error[Error]

class StripePaymentResponse(GQLObject):
   requiresAction: bool
   intentClientSecret: str
   errors: list_Error[Error]

class PaymentResponse(GQLObject):
   stripePaymentResponse: StripePaymentResponse
   errors: list_Error[Error]

class Product(GQLObject):
   id: ID
   currency: Currency
   sku: str
   name: str
   description: str
   cost: int
   costUnits: int
   taxPercent: int

class OrderLine(GQLObject):
   id: ID
   product: Product
   units: int
   taxAmount: int

class list_OrderLine(list, OrderLine): pass

class Order(GQLObject):
   id: ID
   totalNetAmount: int
   currency: Currency
   dueAt: DateTime
   status: str
   orderLines: list_OrderLine[OrderLine]

class list_Order(list, Order): pass

class PayOrderResponse(GQLObject):
   paymentResponse: PaymentResponse
   order: Order
   instalmentOrders: list_Order[Order]

class ScheduledPayment(GQLObject):
   id: ID
   amount: int
   description: str
   category: PaymentsPaymentCategoryChoices
   failed: bool
   paid: bool
   refunded: bool
   dueAt: Date
   amountLocale: str
   memberInvoices: list_MemberInvoice[MemberInvoice]

class PayScheduledPaymentResponse(GQLObject):
   paymentResponse: PaymentResponse
   payment: ScheduledPayment

class list_SetKeyValuePair(list, SetKeyValuePair): pass

class ServerEnvOutput(GQLObject):
   store: list_SetKeyValuePair[SetKeyValuePair]
   environment: str
   serverId: str
   serverVersion: str
   errors: list_Error[Error]

class UpdateActiveCoopStatus(GQLObject):
   coop: Coop
   userErrors: list_UserError[UserError]

class AddressInput(GQLObject):
   postcode: str
   line1: str
   line2: str
   town: str
   county: str
   country: str
   mpan: str
   mprn: str
   manuallyEntered: bool
   selectedFromDropdown: OctopusApiAddressInput
   requiresManualSwitch: bool
   hasPrepaidMeter: bool

class CreateAccountInput(GQLObject):
   user: UserInput
   isBusiness: bool
   businessName: str

class PaymentInput(GQLObject):
   uniquePaymentId: str
   description: str
   totalAmount: int
   totalTaxAmount: int
   payAmount: int
   voucherAmount: int
   balanceCreditAmount: int
   balanceDebitAmount: int
   currency: str
   stripePayment: StripePaymentInput
   billingAddress: BillingAddress
   email: str
   voucherCodes: list[str]

class list_PaymentLineInput(list, PaymentLineInput): pass

class InstalmentInput(GQLObject):
   description: str
   amount: int
   taxAmount: int
   instalmentDates: list[Date]
   instalments: int
   lines: list_PaymentLineInput[PaymentLineInput]

class OrderInput(GQLObject):
   currency: str
   lines: list_PaymentLineInput[PaymentLineInput]
   instalments: InstalmentInput

class PayOrderInput(GQLObject):
   payment: PaymentInput
   order: OrderInput

class CreateOwnershipUserInput(GQLObject):
   createAddress: AddressInput
   createSupplierQuotes: UpdateSupplierQuotesInput
   createConsumption: ConsumptionInput
   createQuote: UpdateQuoteInput
   createAccount: CreateAccountInput
   payOrder: PayOrderInput

class CreateOwnershipUser(GQLObject):
   user: User
   userErrors: list_UserError[UserError]

class CreateReservedUserInput(GQLObject):
   createAccount: AuthenticationCreateAccountInput
   updateDetails: RegistrationUpdateUserPersonalDetailsInput
   createAddress: AddressInput
   payOrder: PayOrderInput

class CreateReservedUser(GQLObject):
   user: User
   userErrors: list_UserError[UserError]

class list_BillSavingsForecastDataPoint(list, BillSavingsForecastDataPoint): pass

class list_BillSavingsForecastReference(list, BillSavingsForecastReference): pass

class BillSavingsForecast(GQLObject):
   id: ID
   name: str
   coop: Coop
   isDefault: bool
   description: str
   dataPoints: list_BillSavingsForecastDataPoint[BillSavingsForecastDataPoint]
   references: list_BillSavingsForecastReference[BillSavingsForecastReference]
   paybackPeriodInYears: int
   firstYearPencePerKiloWattHour: float
   totalPencePerKiloWattHour: float

class list_BillSavingsForecast(list, BillSavingsForecast): pass

class BillSavingsForecastsChartData(GQLObject):
   forecasts: list_BillSavingsForecast[BillSavingsForecast]
   defaultForecast: BillSavingsForecast
   maxDataPointPencePerKiloWattHour: float

class Amount(GQLObject):
   currency: Currency
   amount: int
   localeAmount: str

class list_GiftCard(list, GiftCard): pass

class Basket(GQLObject):
   items: list_GiftCard[GiftCard]
   totalAmount: Amount

class list_PaymentMethod(list, PaymentMethod): pass

class PaymentMethodPayload(GQLObject):
   paymentMethods: list_PaymentMethod[PaymentMethod]
   isDefaultCardExpired: bool
   showPaymentMethods: bool
   userErrors: list_UserError[UserError]

class list_CalculatedPaymentLine(list, CalculatedPaymentLine): pass

class CalculateUnitsForCost(GQLObject):
   totalNetAmount: int
   totalTaxAmount: int
   instalments: int
   totalAmount: int
   currency: Currency
   orderLines: list_CalculatedPaymentLine[CalculatedPaymentLine]
   errors: list_Error[Error]

class PaymentPlan(GQLObject):
   totalAmount: int
   totalNetAmount: int
   totalTaxAmount: int
   balanceAmountDebit: int
   balanceAmountCredit: int
   balanceAmountNew: int
   payAmount: int
   orderLines: list_CalculatedPaymentLine[CalculatedPaymentLine]

class InstalmentPaymentPlan(GQLObject):
   totalAmount: int
   totalNetAmount: int
   totalTaxAmount: int
   instalments: int
   instalmentDates: list[Date]
   initialPayment: PaymentPlan
   instalmentPayment: PaymentPlan

class list_ValidatedVoucherInfo(list, ValidatedVoucherInfo): pass

class CalculatePayOrder(GQLObject):
   voucherCodes: list_ValidatedVoucherInfo[ValidatedVoucherInfo]
   balanceAmount: int
   voucherAmount: int
   currency: Currency
   singlePaymentPlan: PaymentPlan
   instalmentPaymentPlan: InstalmentPaymentPlan
   errors: list_Error[Error]

class list_News(list, News): pass

class NewsOutput(GQLObject):
   errors: list_Error[Error]
   news: list_News[News]

class QuoteCalculator(GQLObject):
   consumption: float
   minimum: CalculatorMark
   maximum: CalculatorMark
   sliderGenerationStep: float

class list_GetMemberOctopusConsumptionDataSetElement(list, GetMemberOctopusConsumptionDataSetElement): pass

class GetMemberOctopusConsumptionData(GQLObject):
   title: GetMemberOctopusConsumptionDataTitle
   dataSet: list_GetMemberOctopusConsumptionDataSetElement[GetMemberOctopusConsumptionDataSetElement]

class list_GetMemberOctopusConsumptionData(list, GetMemberOctopusConsumptionData): pass

class GetMemberOctopusConsumptionInfo(GQLObject):
   data: list_GetMemberOctopusConsumptionData[GetMemberOctopusConsumptionData]
   userErrors: list_UserError[UserError]

class SupplierMemberInfo(GQLObject):
   member: Member
   errors: list_Error[Error]

class list_UserMemo(list, UserMemo): pass

class UserCRM(GQLObject):
   user: User
   memo: list_UserMemo[UserMemo]

class SearchCountAndFilterInput(GQLObject):
   search: SearchCountInput
   filter: FilterInput

class SearchAndFilterInput(GQLObject):
   search: SearchInput
   filter: FilterInput

class EmailInfo(GQLObject):
   discount: bool
   discountMessage: str
   errors: list_Error[Error]

class list_ChoiceType(list, ChoiceType): pass

class QuestionType(GQLObject):
   id: ID
   question: str
   choiceType: SurveyQuestionChoiceTypeChoices
   choices: list_ChoiceType[ChoiceType]
   order: str
   hidden: bool

class list_QuestionType(list, QuestionType): pass

class SurveyType(GQLObject):
   id: ID
   name: str
   pathName: str
   questions: list_QuestionType[QuestionType]
   forMembersOnly: bool
   secondsUntilDisplay: int
   exact: bool

class list_PublicGenerationDataSet(list, PublicGenerationDataSet): pass

class PublicGenerationData(GQLObject):
   title: GenerationDataTitle
   dataSet: list_PublicGenerationDataSet[PublicGenerationDataSet]

class list_Tag(list, Tag): pass

class Faq(GQLObject):
   id: ID
   question: str
   answer: str
   tags: list_Tag[Tag]

class SavingsData(GQLObject):
   currency: Currency
   month: str
   year: str
   savings: float
   referredSavings: float
   generation: float
   co2Saved: float
   treeEquivalent: int

class CumulativeSavingsData(GQLObject):
   currency: Currency
   savings: float
   generation: float
   co2Saved: float
   lastUpdate: str

class list_CalculatePaymentLineInput(list, CalculatePaymentLineInput): pass

class CalculateOrderPaymentInput(GQLObject):
   balanceAmount: int
   currency: str
   voucherCodes: list[str]
   instalments: int
   orderLines: list_CalculatePaymentLineInput[CalculatePaymentLineInput]

class DeleteCypressTestsData(GQLObject):
   userErrors: list_UserError[UserError]

class TokenAuthenticationOutput(GQLObject):
   token: str
   errors: list_Error[Error]

class SocialAuthLogin(GQLObject):
   userErrors: list_UserError[UserError]

class SocialAuthCreateAccount(GQLObject):
   userErrors: list_UserError[UserError]

class list_GetKeyValuePair(list, GetKeyValuePair): pass

class ClientEnvInput(GQLObject):
   store: list_GetKeyValuePair[GetKeyValuePair]
   siteUrl: str
   path: str
   query: str
   referrerUrl: str
   clientId: str
   clientVersion: str

class PayCapacityQuoteResponse(GQLObject):
   paymentResponse: PaymentResponse
   switchError: str

class PayGiftCardResponse(GQLObject):
   paymentResponse: PaymentResponse

class SetDefaultPaymentMethod(GQLObject):
   success: bool
   userErrors: list_UserError[UserError]

class CreateSetupIntent(GQLObject):
   clientSecret: str
   userErrors: list_UserError[UserError]

class ConfirmAndAddPaymentMethod(GQLObject):
   success: bool
   userErrors: list_UserError[UserError]

class DeleteAlternatePaymentMethod(GQLObject):
   success: bool
   userErrors: list_UserError[UserError]

class InitialiseSignUpStateSession(GQLObject):
   signUpState: SignUpState

class RemoveSignUpStateSession(GQLObject):
   errors: list_Error[Error]

class VerifyEmail(GQLObject):
   errors: list_Error[Error]

class SendEmailVerification(GQLObject):
   user: User

class ChangeUserPasswordResponse(GQLObject):
   errors: list_Error[Error]

class PasswordResetResponse(GQLObject):
   errors: list_Error[Error]

class UpdateUserDirectDebit(GQLObject):
   directDebit: DirectDebit

class UpdateSupplierQuotes(GQLObject):
   supplierQuotes: MemberSupplierQuotes

class RecordSwitchAlreadyInitiated(GQLObject):
   errors: list_Error[Error]

class UpdateMemberIsBusinessField(GQLObject):
   member: Member

class list_ConsumptionEvidenceInput(list, ConsumptionEvidenceInput): pass

class CreateMemberConsumptionEvidenceSubmissionInput(GQLObject):
   files: list_ConsumptionEvidenceInput[ConsumptionEvidenceInput]
   note: str

class CancelMemberConsumptionEvidenceSubmissionPayload(GQLObject):
   userErrors: list_UserError[UserError]

class UpdateMemberConsumptionEvidenceSubmissionAdminNotePayload(GQLObject):
   adminNote: str
   userErrors: list_UserError[UserError]

class RemoveMemberFromCoopWaitingListPayload(GQLObject):
   userErrors: list_UserError[UserError]

class DeleteMemberBeneficiaryOutput(GQLObject):
   userErrors: list_UserError[UserError]

class AddAdditionalWatts(GQLObject):
   errors: list_Error[Error]
