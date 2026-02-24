import logging

from scripts.extract_admin_roles import get_admin_users, get_admin_groups, get_admin_apps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("okta_compare")


def _role_label(role):
    if isinstance(role, str):
        return role
    if not isinstance(role, dict):
        return None
    for key in ("label", "name", "type", "roleType"):
        value = role.get(key)
        if value:
            return value
    nested = role.get("role")
    if isinstance(nested, dict):
        nested_label = _role_label(nested)
        if nested_label:
            return nested_label
    if role.get("id"):
        return role.get("id")
    return None


def _extract_admin_roles(item):
    if not isinstance(item, dict):
        return ""
    roles = []
    for key in ("roles", "adminRoles", "assignedRoles", "roleAssignments", "roleAssignment", "role"):
        value = item.get(key)
        if not value:
            continue
        if isinstance(value, list):
            roles.extend(value)
        else:
            roles.append(value)
    labels = []
    for role in roles:
        label = _role_label(role)
        if label:
            labels.append(label)
    if not labels:
        return ""
    return ", ".join(sorted({str(label) for label in labels}))


def get_admin_assignments_view(domain_url, api_token):
    logger.info("Fetching admin assignments for OktaView.")
    users = get_admin_users(domain_url, api_token) or []
    groups = get_admin_groups(domain_url, api_token) or []
    apps = get_admin_apps(domain_url, api_token) or []

    user_rows = []
    for user in users:
        user_rows.append({
            "User ID": user.get("userId"),
            "Display Name": user.get("displayName"),
            "Email": user.get("email"),
            "Login": user.get("login"),
            "Admin Roles": _extract_admin_roles(user),
        })

    group_rows = []
    for group in groups:
        group_rows.append({
            "Group ID": group.get("groupId"),
            "Group Name": group.get("name"),
            "Admin Roles": _extract_admin_roles(group),
        })

    app_rows = []
    for app in apps:
        app_rows.append({
            "Client ID": app.get("clientId"),
            "Display Name": app.get("displayName"),
            "App Name": app.get("appName"),
            "App Instance ID": app.get("appInstanceId"),
        })

    return user_rows, group_rows, app_rows
