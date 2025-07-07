from src.core import BaseEnum


class CurrencyEnum(BaseEnum):
    """
    Enum for supported currencies.

    Attributes:
        BRL: Brazilian Real.
        USD: United States Dollar.
        EUR: Euro.
    """
    BRL = "brl"
    USD = "usd"
    EUR = "eur"

class PaymentMethodTypeEnum(BaseEnum):
    """
    Enum for supported payment method types.

    https://docs.stripe.com/api/payment_methods

    Attributes:
        ACSS_DEBIT: ACSS Debit payment method.
        AFFIRM: Affirm payment method.
        AFTERPAY_CLEARPAY: Afterpay Clearpay payment method.
        ALIPAY: Alipay payment method.
        ALMA: Alma payment method.
        AMAZON_PAY: Amazon Pay payment method.
        AU_BECS_DEBIT: AU BECS Debit payment method.
        BACS_DEBIT: BACS Debit payment method.
        BANCONTACT: Bancontact payment method.
        BILLIE: Billie payment method.
        BLIK: BLIK payment method.
        BOLETO: Boleto payment method.
        CARD: Card payment method.
        CARD_PRESENT: Card Present payment method.
        CASH_APP: Cash App payment method.
        CRYPTO: Crypto payment method.
        CUSTOMER_BALANCE: Customer Balance payment method.
        EPS: EPS payment method.
        FPX: FPX payment method.
        GIROPAY: Giropay payment method.
        GRABPAY: GrabPay payment method.
        IDEAL: iDEAL payment method.
        INTERAC_PRESENT: Interac Present payment method.
        KAKAO_PAY: Kakao Pay payment method.
        KLARNA: Klarna payment method.
        KONBINI: Konbini payment method.
        KR_CARD: KR Card payment method.
        LINK: Link payment method.
        MOBILEPAY: MobilePay payment method.
        MULTIBANCO: Multibanco payment method.
        NAVER_PAY: Naver Pay payment method.
        NZ_BANK_ACCOUNT: NZ Bank Account payment method.
        OXXO: OXXO payment method.
        P24: P24 payment method.
        PAYCO: Payco payment method.
        PAY_NOW: PayNow payment method.
        PAYPAL: PayPal payment method.
        PIX: Pix payment method.
        PROMPT_PAY: PromptPay payment method.
        REVOLUT_PAY: Revolut Pay payment method.
        SAMSUNG_PAY: Samsung Pay payment method.
        SATIS_PAY: Satispay payment method.
        SEPA_DEBIT: SEPA Debit payment method.
        SOFORT: Sofort payment method.
        SWISH: Swish payment method.
        TWINT: Twint payment method.
        US_BANK_ACCOUNT: US Bank Account payment method.
        WECHAT_PAY: WeChat Pay payment method.
        ZIP: Zip payment method.
    """
    ACSS_DEBIT = "acss_debit"
    AFFIRM = "affirm"
    AFTERPAY_CLEARPAY = "afterpay_clearpay"
    ALIPAY = "alipay"
    ALMA = "alma"
    AMAZON_PAY = "amazon_pay"
    AU_BECS_DEBIT = "au_becs_debit"
    BACS_DEBIT = "bacs_debit"
    BANCONTACT = "bancontact"
    BILLIE = "billie"
    BLIK = "blik"
    BOLETO = "boleto"
    CARD = "card"
    CARD_PRESENT = "card_present"
    CASH_APP = "cashapp"
    CRYPTO = "crypto"
    CUSTOMER_BALANCE = "customer_balance"
    EPS = "eps"
    FPX = "fpx"
    GIROPAY = "giropay"
    GRABPAY = "grabpay"
    IDEAL = "ideal"
    INTERAC_PRESENT = "interac_present"
    KAKAO_PAY = "kakao_pay"
    KLARNA = "klarna"
    KONBINI = "konbini"
    KR_CARD = "kr_card"
    LINK = "link"
    MOBILEPAY = "mobilepay"
    MULTIBANCO = "multibanco"
    NAVER_PAY = "naver_pay"
    NZ_BANK_ACCOUNT = "nz_bank_account"
    OXXO = "oxxo"
    P24 = "p24"
    PAYCO = "payco"
    PAY_NOW = "paynow"
    PAYPAL = "paypal"
    PIX = "pix"
    PROMPT_PAY = "promptpay"
    REVOLUT_PAY = "revolut_pay"
    SAMSUNG_PAY = "samsung_pay"
    SATIS_PAY = "satispay"
    SEPA_DEBIT = "sepa_debit"
    SOFORT = "sofort"
    SWISH = "swish"
    TWINT = "twint"
    US_BANK_ACCOUNT = "us_bank_account"
    WECHAT_PAY = "wechat_pay"
    ZIP = "zip"


class SubscriptionInterval(BaseEnum):
    """
    Enum for subscription intervals.

    Attributes:
        MONTH: Monthly subscription.
        YEAR: Yearly subscription.
        WEEK: Weekly subscription.
        DAY: Daily subscription.
    """
    MONTH = "month"
    YEAR = "year"
    WEEK = "week"
    DAY = "day"


class SubscriptionStatus(BaseEnum):
    """
    Enum for subscription statuses.

    Attributes:
        ACTIVE: Subscription is active.
        CANCELED: Subscription is canceled.
        PAST_DUE: Subscription is past due.
        UNPAID: Subscription is unpaid.
        TRIALING: Subscription is in trial period.
        INCOMPLETE: Subscription is incomplete.
        INCOMPLETE_EXPIRED: Subscription is incomplete and expired.
    """
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"
    PAUSED = "paused"
    UNPAID = "unpaid"
    TRIALING = "trialing"
    INCOMPLETE = "incomplete"
    INCOMPLETE_EXPIRED = "incomplete_expired"