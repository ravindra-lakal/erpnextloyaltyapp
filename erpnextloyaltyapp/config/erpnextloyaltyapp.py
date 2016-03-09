from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
	{
			"label": _("Masters"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description":_("Send mass SMS to your contacts"),
				},
				{
					"type": "doctype",
					"name": "Store",
					"description":_("Logs for maintaining sms delivery status"),
				},
				{
					"type": "doctype",
					"name": "Department",
					"description": _("Newsletters to contacts, leads."),
				},
				# {
				# 	"type": "doctype",
				# 	"name": "Season",
				# 	"description": _("Newsletters to contacts, leads."),
				# },

			]
		},
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Confirmed orders from Customers."),
				},
				
			]
		},
		
		{
			"label": _("Setup"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Rule Engine",
					"description": _("Default settings for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "SMS Settings",
					"description": _("Default settings for selling transactions.")
				},
			]
		},
		]