import logging

from scripts.oktasnapshot_utils import ensure_domain_str, get_paginated

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


def _oidc_endpoints(protocol):
    endpoints = protocol.get("endpoints", {}) or {}
    return {
        "authorization": endpoints.get("authorization", {}).get("url"),
        "token": endpoints.get("token", {}).get("url"),
        "jwks": endpoints.get("jwks", {}).get("url"),
    }


def _provisioning_groups(policy):
    provisioning = policy.get("provisioning", {}) or {}
    groups = provisioning.get("groups", {}) or {}
    if groups.get("action") != "SYNC":
        return None
    return groups.get("filter") or []


def get_identity_providers(domain_url, api_token):
    base = ensure_domain_str(domain_url).rstrip("/")
    logger.info("Fetching identity providers for OktaView.")
    url = f"{base}/api/v1/idps"
    idps = get_paginated(url, _headers(api_token), "Error fetching identity providers") or []
    results = []
    for idp in idps:
        protocol = idp.get("protocol", {}) or {}
        protocol_type = (protocol.get("type") or idp.get("type") or "").upper()
        policy = idp.get("policy", {}) or {}
        row = {
            "Name": idp.get("name"),
            "Type": idp.get("type"),
            "Protocol Type": protocol.get("type"),
            "Status": idp.get("status"),
            "Policy Max Clock Skew": policy.get("maxClockSkew"),
            "Policy Account Link Action": policy.get("accountLink", {}).get("action"),
            "Policy Username Template": policy.get("subject", {}).get("userNameTemplate", {}).get("template"),
            "Policy Provisioning Action": policy.get("provisioning", {}).get("action"),
        }

        if protocol_type == "OIDC":
            row.update({
                "Endpoints": _oidc_endpoints(protocol),
                "Settings": protocol.get("settings", {}) or {},
                "Issuer": protocol.get("issuer", {}).get("url"),
                "Provisioning Groups To Sync": _provisioning_groups(policy),
            })
        else:
            trust = protocol.get("credentials", {}).get("trust", {}) or {}
            row.update({
                "SSO URL": protocol.get("endpoints", {}).get("sso", {}).get("url"),
                "Trust Issuer": trust.get("issuer"),
                "Trust Audience": trust.get("audience"),
                "Signing Key ID": protocol.get("credentials", {}).get("signing", {}).get("kid"),
            })

        results.append(row)
    return results
