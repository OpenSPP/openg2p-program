# Part of OpenG2P. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenG2P Program Payments: In Files",
    "category": "G2P",
    "version": "17.0.1.2.1",
    "sequence": 1,
    "author": "OpenG2P (OpenSPP fork)",
    "website": "https://openg2p.org",
    "license": "LGPL-3",
    "depends": [
        "g2p_programs",
        "g2p_program_documents",
        "g2p_encryption",
        "mail",
    ],
    "external_dependencies": {
        "python": [
            "base45",
            "cose",
            "python-barcode",
            "pdfkit",
            "qrcode",
            "wkhtmltopdf",
        ]
    },
    "data": [
        "security/ir.model.access.csv",
        "views/payment_file_config_view.xml",
        "views/payment_batch_tag_view.xml",
        "views/payment_manager_view.xml",
        "views/payment_view.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
