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
					"description":_("Item Database"),
				},
				{
					"type": "doctype",
					"name": "Store",
					"description":_("Stores Database"),
				},
				{
					"type": "doctype",
					"name": "Department",
					"description": _("Departments Database."),
				},
				{
					"type": "doctype",
					"name": "Season",
					"description": _("Seasons Database."),
				},

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
					"description": _("Rules for Points redumption.")
				},
				{
					"type": "doctype",
					"name": "SMS Settings",
					"description": _("Settings for the SMS Gateway.")
				},
			]
		},
		]