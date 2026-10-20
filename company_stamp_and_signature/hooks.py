import logging

_logger = logging.getLogger(__name__)

_DELIVERY_ARCH = """
<xpath expr="//div[hasclass('page')]" position="inside">
    <t t-call="company_stamp_and_signature.stamp_delivery_block"/>
</xpath>
"""


def _ensure_delivery_stamp_view(env):
    parent = env.ref("stock.report_deliveryslip_document", raise_if_not_found=False)
    if not parent:
        _logger.warning(
            "company_stamp_and_signature: stock.report_deliveryslip_document "
            "not found — delivery stamp skipped."
        )
        return
    key = "company_stamp_and_signature.report_deliveryslip_document_stamp"
    existing = env["ir.ui.view"].search([("key", "=", key)], limit=1)
    if not existing:
        env["ir.ui.view"].create(
            {
                "name": "report_deliveryslip_document_stamp",
                "type": "qweb",
                "inherit_id": parent.id,
                "arch": _DELIVERY_ARCH,
                "key": key,
            }
        )
        _logger.info("company_stamp_and_signature: delivery stamp view created.")


def post_init_hook(env):
    _ensure_delivery_stamp_view(env)
