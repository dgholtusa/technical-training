from odoo import models,fields

class EstateProperty(models.Model):
        _name = "estate.property"
        _description = "Our Estate Module"

        id = fields.Integer()
        create_uid = fields.Integer()
        create_date = fields.Date()
        write_uid = fields.Integer()
        write_date = fields.Date()
        name = fields.Char()
        description = fields.Char()
        postcode = fields.Char()
        date_availability = fields.Date(copy=False,default=fields.Date.add(fields.Date.today(), months=3))
        expected_price = fields.Float()
        selling_price = fields.Float(copy=False,readonly=True)
        bedrooms = fields.Integer(default=2)
        living_area = fields.Integer()
        facades = fields.Integer()
        garage = fields.Boolean()
        garden = fields.Boolean()
        garden_area = fields.Integer()
        garden_orientation = fields.Selection(
           string='Orientation',
           selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
           help='Make your selection')
        active = fields.Boolean(default=False)
        state = fields.Selection(
                string='State',
                selection=[('new', 'New'),('offer', 'Offer'), ('received', 'Received'), ('offer', 'Offer'), ('accepted', 'Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
                copy=False,
                required=True,
                default='new')
        property_type_id = fields.Char()
