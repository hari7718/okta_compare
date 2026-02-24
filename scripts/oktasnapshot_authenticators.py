import logging

from scripts.extract_authenticators import get_authenticators

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("okta_compare")


def _allowed_for_label(value):
    if not value:
        return "Not Available"
    normalized = str(value).lower()
    if normalized == "any":
        return "Authentication and recovery"
    if normalized == "recovery":
        return "Recovery in password policy rules"
    if normalized == "authentication":
        return "Authentication"
    return value


def _method_enabled(value):
    if isinstance(value, dict):
        if "enabled" in value:
            return bool(value.get("enabled"))
        if "status" in value:
            return str(value.get("status")).upper() == "ACTIVE"
        return True
    return bool(value)


def _phone_methods(settings):
    methods = settings.get("methods") or settings.get("channels") or {}
    allowed = []
    if _method_enabled(methods.get("voice")):
        allowed.append("Voice call")
    if _method_enabled(methods.get("sms")):
        allowed.append("SMS")
    return ", ".join(allowed) if allowed else "Not Available"


def get_authenticators_view(domain_url, api_token):
    logger.info("Fetching authenticators for OktaView.")
    authenticators = get_authenticators(domain_url, api_token) or []
    rows = []
    for auth in authenticators:
        key = (auth.get("key") or "").lower()
        auth_type = (auth.get("type") or "").lower()
        settings = auth.get("settings", {}) or {}
        row = {
            "Name": auth.get("name") or auth.get("label"),
            "Key": auth.get("key"),
            "Type": auth.get("type"),
            "Status": auth.get("status"),
        }

        if key == "email" or auth_type == "email":
            row.update({
                "Allowed For": _allowed_for_label(settings.get("allowedFor")),
                "Token Lifetime (Minutes)": settings.get("tokenLifetimeInMinutes"),
            })
        elif "phone" in key or auth_type == "phone":
            row.update({
                "User can verify with": _phone_methods(settings),
            })
        elif key == "security_question" or auth_type == "security_question":
            row.update({
                "Usage": _allowed_for_label(settings.get("allowedFor")),
            })
        elif key == "okta_verify":
            channel_binding = settings.get("channelBinding", {}) or {}
            row.update({
                "Compliance FIPS": settings.get("compliance", {}).get("fips"),
                "Channel Binding Style": channel_binding.get("style"),
                "Channel Binding Required": channel_binding.get("required"),
                "User Verification": settings.get("userVerification"),
                "Enrollment Security Level": settings.get("enrollmentSecurityLevel"),
                "User Verification Methods": settings.get("userVerificationMethods"),
            })

        rows.append(row)
    return rows
