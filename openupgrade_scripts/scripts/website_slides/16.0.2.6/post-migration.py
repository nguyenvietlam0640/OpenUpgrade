from openupgradelib import openupgrade


def recompute_slide_type(env):
    env["slide.slide"].with_context(active_test=False).search([])._compute_slide_type()


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "website_slides", "16.0.2.6/noupdate_changes.xml")
    recompute_slide_type(env)
