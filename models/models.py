from odoo import models, fields, api
from datetime import timedelta, datetime
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class ACSPatient(models.Model):
    _inherit = 'hms.patient'

    # tanda_vital = fields.One2many('pasien.tanda.vital', 'patient_id', string='Tanda Vital', readonly=True)
    appointment_line = fields.One2many('hms.appointment', 'patient_id', ondelete='restrict', string='Appointment', readonly=True)
    patient_diseases = fields.One2many('hms.patient.disease', 'patient_id', string='Diseases', readonly=True)
    nama_ayah = fields.Char('Nama Ayah')
    nama_ibu = fields.Char('Nama Ibu')


# class pasien_tanda_vital(models.Model):
#     _name = 'pasien.tanda.vital'
#
#     patient_id = fields.Many2one('hms.patient', ondelete='cascade', string="Patient")
#     name = fields.Datetime('Tanggal', related='appointment_id.date')
#     suhu_badan = fields.Integer('Suhu Badan (°C)')
#     berat_badan = fields.Float('Berat Badan (Kg)')
#     tinggi_badan = fields.Integer('Tinggi Badan (cm)')
#     lingkar_kepala = fields.Integer('Lingkar Kepala (cm)')
#     tekanan_darah = fields.Char('Tekanan Darah (mmHg)')
#     pernafasan = fields.Integer('Pernafasan (Kali/Menit)')
#     nadi = fields.Integer('Nadi (BPM)')
#     appointment_id = fields.Many2one('hms.appointment', ondelete='cascade', string='Appointment', required=True)



class ACSPatientDisease(models.Model):
    _inherit = 'hms.patient.disease'

    patient_id = fields.Many2one('hms.patient', ondelete='cascade', string='Patient')
    disease = fields.Many2one('hms.diseases', ondelete='set null', string='Diagnosis', related='treatment_id.diagnosis_id')
    diagnosed_date = fields.Datetime(string='Date of Diagnosis', related='treatment_id.date')
    physician_id = fields.Many2one('hms.physician', ondelete='restrict', string='Physician', help='Physician who treated or diagnosed the patient', related='treatment_id.physician_id')
    age = fields.Char(string='Age when diagnosed', help='Patient age at the moment of the diagnosis. Can be estimative', related='treatment_id.age')
    allergy_type = fields.Selection([
            ('da', 'Drug Allergy'),
            ('fa', 'Food Allergy'),
            ('ma', 'Misc Allergy'),
            ('mc', 'Misc Contraindication'),
        ], string='Allergy type', index=True, sort=False, related='treatment_id.allergy_type')
    description = fields.Text(string='Keluhan Utama', related='treatment_id.finding')
    anamnesis = fields.Text(string="Anamnesis", related='treatment_id.anamnesis')
    pemeriksaan_fisik = fields.Text(string="Pemeriksaan Fisik", related='treatment_id.pemeriksaan_fisik')
    tindakan = fields.Text(string="Tindakan", related='treatment_id.tindakan')
    healed_date = fields.Date(string='Healed', related='treatment_id.healed_date')
    is_allergy = fields.Boolean(string='Allergic Disease', related='treatment_id.is_allergy')
    pregnancy_warning = fields.Boolean(string='Pregnancy warning', related='treatment_id.pregnancy_warning')
    lactation = fields.Boolean('Lactation', related='treatment_id.lactation')
    disease_severity = fields.Selection([
            ('mild', 'Mild'),
            ('moderate', 'Moderate'),
            ('severe', 'Severe'),
        ], string='Severity',index=True, sort=False, related='treatment_id.disease_severity')
    status = fields.Selection([
            ('acute', 'Acute'),
            ('chronic', 'Chronic'),
            ('unchanged', 'Unchanged'),
            ('healed', 'Healed'),
            ('improving', 'Improving'),
            ('worsening', 'Worsening'),
        ], string='Status of the disease',index=True, sort=False, related='treatment_id.disease_status')
    is_infectious = fields.Boolean(string='Infectious Disease', help='Check if the patient has an infectious transmissible disease', related='treatment_id.is_infectious')
