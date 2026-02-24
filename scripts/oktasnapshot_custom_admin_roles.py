import logging

from scripts.extract_admin_roles import get_custom_admin_roles

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("okta_compare")


def get_custom_admin_roles_view(domain_url, api_token):
    logger.info("Fetching custom admin roles for OktaView.")
    roles = get_custom_admin_roles(domain_url, api_token) or []
    rows = []
    for role in roles:
        rows.append({
            "Label": role.get("label"),
            "Description": role.get("description"),
            "Is Cloneable": role.get("isCloneable"),
        })
    return rows
