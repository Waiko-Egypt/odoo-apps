def migrate(cr, version):
    """Repair empty dimensions and enable images for uninitialized companies."""
    cr.execute(
        """
        UPDATE res_company
           SET show_product_image_in_reports = CASE
                   WHEN product_image_width IS NULL OR product_image_width <= 0
                     OR product_image_height IS NULL OR product_image_height <= 0 THEN TRUE
                   ELSE COALESCE(show_product_image_in_reports, TRUE)
               END,
               product_image_width = CASE
                   WHEN product_image_width IS NULL OR product_image_width <= 0 THEN 40
                   ELSE product_image_width
               END,
               product_image_height = CASE
                   WHEN product_image_height IS NULL OR product_image_height <= 0 THEN 40
                   ELSE product_image_height
               END
        """
    )
