from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class DeleteRefreshTokenCookie(GQLObject):
   deleted: bool

class Refresh(GQLObject):
   payload: GenericScalar
   refreshExpiresIn: int
   token: str

class OpenGiftCard(GQLObject):
   errors: list[str]

class RecipientAddressInput(GQLObject):
   line1: str
   line2: str
   town: str
   postcode: str

class UpdateBuyer(GQLObject):
   id: int
   firstName: str
   lastName: str
   email: str
   isKnown: bool
   isLoggedIn: bool
   errors: list[str]

class RequestCallBackInput(GQLObject):
   firstName: str
   lastName: str
   phoneNumber: str
   companyName: str
   message: str
   pathname: str
   numberOfEmployees: str
   currentEnergySupplier: str
   annualConsumptionKwh: str
   numberOfSites: str

class CreateEmployerContactInput(GQLObject):
   firstname: str
   lastname: str
   email: str
   phone: str
   company: str
   numberOfEmployees: str
   currentEnergySupplier: str
   annualConsumptionKwh: str
   numberOfSites: str
   message: str
   pathname: str
   jobTitle: str

class UserContactInput(GQLObject):
   firstname: str
   lastname: str
   email: str

class CreateContactUsMessageInput(GQLObject):
   name: str
   email: str
   message: str

class CreateUserMemoInputs(GQLObject):
   note: str
   userId: str
   channel: str
   open: bool
   actionRequired: bool

class SingleNewsFileUploadInput(GQLObject):
   file: Upload
   category: str
   newsId: str

class CreateOrUpdateNewsInput(GQLObject):
   id: str
   title: str
   body: str
   hidden: bool
   coopId: str

class ResponseInputType(GQLObject):
   question: str
   surveyResponse: str
   email: str
   multipleChoiceAnswer: list[str]
   radioChoiceAnswer: str
   textFieldAnswer: str
   numberAnswer: int
   yesNoAnswer: str
   surveyId: str

class UpdateMemberBeneficiaryInput(GQLObject):
   beneficiaryId: str
   nominatedPerson: str
   email: str
   phone: str
   line1: str
   line2: str
   town: str
   postcode: str

class AddMemberToCoopWaitingListInput(GQLObject):
   coopId: str
   generationRequestedKwh: int

class ApproveMemberConsumptionEvidenceSubmissionInput(GQLObject):
   submissionId: str
   approvedEvidence: float
   adminNote: str

class AuthLogoutSessionResponseType(GQLObject):
   logoutSuccessful: bool

class AuthLoginSessionResponseType(GQLObject):
   id: int
   loginSuccessful: bool

class UpdateUserCRMInput(GQLObject):
   id: int
   email: str

class ChangeUserPasswordInput(GQLObject):
   currentPassword: str
   newPassword: str
   confirmNewPassword: str

class PayCapacityQuoteInput(GQLObject):
   capacityQuoteId: int
   instalments: int

class GetKeyValuePair(GQLObject):
   key: str
   value: str
   expiry: str

class TokenAuthenticationInput(GQLObject):
   email: str
   password: str

class SingleFileUpload(GQLObject):
   success: bool

class UpdateQuoteInput(GQLObject):
   electricityConsumptionAnnual: int
   voucherCodes: list[str]
   monetaryValue: int
   capacity: int

class UpdateSupplierQuotesInput(GQLObject):
   electricityAnnualStandardKwh: float
   hasEconomy7Meter: bool
   electricityAnnualDayKwh: int
   electricityAnnualNightKwh: int
   switchesGas: bool
   gasAnnualKwh: int
   hasSmartMeter: bool
   postcode: str
   isSwitchDelayed: bool
   switchDisabled: bool
   delayedSwitchDate: Date
   requiresManualSwitch: bool
   supplier: int
   selectedQuoteCode: str
   isAlreadyWithPartnerSupplier: bool
   isAlreadyWithBrandedSupplier: bool
   wantsToSeeTariffs: bool
   switchesToAnotherPartnerSupplier: bool
   electricitySupplierId: int
   acknowledgesTariffsWillBeDifferentInTheFuture: bool
   acknowledgesHeWillLoseSavingsIfHeDoesntSwitchOnTime: bool
   acknowledgesHeNeedsToContactTheSupplierToUpdateAddress: bool

class BillingAddress(GQLObject):
   line1: str
   line2: str
   town: str
   county: str
   postcode: str
   country: str

class OctopusApiAddressInput(GQLObject):
   line1: str
   line2: str
   line3: str
   town: str
   county: str
   postcode: str
   mpans: list[str]
   mprn: str
   gsp: str
   economy7: bool
   prepaidElectricityMeter: bool
   display: str

class AuthenticationCreateAccountInput(GQLObject):
   email: str
   password: str
   path: str

class BillSavingsForecastDataPoint(GQLObject):
   id: ID
   year: int
   pencePerKiloWattHour: float

class Ambassador(GQLObject):
   id: ID
   code: str
   name: str
   showBanner: bool
   headline: str
   subtext: str
   backgroundColor: str
   textColor: str
   logo: str

class Sender(GQLObject):
   id: ID
   isAnonymous: bool
   firstName: str
   lastName: str

class Buyer(GQLObject):
   id: int
   firstName: str
   lastName: str
   email: str
   isKnown: bool
   isLoggedIn: bool

class CalculateUnitsForCostInput(GQLObject):
   currency: str
   instalments: int
   cost: int
   sku: str

class CalculatedPaymentLine(GQLObject):
   amount: int
   units: int
   netAmount: int
   taxAmount: int
   sku: str
   costUnits: int
   unitCost: int
   description: str
   message: str
   params: JSONString
   error: str

class Tag(GQLObject):
   id: ID
   name: str

class CalculatorMark(GQLObject):
   consumptionMet: float
   costTotal: int
   expectedGeneration: float

class PublicGenerationDataSet(GQLObject):
   netPowerOutputKwh: float
   dateTime: str
   windSpeedMph: float
   savingsForPeriod: float
   estimatedCo2Saved: float
   estimatedTreesSaved: float

class GetMemberOctopusConsumptionDataSetElement(GQLObject):
   consumptionKwh: float
   dateTime: str

class Error(GQLObject):
   code: str
   message: str

class SearchCountInput(GQLObject):
   searchTerm: str

class PaginationInput(GQLObject):
   offset: int
   limit: int

class GetMemberMissingInvoiceData(GQLObject):
   capacity: float
   coopId: str
   costOfWatts: float
   costOfFeesNet: float
   costOfFeesTax: float
   invoiceDate: str

class VoucherPayload(GQLObject):
   code: str

class InsightsChartDataInput(GQLObject):
   genFarmId: str
   startDate: str
   endDate: str
   period: Period

class InsightsChartDataInputObject(GQLObject):
   genFarmId: str
   period: Period
   startDate: str
   endDate: str

class InsightsChartDataSet(GQLObject):
   windSpeedMph: float
   generationKwh: float
   savings: float
   fromTime: DateTime
   toTime: DateTime

class Address(GQLObject):
   id: ID
   town: str
   country: str

class UserType(GQLObject):
   id: ID
   firstName: str
   lastName: str
   email: str
   phoneNumber: str

class OctopusApiAddress(GQLObject):
   line1: str
   line2: str
   line3: str
   town: str
   county: str
   postcode: str
   mpans: list[str]
   mprn: str
   gsp: str
   economy7: bool
   prepaidElectricityMeter: bool
   display: str

class ImageGeneral(GQLObject):
   id: ID
   name: str
   description: str
   url: str
