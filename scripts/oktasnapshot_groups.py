import logging

from scripts.extract_groups import get_groups

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("okta_compare")


def get_groups_view(domain_url, api_token):
    logger.info("Fetching groups for OktaView.")
    groups = get_groups(domain_url, api_token) or []
    rows = []
    for group in groups:
        if group.get("type") != "OKTA_GROUP":
            continue
        profile = group.get("profile") or {}
        rows.append({
            "Group Name": profile.get("name"),
            "Description": profile.get("description"),
        })
    return rows
