from odoo import fields, models, api


class CategoryEvaluation(models.Model):
    _name = 'gdu.category.evaluation'

    name = fields.Char(string='Abreviatura')
    nombre = fields.Char(string='Nombre de la Categoría')
    descripcion = fields.Char(string='Descripción')
    valor = fields.Integer(string='Valor', required=False)

    # evaluation_ids = fields.Many2many(comodel_name='gdu.evaluation', string='Evaluation_ids')
    # evaluation_ids = fields.One2many(
    #     comodel_name='gdu.evaluation',
    #     inverse_name='category_evaluation_id',
    #     string='Evaluation_ids',
    #     required=False)
