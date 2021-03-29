# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_helper"
app_title = "Erpnext Helper"
app_publisher = "Frappe Technologies Pvt Ltd"
app_description = "Setting up Self Hosted sites via Mdifferent Marketplaces"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_helper/css/erpnext_helper.css"
app_include_js = "/assets/js/erpnext_helper.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_helper/css/erpnext_helper.css"
# web_include_js = "/assets/erpnext_helper/js/erpnext_helper.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_helper.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Setup Wizard
# -------------
setup_wizard_requires = "assets/erpnext_helper/js/setup_wizard.js"
# setup_wizard_stages = "erpnext.setup.setup_wizard.setup_wizard.get_setup_stages"
# setup_wizard_test = "erpnext.setup.setup_wizard.test_setup_wizard.run_setup_wizard_test"

# Installation
# ------------
# before_install = "erpnext_helper.install.before_install"
# after_install = "erpnext_helper.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_helper.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_helper.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_helper.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_helper.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_helper.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_helper.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_helper.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_helper.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_helper.task.get_dashboard_data"
# }

