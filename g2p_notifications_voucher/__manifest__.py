{
    "name": "G2P Notifications: Voucher",
    "category": "G2P",
    "version": "17.0.1.2.1",
    "sequence": 1,
    "author": "OpenG2P (OpenSPP fork)",
    "website": "https://openg2p.org",
    "license": "LGPL-3",
    "depends": [
        "g2p_entitlement_voucher",
        "g2p_notifications_base",
    ],
    "data": [
        "views/email_notification_manager.xml",
        "views/sms_notification_manager.xml",
    ],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
    },
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}
