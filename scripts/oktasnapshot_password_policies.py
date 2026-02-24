import logging

from scripts.oktasnapshot_utils import ensure_domain_str, get_paginated, get_json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("okta_compare")


def _headers(api_token):
    return {
        "Authorization": f"SSWS {api_token}",
        "Accept": "application/json",
    }


def _get_rules(base, api_token, policy_id):
    url = f"{base}/api/v1/policies/{policy_id}/rules"
    return get_paginated(url, _headers(api_token), "Error fetching password policy rules") or []


def _settings_to_string(settings, label_map=None):
    if not isinstance(settings, dict):
        return ""
    parts = []
    label_map = label_map or {}
    ordered_keys = list(label_map.keys())
    for key in ordered_keys:
        if key not in settings:
            continue
        value = settings.get(key)
        label, formatter = label_map.get(key, (key, None))
        formatted = formatter(value) if formatter else value
        parts.append(f"{label}: {formatted}")
    for key, value in settings.items():
        if key in ordered_keys:
            continue
        label, formatter = label_map.get(key, (key, None))
        formatted = formatter(value) if formatter else value
        parts.append(f"{label}: {formatted}")
    return "; ".join(parts)


def _bool_label(value):
    if value is None:
        return "Not Available"
    return "Yes" if bool(value) else "No"


def _list_label(value):
    if not value:
        return "None"
    return ", ".join([str(v) for v in value])


def _minutes_label(value):
    if value is None:
        return "Not Available"
    try:
        minutes = int(value)
    except (TypeError, ValueError):
        return str(value)
    if minutes % 60 == 0:
        hours = minutes // 60
        return f"{hours} hours" if hours != 1 else "1 hour"
    return f"{minutes} minutes"


def _lockout_channels_label(value):
    if not value:
        return "No"
    return "Yes"


def _exclude_attributes_label(value):
    if not value:
        return "None"
    mapping = {
        "firstName": "first name",
        "lastName": "last name",
        "login": "username",
        "email": "email",
    }
    labels = [mapping.get(v, v) for v in value]
    return ", ".join(labels)


def _complexity_label_map():
    return {
        "minLength": ("Minimum length", None),
        "minLowerCase": ("Lower case letters", None),
        "minUpperCase": ("Upper case letters", None),
        "minNumber": ("Numbers", None),
        "minSymbol": ("Symbols", None),
        "excludeUsername": ("Does not contain part of username", _bool_label),
        "excludeAttributes": ("Does not contain attributes", _exclude_attributes_label),
        "dictionary": ("Restrict use of common passwords", _dictionary_label),
        "minRepeatingCharacters": ("Maximum consecutive repeating characters", None),
    }


def _dictionary_label(dictionary_settings):
    if not isinstance(dictionary_settings, dict):
        return "Not Available"
    common = (dictionary_settings.get("common") or {}).get("exclude")
    if common is None:
        return "Not Available"
    return "Enabled" if bool(common) else "Disabled"


def _age_label_map():
    return {
        "maxAgeDays": ("Password expires after (days)", None),
        "expireWarnDays": ("Prompt user before expiry (days)", None),
        "minAgeMinutes": ("Minimum password age", _minutes_label),
        "historyCount": ("Enforce password history (count)", None),
    }


def _lockout_label_map():
    return {
        "maxAttempts": ("Lock out after failed attempts", None),
        "autoUnlockMinutes": ("Auto unlock after", _minutes_label),
        "userLockoutNotificationChannels": ("Send lockout email", _lockout_channels_label),
        "showLockoutFailures": ("Show lockout failures", _bool_label),
    }


def _breached_label_map():
    return {
        "expireAfterDays": ("Expire the password after this many days", None),
        "logoutEnabled": ("Log out user from Okta immediately", _bool_label),
        "delegatedWorkflowId": ("Take custom actions using Workflows", None),
    }


def get_password_policies(domain_url, api_token):
    base = ensure_domain_str(domain_url).rstrip("/")
    logger.info("Fetching password policies for OktaView.")
    url = f"{base}/api/v1/policies?type=PASSWORD"
    policies = get_paginated(url, _headers(api_token), "Error fetching password policies") or []

    policy_rows = []
    rule_rows = []

    for policy in policies:
        policy_id = policy.get("id")
        rules = _get_rules(base, api_token, policy_id)
        password_settings = (policy.get("settings", {}) or {}).get("password", {}) or {}
        policy_rows.append({
            "ID": policy_id,
            "Status": policy.get("status"),
            "Name": policy.get("name"),
            "Description": policy.get("description"),
            "Priority": policy.get("priority"),
            "Provider": (policy.get("provider", {}) or {}).get("type"),
            "Complexity Settings": _settings_to_string(
                password_settings.get("complexity", {}),
                _complexity_label_map(),
            ),
            "Age Settings": _settings_to_string(password_settings.get("age", {}), _age_label_map()),
            "Lockout Settings": _settings_to_string(password_settings.get("lockout", {}), _lockout_label_map()),
            "Breached Protection Settings": _settings_to_string(
                password_settings.get("breachedProtection", {}),
                _breached_label_map(),
            ),
            "Rules": ", ".join([r.get("name") for r in rules if r.get("name")]),
        })

        for rule in rules:
            rule_rows.append({
                "Policy ID": policy_id,
                "Policy Name": policy.get("name"),
                "Rule ID": rule.get("id"),
                "Rule Name": rule.get("name"),
                "Status": rule.get("status"),
                "Priority": rule.get("priority"),
                "Conditions People": (rule.get("conditions", {}) or {}).get("people", {}),
                "Conditions Network": (rule.get("conditions", {}) or {}).get("network", {}),
                "Actions": rule.get("actions", {}),
            })

    return policy_rows, rule_rows
