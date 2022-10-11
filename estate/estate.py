from odoo import models,fields

class EstatePropertyType(models.Model):
        _name = "estate.property.type"
        _description = "Estate Property Type Module"

        id = fields.Integer()
        name = fields.Char(required=True)
        description = fields.Char()
