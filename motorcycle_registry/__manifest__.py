{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': """
                Motorcycle Registry
                ====================
                This Module is used to keep track of the 
                Motorcycle Registration and Ownership of each 
                motorcycled of the brand.
            """,
    'author': 'kejw-odoo',
    'website': 'https://github.com/kejw-odoo',
    'category': 'Kawiil',
    "data": [
        "security/motorcycle_registry_groups.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
        "demo/motorcycle_registry_demo.xml",
    ],
    'application': True
}