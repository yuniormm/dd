# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Evaluation(models.Model):
    _name = 'gdu.evaluation'

    type_person = fields.Selection(string='Tipo Persona', selection=[('trabajador', 'Trabajador'), ('profesor', 'Profesor'), ], compute='_definition_person')
    user_id = fields.Many2one('res.users', 'Me', required=False, default=lambda self: self.env.user, readonly=True)

    # Definir Tipo de Persona
    @api.depends('person_id')
    def _definition_person(self):
        for record in self:
            if record.person_id:
                if record.person_id.tipo_persona == 'Trabajador' and record.person_id.es_profesor:
                    record.type_person = 'profesor'
                elif record.person_id.tipo_persona == 'Trabajador' and not record.person_id.es_profesor:
                    record.type_person = 'trabajador'
                else:
                    raise ValidationError("Usted no puede ser evaluado")

    # Datos de pruebas
    person_id = fields.Many2one(comodel_name='gdu.base.persona', string='Person_id', required=False, compute='cargar_datos')

    area = fields.Many2one(related='user_id.usuario_base_id.persona_id.area_id', string='Área')
    departamento = fields.Char(related='user_id.usuario_base_id.persona_id.direccion_real', string='Departamento')

    @api.depends('user_id')
    def cargar_datos(self):
        person = self.sudo().env['gdu.base.persona'].search([('name', '=', self.persona_autenticada().name)])
        self.person_id = person

    def persona_autenticada(self):
        uid = self.env.user
        id_persona = uid.usuario_base_id.persona_id.id
        persona = self.sudo().env['gdu.base.persona'].search([('id', '=', id_persona)])
        return persona
    ################################

    desde = fields.Date(string='Desde', required=False)
    hasta = fields.Date(string='Hasta', required=False)

    ###############################
    #### Campos de Docente ####
    name = fields.Char(string='Nombre y Apellidos', required=False)
    # teaching_category = fields.Char(string='Categoría Docente', required=False)
    teaching_category = fields.Char(string='Categoría Docente', required=False, related='person_id.categoria_docente')

    # scientific_category = fields.Char(string='Categoría Científica', required=False)
    scientific_category = fields.Char(string='Categoría Científica', required=False, related='person_id.categoria_cientifica')


    faculty = fields.Char(string='Facultad', required=False)
    departament = fields.Char(string='Departamento', required=False)
    ##############################################################

    ###########################
    #### Campos no Docente ####
    # Nombre y apellidos
    # Cargo
    # area = fields.Char(string='Área', required=False)
    period = fields.Char(string='Período Evaluativo', required=False)
    ####################################################

    state = fields.Selection(string='Estado', selection=[
        ('borrador', 'Borrador'),
        ('espera', 'En espera de Revisión'),
        ('revisado', 'Revisado'),
        ('evaluado', 'Evaluado'), ], required=False,default='borrador')

    # category_evaluation_id = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    # Indicadores Evaluacion Docente
    training_pre = fields.Html(string='Formación de Pregrado', required=False)
    training_pre_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    training_post = fields.Html(string='Formación de Postgrado', required=False)
    training_post_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    cti = fields.Html(string='Ciencia Tecnologia e Innovacion', required=False)
    cti_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)


    extension_university = fields.Html(string='Extensión Universitaria', required=False)
    extension_university_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    computerization = fields.Html(string='Informatización. Comunicacion. Informatizacion', required=False)
    computerization_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)


    international = fields.Html(string='Internacionalización', required=False)
    international_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)


    assurance = fields.Html(string='Aseguramiento Material y Financiero', required=False)
    assurance_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)


    resources_human = fields.Html(string='Recursos Humanos', required=False)
    resources_human_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    institutional_management = fields.Html(string='Gestión Institucional', required=False)
    institutional_management_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    # Indicadores Evaluacion Docente
    a = fields.Html(string='A', required=False)
    a_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    b = fields.Html(string='B', required=False)
    b_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    c = fields.Html(string='C', required=False)
    c_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    d = fields.Html(string='D', required=False)
    d_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    e = fields.Html(string='E', required=False)
    e_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    f = fields.Html(string='F', required=False)
    f_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)

    g = fields.Html(string='G', required=False)
    g_eva = fields.Many2one(comodel_name='gdu.category.evaluation', string='Evaluación', required=False)


    @api.model
    def create(self, values):
        # raise ValidationError('mildreyyy')

        sol = super(Evaluation, self).create(values)

        sol.state = 'espera'

        return sol

    evaluation_general = fields.Selection(string='Evaluación', selection=[
        ('excelente', 'EXCELENTE'),
        ('bien', 'BIEN'),
        ('regular', 'REGULAR'),
        ('mal', 'MAL'),
        ('superior', 'SUPERIOR'),
        ('adecuado', 'ADECUADO'),
        ('deficiente', 'DEFICIENTE'), ], required=False, )

    # category_evaluation_id = fields.Many2one(
    #     comodel_name='gdu.category.evaluation',
    #     string='category_evaluation_id',
    #     required=False)

    def calc_evaluation(self):
        sum 





