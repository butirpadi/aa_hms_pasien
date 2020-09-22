{
    'name': "Custom Form Pasien",
    'summary': """
        Modul custom menu pasien """,
    'description': """
        Modul custom menu pasien
    """,
    'author': "Muhammad Aziz - 087881071515",
    'website': "https://www.tutorialopenerp.wordpress.com/",
    'category': 'Patient',
    'version': '0.1',
    'depends': ['base', 'acs_hms', 'aa_hms_pengobatan'],
    'data': [
        'report/pasien_penyakit.xml',
        'report/pasien_tandavital.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/view_patient_form.xml',
    ],
    'demo': [
    ],
	'application': True,
	'installable': True,
	'auto_install': False,
}
