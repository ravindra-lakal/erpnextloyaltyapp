# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "erpnextloyaltyapp"
app_title = "Erpnextloyaltyapp"
app_publisher = "New Indictrans Technologies PVT LTD"
app_description = "The app is used to give loyalty points to the users based on various Rules"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ravindra.l@indictranstech.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnextloyaltyapp/css/erpnextloyaltyapp.css"
# app_include_js = "/assets/erpnextloyaltyapp/js/erpnextloyaltyapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnextloyaltyapp/css/erpnextloyaltyapp.css"
# web_include_js = "/assets/erpnextloyaltyapp/js/erpnextloyaltyapp.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnextloyaltyapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnextloyaltyapp.install.before_install"
# after_install = "erpnextloyaltyapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnextloyaltyapp.notifications.get_notification_config"

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

doc_events = {
	"Customer": {
        "autoname":"erpnextloyaltyapp.custom.customer.autoname",
		# "on_update": "method",
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnextloyaltyapp.tasks.all"
# 	],
# 	"daily": [
# 		"erpnextloyaltyapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnextloyaltyapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnextloyaltyapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnextloyaltyapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnextloyaltyapp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnextloyaltyapp.event.get_events"
# }
fixtures=['Custom Script','Property Setter','Custom Field']
