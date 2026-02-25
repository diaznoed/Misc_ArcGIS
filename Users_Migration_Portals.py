from arcgis.gis import GIS
from arcgis.gis import User
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def super_share(item, groups, everyone=False, org=False):
    """Share an item with specified groups, and optionally with everyone and within the organization."""
    try:
        item.share(groups=groups, everyone=everyone, org=org)
        logger.info(f"Item {item.id} shared with groups {groups}, everyone={everyone}, org={org}.")
    except Exception as e:
        logger.error(f"Failed to share item {item.id}: {e}")

def recreate_user(session_gis, old_username, new_username, idp_username=None):
    """Create a new user with the same profile as an existing user."""
    old_user = session_gis.users.get(old_username)
    user_type = old_user.userType
    role = old_user.role
    try:
        user_params = {'username': new_username, 'password': 'ExamplePassword123!', 'firstname': old_user.firstName,
                       'lastname': old_user.lastName, 'email': old_user.email, 'role': role, 'user_type': user_type,
                       'provider': 'enterprise' if idp_username else 'arcgis'}
        new_user = session_gis.users.create(**user_params)
        logger.info(f"New user created: {new_username}")
        return new_user
    except Exception as e:
        logger.error(f"Error creating user {new_username}: {e}")
        return None

def reassign_groups(old_user, new_user, verbose=True):
    """Transfer group memberships from old user to new user."""
    groups = old_user.groups
    for group in groups:
        if group.owner == old_user.username:
            group.reassign_to(new_user.username)
            if verbose:
                logger.info(f"Reassigned ownership of group {group.id} to {new_user.username}")
        else:
            group.add_users([new_user.username])
            if verbose:
                logger.info(f"Added {new_user.username} to group {group.id}")

def reassign_items(old_user, new_user, verbose=True):
    """Transfer all items owned by the old user to the new user."""
    items = old_user.items()
    for item in items:
        item.reassign_to(new_user.username)
        if verbose:
            logger.info(f"Reassigned item {item.id} to {new_user.username}")

def user_migration(session_gis, old_username, new_username, idp_username=None):
    """Orchestrate the user migration process."""
    new_user = recreate_user(session_gis, old_username, new_username, idp_username)
    if new_user:
        old_user = session_gis.users.get(old_username)
        reassign_groups(old_user, new_user)
        reassign_items(old_user, new_user)

def main():
    portal_url = 'https://www.example.com/portal'  # Specify your portal URL
    admin_username = 'admin'  # Specify admin username
    admin_password = 'adminpassword'  # Specify admin password
    old_username = 'old_user'  # Specify old username
    new_username = 'new_user'  # Specify new username
    idp_username = 'new_user_idp'  # Specify IDP username if applicable

    gis = GIS(portal_url, admin_username, admin_password)
    user_migration(gis, old_username, new_username, idp_username)

if __name__ == '__main__':
    main()
