from typing import List
from pygqlmap import GQLMutation
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *


class NonNull_CreateReservedUserInput(CreateReservedUserInput): pass

class NonNull_CreateOwnershipUserInput(CreateOwnershipUserInput): pass

class NonNull_SingleFileUploadInput(SingleFileUploadInput): pass

class NonNull_TokenAuthenticationInput(TokenAuthenticationInput): pass

class NonNull_ClientEnvInput(ClientEnvInput): pass

class NonNull_PaymentInput(PaymentInput): pass

class NonNull_PayScheduledPaymentInput(PayScheduledPaymentInput): pass

class NonNull_OrderInput(OrderInput): pass

class NonNull_PayCapacityQuoteInput(PayCapacityQuoteInput): pass

class NonNull_UpdateUserInput(UpdateUserInput): pass

class NonNull_ChangeUserPasswordInput(ChangeUserPasswordInput): pass

class NonNull_PasswordResetConfirmInput(PasswordResetConfirmInput): pass

class NonNull_UpdateUserCRMInput(UpdateUserCRMInput): pass

class NonNull_AddressInput(AddressInput): pass

class NonNull_AuthenticationCreateAccountInput(AuthenticationCreateAccountInput): pass

class NonNull_DirectDebitInput(DirectDebitInput): pass

class NonNull_AuthLoginSessionInputType(AuthLoginSessionInputType): pass

class NonNull_UpdateSupplierQuotesInput(UpdateSupplierQuotesInput): pass

class NonNull_CreateAccountInput(CreateAccountInput): pass

class NonNull_ConsumptionInput(ConsumptionInput): pass

class NonNull_CreateMemberConsumptionEvidenceSubmissionInput(CreateMemberConsumptionEvidenceSubmissionInput): pass

class NonNull_ApproveMemberConsumptionEvidenceSubmissionInput(ApproveMemberConsumptionEvidenceSubmissionInput): pass

class NonNull_UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput(UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput): pass

class NonNull_AddMemberToCoopWaitingListInput(AddMemberToCoopWaitingListInput): pass

class NonNull_CreateMemberBeneficiaryInput(CreateMemberBeneficiaryInput): pass

class NonNull_UpdateMemberBeneficiaryInput(UpdateMemberBeneficiaryInput): pass

class NonNull_UpdateQuoteInput(UpdateQuoteInput): pass

class NonNull_ResponseInputType(ResponseInputType): pass

class NonNull_AddAdditionalWattsInputs(AddAdditionalWattsInputs): pass

class NonNull_CreateOrUpdateNewsInput(CreateOrUpdateNewsInput): pass

class NonNull_SingleNewsFileUploadInput(SingleNewsFileUploadInput): pass

class NonNull_CreateUserMemoInputs(CreateUserMemoInputs): pass

class NonNull_Upload(Upload): pass

class NonNull_CreateContactUsMessageInput(CreateContactUsMessageInput): pass

class NonNull_UserContactInput(UserContactInput): pass

class NonNull_CreateEmployerContactInput(CreateEmployerContactInput): pass

class NonNull_RequestCallBackInput(RequestCallBackInput): pass

class NonNull_QuoteInput(QuoteInput): pass

class NonNull_GiftCardInput(GiftCardInput): pass

class createReservedUser(GQLMutation):
   class CreateReservedUserArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateReservedUserInput

   _args: CreateReservedUserArgs


   type: CreateReservedUser

class createOwnershipUser(GQLMutation):
   class CreateOwnershipUserArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateOwnershipUserInput

   _args: CreateOwnershipUserArgs


   type: CreateOwnershipUser

class deleteCypressTestsData(GQLMutation):
   type: DeleteCypressTestsData

class updateActiveCoopStatus(GQLMutation):
   class UpdateActiveCoopStatusArgs(GQLArgsSet, GQLObject):
      status: NonNull_str

   _args: UpdateActiveCoopStatusArgs


   type: UpdateActiveCoopStatus

class singleFileUpload(GQLMutation):
   class SingleFileUploadArgs(GQLArgsSet, GQLObject):
      input: NonNull_SingleFileUploadInput

   _args: SingleFileUploadArgs


   type: SingleFileUpload

class tokenAuth(GQLMutation):
   class TokenAuthenticationOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_TokenAuthenticationInput

   _args: TokenAuthenticationOutputArgs


   type: TokenAuthenticationOutput

class imitateUser(GQLMutation):
   class TokenAuthenticationOutputArgs(GQLArgsSet, GQLObject):
      id: NonNull_str

   _args: TokenAuthenticationOutputArgs


   type: TokenAuthenticationOutput

class socialAuthLogin(GQLMutation):
   class SocialAuthLoginArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: SocialAuthLoginArgs


   type: SocialAuthLogin

class socialAuthCreateAccount(GQLMutation):
   class SocialAuthCreateAccountArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: SocialAuthCreateAccountArgs


   type: SocialAuthCreateAccount

class clientSession(GQLMutation):
   class ServerEnvOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_ClientEnvInput

   _args: ServerEnvOutputArgs


   type: ServerEnvOutput

class payScheduledPayment(GQLMutation):
   class PayScheduledPaymentResponseArgs(GQLArgsSet, GQLObject):
      payment: NonNull_PaymentInput
      scheduledPayment: NonNull_PayScheduledPaymentInput

   _args: PayScheduledPaymentResponseArgs


   type: PayScheduledPaymentResponse

class payOrder(GQLMutation):
   class PayOrderResponseArgs(GQLArgsSet, GQLObject):
      order: NonNull_OrderInput
      payment: NonNull_PaymentInput

   _args: PayOrderResponseArgs


   type: PayOrderResponse

class payCapacityQuote(GQLMutation):
   class PayCapacityQuoteResponseArgs(GQLArgsSet, GQLObject):
      payment: NonNull_PaymentInput
      quote: NonNull_PayCapacityQuoteInput

   _args: PayCapacityQuoteResponseArgs


   type: PayCapacityQuoteResponse

class payGiftCard(GQLMutation):
   class PayGiftCardResponseArgs(GQLArgsSet, GQLObject):
      payment: NonNull_PaymentInput

   _args: PayGiftCardResponseArgs


   type: PayGiftCardResponse

class cancelRefundPayment(GQLMutation):
   class ErrorArgs(GQLArgsSet, GQLObject):
      paymentIds: NonNull_list[NonNull_str]

   _args: ErrorArgs


   type: list_Error[Error]

class setDefaultPaymentMethod(GQLMutation):
   class SetDefaultPaymentMethodArgs(GQLArgsSet, GQLObject):
      paymentMethodId: NonNull_str

   _args: SetDefaultPaymentMethodArgs


   type: SetDefaultPaymentMethod

class createSetupIntent(GQLMutation):
   type: CreateSetupIntent

class confirmAndAddPaymentMethod(GQLMutation):
   class ConfirmAndAddPaymentMethodArgs(GQLArgsSet, GQLObject):
      paymentMethodId: NonNull_str

   _args: ConfirmAndAddPaymentMethodArgs


   type: ConfirmAndAddPaymentMethod

class deleteAlternatePaymentMethod(GQLMutation):
   class DeleteAlternatePaymentMethodArgs(GQLArgsSet, GQLObject):
      paymentMethodId: NonNull_str

   _args: DeleteAlternatePaymentMethodArgs


   type: DeleteAlternatePaymentMethod

class initialiseSignUpStateSession(GQLMutation):
   class InitialiseSignUpStateSessionArgs(GQLArgsSet, GQLObject):
      brandingName: str

   _args: InitialiseSignUpStateSessionArgs


   type: InitialiseSignUpStateSession

class removeSignUpStateSession(GQLMutation):
   type: RemoveSignUpStateSession

class updateUser(GQLMutation):
   class UpdateUserOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateUserInput

   _args: UpdateUserOutputArgs


   type: UpdateUserOutput

class updateUserPhoneNumber(GQLMutation):
   class UpdateUserPhoneNumberArgs(GQLArgsSet, GQLObject):
      phoneNumber: NonNull_str

   _args: UpdateUserPhoneNumberArgs


   type: UpdateUserPhoneNumber

class verifyEmail(GQLMutation):
   class VerifyEmailArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: VerifyEmailArgs


   type: VerifyEmail

class sendEmailVerification(GQLMutation):
   class SendEmailVerificationArgs(GQLArgsSet, GQLObject):
      email: NonNull_str
      path: NonNull_str

   _args: SendEmailVerificationArgs


   type: SendEmailVerification

class changeUserPassword(GQLMutation):
   class ChangeUserPasswordResponseArgs(GQLArgsSet, GQLObject):
      input: NonNull_ChangeUserPasswordInput

   _args: ChangeUserPasswordResponseArgs


   type: ChangeUserPasswordResponse

class changeUserEmail(GQLMutation):
   class ChangeUserEmailArgs(GQLArgsSet, GQLObject):
      email: NonNull_str

   _args: ChangeUserEmailArgs


   type: ChangeUserEmail

class passwordResetRequest(GQLMutation):
   class PasswordResetResponseArgs(GQLArgsSet, GQLObject):
      email: NonNull_str

   _args: PasswordResetResponseArgs


   type: PasswordResetResponse

class passwordResetConfirm(GQLMutation):
   class PasswordResetConfirmOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_PasswordResetConfirmInput

   _args: PasswordResetConfirmOutputArgs


   type: PasswordResetConfirmOutput

class updateUserCrm(GQLMutation):
   class UpdateUserCRMOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateUserCRMInput

   _args: UpdateUserCRMOutputArgs


   type: UpdateUserCRMOutput

class registrationUpdateUserPersonalDetails(GQLMutation):
   class RegistrationUpdateUserPersonalDetailsArgs(GQLArgsSet, GQLObject):
      firstName: NonNull_str
      lastName: NonNull_str
      phoneNumber: NonNull_str

   _args: RegistrationUpdateUserPersonalDetailsArgs


   type: RegistrationUpdateUserPersonalDetails

class registrationUpdateOrCreateMemberAddress(GQLMutation):
   class RegistrationUpdateOrCreateMemberAddressArgs(GQLArgsSet, GQLObject):
      addressInput: NonNull_AddressInput

   _args: RegistrationUpdateOrCreateMemberAddressArgs


   type: RegistrationUpdateOrCreateMemberAddress

class authenticationCreateAccount(GQLMutation):
   class AuthenticationCreateAccountOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_AuthenticationCreateAccountInput

   _args: AuthenticationCreateAccountOutputArgs


   type: AuthenticationCreateAccountOutput

class updateUserDirectDebit(GQLMutation):
   class UpdateUserDirectDebitArgs(GQLArgsSet, GQLObject):
      input: NonNull_DirectDebitInput

   _args: UpdateUserDirectDebitArgs


   type: UpdateUserDirectDebit

class authLoginSession(GQLMutation):
   class AuthLoginSessionResponseTypeArgs(GQLArgsSet, GQLObject):
      input: NonNull_AuthLoginSessionInputType

   _args: AuthLoginSessionResponseTypeArgs


   type: AuthLoginSessionResponseType

class authLogoutSession(GQLMutation):
   type: AuthLogoutSessionResponseType

class updateSupplierQuotes(GQLMutation):
   class UpdateSupplierQuotesArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateSupplierQuotesInput

   _args: UpdateSupplierQuotesArgs


   type: UpdateSupplierQuotes

class recordSwitchAlreadyInitiated(GQLMutation):
   type: RecordSwitchAlreadyInitiated

class createAccount(GQLMutation):
   class CreateAccountPayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateAccountInput

   _args: CreateAccountPayloadArgs


   type: CreateAccountPayload

class updateMemberAddress(GQLMutation):
   class UpdateMemberAddressPayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddressInput

   _args: UpdateMemberAddressPayloadArgs


   type: UpdateMemberAddressPayload

class updateMemberAddressNew(GQLMutation):
   class UpdateMemberAddressNewArgs(GQLArgsSet, GQLObject):
      line1: NonNull_str
      line2: NonNull_str
      postcode: NonNull_str
      town: NonNull_str

   _args: UpdateMemberAddressNewArgs


   type: UpdateMemberAddressNew

class updateMemberIsBusinessField(GQLMutation):
   class UpdateMemberIsBusinessFieldArgs(GQLArgsSet, GQLObject):
      isBusiness: NonNull_bool

   _args: UpdateMemberIsBusinessFieldArgs


   type: UpdateMemberIsBusinessField

class updateMemberConsumption(GQLMutation):
   class UpdateMemberConsumptionPayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_ConsumptionInput

   _args: UpdateMemberConsumptionPayloadArgs


   type: UpdateMemberConsumptionPayload

class updateMemberConsumptionNew(GQLMutation):
   class UpdateMemberConsumptionNewArgs(GQLArgsSet, GQLObject):
      consumptionKwh: NonNull_float

   _args: UpdateMemberConsumptionNewArgs


   type: UpdateMemberConsumptionNew

class updateMemberSupplierApiKey(GQLMutation):
   class UpdateMemberSupplierAPIKeyPayloadArgs(GQLArgsSet, GQLObject):
      apiKey: NonNull_str

   _args: UpdateMemberSupplierAPIKeyPayloadArgs


   type: UpdateMemberSupplierAPIKeyPayload

class connectToOctopusApi(GQLMutation):
   class ConnectToOctopusAPIPayloadArgs(GQLArgsSet, GQLObject):
      apiKey: NonNull_str

   _args: ConnectToOctopusAPIPayloadArgs


   type: ConnectToOctopusAPIPayload

class disconnectFromOctopusApi(GQLMutation):
   type: DisconnectFromOctopusAPIPayload

class updateOctopusApiConsumptionDataVisibility(GQLMutation):
   class UpdateOctopusApiConsumptionDataVisibilityPayloadArgs(GQLArgsSet, GQLObject):
      wantsToSeeOctopusApiConsumptionData: NonNull_bool

   _args: UpdateOctopusApiConsumptionDataVisibilityPayloadArgs


   type: UpdateOctopusApiConsumptionDataVisibilityPayload

class createMemberConsumptionEvidenceSubmission(GQLMutation):
   class CreateMemberConsumptionEvidenceSubmissionPayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateMemberConsumptionEvidenceSubmissionInput

   _args: CreateMemberConsumptionEvidenceSubmissionPayloadArgs


   type: CreateMemberConsumptionEvidenceSubmissionPayload

class approveMemberConsumptionEvidenceSubmission(GQLMutation):
   class ApproveMemberConsumptionEvidenceSubmissionPayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_ApproveMemberConsumptionEvidenceSubmissionInput

   _args: ApproveMemberConsumptionEvidenceSubmissionPayloadArgs


   type: ApproveMemberConsumptionEvidenceSubmissionPayload

class cancelMemberConsumptionEvidenceSubmission(GQLMutation):
   class CancelMemberConsumptionEvidenceSubmissionPayloadArgs(GQLArgsSet, GQLObject):
      submissionId: NonNull_str

   _args: CancelMemberConsumptionEvidenceSubmissionPayloadArgs


   type: CancelMemberConsumptionEvidenceSubmissionPayload

class updateMemberConsumptionEvidenceSubmissionAdminNote(GQLMutation):
   class UpdateMemberConsumptionEvidenceSubmissionAdminNotePayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateMemberConsumptionEvidenceSubmissionAdminNoteInput

   _args: UpdateMemberConsumptionEvidenceSubmissionAdminNotePayloadArgs


   type: UpdateMemberConsumptionEvidenceSubmissionAdminNotePayload

class addMemberToCoopWaitingList(GQLMutation):
   class AddMemberToCoopWaitingListPayloadArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddMemberToCoopWaitingListInput

   _args: AddMemberToCoopWaitingListPayloadArgs


   type: AddMemberToCoopWaitingListPayload

class removeMemberFromCoopWaitingList(GQLMutation):
   class RemoveMemberFromCoopWaitingListPayloadArgs(GQLArgsSet, GQLObject):
      waitingListPlaceId: NonNull_str

   _args: RemoveMemberFromCoopWaitingListPayloadArgs


   type: RemoveMemberFromCoopWaitingListPayload

class createMemberBeneficiary(GQLMutation):
   class CreateMemberBeneficiaryOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateMemberBeneficiaryInput

   _args: CreateMemberBeneficiaryOutputArgs


   type: CreateMemberBeneficiaryOutput

class updateMemberBeneficiary(GQLMutation):
   class UpdateMemberBeneficiaryOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateMemberBeneficiaryInput

   _args: UpdateMemberBeneficiaryOutputArgs


   type: UpdateMemberBeneficiaryOutput

class deleteMemberBeneficiary(GQLMutation):
   class DeleteMemberBeneficiaryOutputArgs(GQLArgsSet, GQLObject):
      beneficiaryId: NonNull_str

   _args: DeleteMemberBeneficiaryOutputArgs


   type: DeleteMemberBeneficiaryOutput

class updateMemberCommunityName(GQLMutation):
   class UpdateMemberCommunityNameArgs(GQLArgsSet, GQLObject):
      communityName: NonNull_str

   _args: UpdateMemberCommunityNameArgs


   type: UpdateMemberCommunityName

class updateQuote(GQLMutation):
   class UpdateQuoteArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateQuoteInput

   _args: UpdateQuoteArgs


   type: UpdateQuote

class createResponse(GQLMutation):
   """
   createResponse - Response referring to survey response

   """
   class ResponseTypeArgs(GQLArgsSet, GQLObject):
      input: NonNull_ResponseInputType

   _args: ResponseTypeArgs


   type: ResponseType

class addAdditionalWatts(GQLMutation):
   class AddAdditionalWattsArgs(GQLArgsSet, GQLObject):
      inputs: NonNull_AddAdditionalWattsInputs

   _args: AddAdditionalWattsArgs


   type: AddAdditionalWatts

class createOrUpdateNews(GQLMutation):
   class CreateOrUpdateNewsOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateOrUpdateNewsInput

   _args: CreateOrUpdateNewsOutputArgs


   type: CreateOrUpdateNewsOutput

class singleNewsFileUpload(GQLMutation):
   class SingleNewsFileUploadArgs(GQLArgsSet, GQLObject):
      input: NonNull_SingleNewsFileUploadInput

   _args: SingleNewsFileUploadArgs


   type: SingleNewsFileUpload

class deleteNews(GQLMutation):
   class DeleteNewsOutputArgs(GQLArgsSet, GQLObject):
      id: NonNull_str

   _args: DeleteNewsOutputArgs


   type: DeleteNewsOutput

class createNote(GQLMutation):
   class CreateUserMemoOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateUserMemoInputs

   _args: CreateUserMemoOutputArgs


   type: CreateUserMemoOutput

class uploadLightShowImage(GQLMutation):
   class UploadLightShowImageArgs(GQLArgsSet, GQLObject):
      coopMembershipId: NonNull_str
      image: NonNull_Upload

   _args: UploadLightShowImageArgs


   type: UploadLightShowImage

class createContactUsMessage(GQLMutation):
   class CreateContactUsMessageArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateContactUsMessageInput

   _args: CreateContactUsMessageArgs


   type: CreateContactUsMessage

class createUserContact(GQLMutation):
   class CreateUserContactArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserContactInput

   _args: CreateUserContactArgs


   type: CreateUserContact

class createEmployerContact(GQLMutation):
   class CreateEmployerContactOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateEmployerContactInput

   _args: CreateEmployerContactOutputArgs


   type: CreateEmployerContactOutput

class requestCallBack(GQLMutation):
   class RequestCallBackOutputArgs(GQLArgsSet, GQLObject):
      input: NonNull_RequestCallBackInput

   _args: RequestCallBackOutputArgs


   type: RequestCallBackOutput

class sendQuoteEmail(GQLMutation):
   class SendQuoteEmailArgs(GQLArgsSet, GQLObject):
      quoteInput: NonNull_QuoteInput
      subscribesToNewsletter: NonNull_bool
      userContactInput: NonNull_UserContactInput

   _args: SendQuoteEmailArgs


   type: SendQuoteEmail

class updateBuyer(GQLMutation):
   class UpdateBuyerArgs(GQLArgsSet, GQLObject):
      email: str

   _args: UpdateBuyerArgs


   type: UpdateBuyer

class addGiftCard(GQLMutation):
   class AddGiftCardArgs(GQLArgsSet, GQLObject):
      input: NonNull_GiftCardInput

   _args: AddGiftCardArgs


   type: AddGiftCard

class updateGiftCard(GQLMutation):
   class UpdateGiftCardArgs(GQLArgsSet, GQLObject):
      giftCardId: NonNull_str
      input: NonNull_GiftCardInput

   _args: UpdateGiftCardArgs


   type: UpdateGiftCard

class removeGiftCard(GQLMutation):
   class RemoveGiftCardArgs(GQLArgsSet, GQLObject):
      id: NonNull_str

   _args: RemoveGiftCardArgs


   type: RemoveGiftCard

class openGiftCard(GQLMutation):
   class OpenGiftCardArgs(GQLArgsSet, GQLObject):
      id: int

   _args: OpenGiftCardArgs


   type: OpenGiftCard

class verifyToken(GQLMutation):
   class VerifyArgs(GQLArgsSet, GQLObject):
      token: str

   _args: VerifyArgs


   type: Verify

class refreshToken(GQLMutation):
   class RefreshArgs(GQLArgsSet, GQLObject):
      token: str

   _args: RefreshArgs


   type: Refresh

class deleteTokenCookie(GQLMutation):
   type: DeleteJSONWebTokenCookie

class deleteRefreshTokenCookie(GQLMutation):
   type: DeleteRefreshTokenCookie


class Mutations(Enum):
   createReservedUser = createReservedUser
   createOwnershipUser = createOwnershipUser
   deleteCypressTestsData = deleteCypressTestsData
   updateActiveCoopStatus = updateActiveCoopStatus
   singleFileUpload = singleFileUpload
   tokenAuth = tokenAuth
   imitateUser = imitateUser
   socialAuthLogin = socialAuthLogin
   socialAuthCreateAccount = socialAuthCreateAccount
   clientSession = clientSession
   payScheduledPayment = payScheduledPayment
   payOrder = payOrder
   payCapacityQuote = payCapacityQuote
   payGiftCard = payGiftCard
   cancelRefundPayment = cancelRefundPayment
   setDefaultPaymentMethod = setDefaultPaymentMethod
   createSetupIntent = createSetupIntent
   confirmAndAddPaymentMethod = confirmAndAddPaymentMethod
   deleteAlternatePaymentMethod = deleteAlternatePaymentMethod
   initialiseSignUpStateSession = initialiseSignUpStateSession
   removeSignUpStateSession = removeSignUpStateSession
   updateUser = updateUser
   updateUserPhoneNumber = updateUserPhoneNumber
   verifyEmail = verifyEmail
   sendEmailVerification = sendEmailVerification
   changeUserPassword = changeUserPassword
   changeUserEmail = changeUserEmail
   passwordResetRequest = passwordResetRequest
   passwordResetConfirm = passwordResetConfirm
   updateUserCrm = updateUserCrm
   registrationUpdateUserPersonalDetails = registrationUpdateUserPersonalDetails
   registrationUpdateOrCreateMemberAddress = registrationUpdateOrCreateMemberAddress
   authenticationCreateAccount = authenticationCreateAccount
   updateUserDirectDebit = updateUserDirectDebit
   authLoginSession = authLoginSession
   authLogoutSession = authLogoutSession
   updateSupplierQuotes = updateSupplierQuotes
   recordSwitchAlreadyInitiated = recordSwitchAlreadyInitiated
   createAccount = createAccount
   updateMemberAddress = updateMemberAddress
   updateMemberAddressNew = updateMemberAddressNew
   updateMemberIsBusinessField = updateMemberIsBusinessField
   updateMemberConsumption = updateMemberConsumption
   updateMemberConsumptionNew = updateMemberConsumptionNew
   updateMemberSupplierApiKey = updateMemberSupplierApiKey
   connectToOctopusApi = connectToOctopusApi
   disconnectFromOctopusApi = disconnectFromOctopusApi
   updateOctopusApiConsumptionDataVisibility = updateOctopusApiConsumptionDataVisibility
   createMemberConsumptionEvidenceSubmission = createMemberConsumptionEvidenceSubmission
   approveMemberConsumptionEvidenceSubmission = approveMemberConsumptionEvidenceSubmission
   cancelMemberConsumptionEvidenceSubmission = cancelMemberConsumptionEvidenceSubmission
   updateMemberConsumptionEvidenceSubmissionAdminNote = updateMemberConsumptionEvidenceSubmissionAdminNote
   addMemberToCoopWaitingList = addMemberToCoopWaitingList
   removeMemberFromCoopWaitingList = removeMemberFromCoopWaitingList
   createMemberBeneficiary = createMemberBeneficiary
   updateMemberBeneficiary = updateMemberBeneficiary
   deleteMemberBeneficiary = deleteMemberBeneficiary
   updateMemberCommunityName = updateMemberCommunityName
   updateQuote = updateQuote
   createResponse = createResponse
   addAdditionalWatts = addAdditionalWatts
   createOrUpdateNews = createOrUpdateNews
   singleNewsFileUpload = singleNewsFileUpload
   deleteNews = deleteNews
   createNote = createNote
   uploadLightShowImage = uploadLightShowImage
   createContactUsMessage = createContactUsMessage
   createUserContact = createUserContact
   createEmployerContact = createEmployerContact
   requestCallBack = requestCallBack
   sendQuoteEmail = sendQuoteEmail
   updateBuyer = updateBuyer
   addGiftCard = addGiftCard
   updateGiftCard = updateGiftCard
   removeGiftCard = removeGiftCard
   openGiftCard = openGiftCard
   verifyToken = verifyToken
   refreshToken = refreshToken
   deleteTokenCookie = deleteTokenCookie
   deleteRefreshTokenCookie = deleteRefreshTokenCookie
