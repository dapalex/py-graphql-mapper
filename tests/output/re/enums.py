from enum import Enum

class ApprovalStatus(Enum):
   DEFAULT = None
   APPROVAL_NOT_REQUIRED = 'APPROVAL_NOT_REQUIRED'
   EVIDENCE_NEEDED = 'EVIDENCE_NEEDED'
   EVIDENCE_PENDING_APPROVAL = 'EVIDENCE_PENDING_APPROVAL'
   EVIDENCE_APPROVED = 'EVIDENCE_APPROVED'

class MembersMemberConsumptionEvidenceSubmissionStatusChoices(Enum):
   DEFAULT = None
   EVIDENCE_NEEDED = 'EVIDENCE_NEEDED' ##Evidence needed
   EVIDENCE_PENDING_APPROVAL = 'EVIDENCE_PENDING_APPROVAL' ##Evidence pending approval
   EVIDENCE_APPROVED = 'EVIDENCE_APPROVED' ##Evidence approved

class GenerationGenerationFarmGenerationTypeChoices(Enum):
   DEFAULT = None
   WIND = 'WIND' ##Windfarm
   SOL = 'SOL' ##Solarfarm

class GenerationGenerationFarmOperationalStatusChoices(Enum):
   DEFAULT = None
   NA = 'NA' ##N/A
   PRELIMINARY = 'PRELIMINARY' ##Prelimary
   PLANNING = 'PLANNING' ##Planning
   CONTRACTED = 'CONTRACTED' ##Contracted
   UNDER_CONSTRUCTION = 'UNDER_CONSTRUCTION' ##Under construction
   OPERATIONAL = 'OPERATIONAL' ##Operational
   SUSPENDED = 'SUSPENDED' ##Suspended
   DECOMMISSIONED = 'DECOMMISSIONED' ##Decommissioned
   CLOSED = 'CLOSED' ##Closed

class GenerationDataTitle(Enum):
   DEFAULT = None
   TODAY = 'TODAY'
   NEXT_4_DAYS = 'NEXT_4_DAYS'
   NEXT_14_DAYS = 'NEXT_14_DAYS'
   LAST_7_DAYS = 'LAST_7_DAYS'
   LAST_30_DAYS = 'LAST_30_DAYS'

class Period(Enum):
   DEFAULT = None
   Day = 'Day'
   Week = 'Week'
   Month = 'Month'
   Year = 'Year'

class CoopCoopStatusChoices(Enum):
   DEFAULT = None
   RESERVATIONS_OPEN = 'RESERVATIONS_OPEN' ##Reservations open
   RESERVATIONS_CLOSED = 'RESERVATIONS_CLOSED' ##Reservations closed
   OWNERSHIP_OPEN_RESERVED_MEMBERS_ONLY = 'OWNERSHIP_OPEN_RESERVED_MEMBERS_ONLY' ##Ownership open reserved members only
   OWNERSHIP_OPEN = 'OWNERSHIP_OPEN' ##Ownership open
   FULL = 'FULL' ##Full
   BACKFILL = 'BACKFILL' ##Backfill
   CLOSED = 'CLOSED' ##Closed

class PaymentsPaymentCategoryChoices(Enum):
   DEFAULT = None
   JOINING_FEE = 'JOINING_FEE' ##Ripple joining fee
   GIFT_VOUCHER = 'GIFT_VOUCHER' ##Gift Voucher
   ORDER = 'ORDER' ##Order

class InvoiceType(Enum):
   DEFAULT = None
   RESERVATION_RECEIPT = 'RESERVATION_RECEIPT'
   WATTAGE_AMOUNT = 'WATTAGE_AMOUNT'
   ARRANGEMENT_FEE = 'ARRANGEMENT_FEE'
   GIFT_VOUCHER = 'GIFT_VOUCHER'
   INVOICE = 'INVOICE'

class PaymentType(Enum):
   DEFAULT = None
   RESERVATION_FEE = 'RESERVATION_FEE'
   GIFT_VOUCHER = 'GIFT_VOUCHER'
   MONTHLY_INSTALMENT = 'MONTHLY_INSTALMENT'
   INITIAL_INSTALMENT = 'INITIAL_INSTALMENT'
   ONE_TIME_PAYMENT = 'ONE_TIME_PAYMENT'
   PAYMENT = 'PAYMENT'

class PaymentStatus(Enum):
   DEFAULT = None
   PAID = 'PAID'
   FAILED = 'FAILED'
   REFUNDED = 'REFUNDED'
   UPCOMING = 'UPCOMING'
   OVERDUE = 'OVERDUE'

class CrmUserMemoChannelChoices(Enum):
   DEFAULT = None
   DIRECT_EMAIL = 'DIRECT_EMAIL' ##DIRECT_EMAIl
   INFO = 'INFO' ##INFO
   HELP = 'HELP' ##HELP
   CONTACT_US = 'CONTACT_US' ##CONTACT_US
   EMPLOYER = 'EMPLOYER' ##EMPLOYER
   BUSINESS = 'BUSINESS' ##BUSINESS
   OTHER = 'OTHER' ##OTHER

class GetMemberOctopusConsumptionDataTitle(Enum):
   DEFAULT = None
   LAST_7_DAYS = 'LAST_7_DAYS'
   LAST_30_DAYS = 'LAST_30_DAYS'

class SurveyQuestionChoiceTypeChoices(Enum):
   DEFAULT = None
   MULTIPLE_CHOICE = 'MULTIPLE_CHOICE' ##multiple choice
   YES_NO = 'YES_NO' ##yes no
   RADIO = 'RADIO' ##radio
   TEXT = 'TEXT' ##text
   NUMBER = 'NUMBER' ##number

class StripePaymentType(Enum):
   DEFAULT = None
   CARD = 'CARD'

class CardBrandType(Enum):
   DEFAULT = None
   OTHER = 'OTHER'
   VISA = 'VISA'
   MASTERCARD = 'MASTERCARD'
