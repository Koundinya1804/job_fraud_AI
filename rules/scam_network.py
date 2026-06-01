from database.db_manager import update_pattern, get_network_alerts


def update_pattern_database(patterns):

    for p in patterns:
        update_pattern(p)


def detect_scam_network():

    alerts = get_network_alerts()

    return alerts