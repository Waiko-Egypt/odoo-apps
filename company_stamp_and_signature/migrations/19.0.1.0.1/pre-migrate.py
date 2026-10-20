# Migration script: 19.0.1.0.1
# Adds signature_expiry_date and signature_is_expired fields to res.company.
# These are new fields — no data migration needed.
# Odoo ORM will create the columns automatically on module update.


def migrate(cr, version):
    pass
