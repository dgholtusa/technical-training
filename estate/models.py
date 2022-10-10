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
        date_availability = fields.Date()
        expected_price = fields.Float()
        selling_price = fields.Float()
        bedrooms = fields.Integer()
        living_area = fields.Integer()
        facades = fields.Integer()
        garage = fields.Boolean()
        garden = fields.Boolean()
        garden_area = fields.Integer()
        garden_orientation = fields.Selection(
           string='Type',
           selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
           help='Make your selection'
        )

<record id="estate_model_action" model="ir.actions.act_window">
    <field name="name">Test action</field>
        <field name="res_model">test.model</field>
            <field name="view_mode">tree,form</field>
            </record>
