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
					"name": "Catagory",
					"description": _("Catagory database."),
				},
				{
					"type": "doctype",
					"name": "Department",
					"description":_("Stores Database"),
				},
				{
					"type": "doctype",
					"name": "Color",
					"description":_("Color Database"),
				},
				{
					"type": "doctype",
					"name": "Sub Family",
					"description":_("Stores Database"),
				},
				{
					"type": "doctype",
					"name": "Family",
					"description":_("Stores Database"),
				},
				{
					"type": "doctype",
					"name": "Style",
					"description":_("Stores Database"),
				},
				{
					"type": "doctype",
					"name": "Season",
					"description":_("Stores Database"),
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


		