from django.db import models

from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify

from partner.util import load_choices
from partner.fields import (
    RangeIntegerField,
    PercentageField,
)


# model.FileField(uploadto=proof_of_agency_status_uh)
def proof_of_agency_status_uh(instance, filename):
    return '{}/proof_of_agency_status/{}'.format(slugify(instance.name), filename)


# model.FileField(scan_990)
def scan_990_uh(instance, filename):
    return '{}/scan_990_uh/{}'.format(slugify(instance.name), filename)

"""
h2 Agency Information
         :name
         :distributor_type, collection: %w[Agency Hospital], as: :radio_buttons
         :agency_type, collection: ['501(c)3', 'Religious Organization', 'Government Organization']
         :proof_of_agency_status, as: :file
        ul
          li 501(c)3 Letter
          li Letter of Good Standing from Denominational Headquarters
          li Government Letterhead
         :agency_mission, as: :text
         :address1
         :address2
         :city
         :state, collection: states
         :zip_code

        h2 Media Information
         :website
         :facebook
         :twitter

        h2 Agency Stability
         :founded, as: :integer, input_html: { min: 1800, max: Date.current.year }
         :form_990, as: :radio_buttons
         :scan_990, as: :file
         :program_name
         :program_description
         :program_age
         :case_management, as: :radio_buttons
         :evidence_based, as: :radio_buttons
         :evidence_based_description, as: :text
         :program_client_improvement, as: :text
         :diaper_use, collection: diaper_use, as: :check_boxes
         :other_diaper_use
         :currently_provide_diapers, as: :radio_buttons
         :turn_away_child_care, as: :radio_buttons

        h3 Program Address
         :program_address1
         :program_address2
         :program_city
         :program_state, collection: states
         :program_zip_code

        h2 Organizational Capacity
         :max_serve
         :incorporate_plan, as: :text
         :responsible_staff_position, as: :radio_buttons
         :storage_space, as: :radio_buttons
         :describe_storage_space, as: :text
         :trusted_pickup, as: :radio_buttons

        h2 Population Served
         :income_requirement_desc, as: :radio_buttons
         :serve_income_circumstances, as: :radio_buttons
         :income_verification, as: :radio_buttons
         :internal_db, as: :radio_buttons
         :maac, as: :radio_buttons

        h3 Ethnic composition of those served
         :population_black, input_html: { min: 0, max: 100 }
         :population_white, input_html: { min: 0, max: 100 }
         :population_hispanic, input_html: { min: 0, max: 100 }
         :population_asian, input_html: { min: 0, max: 100 }
         :population_american_indian, input_html: { min: 0, max: 100 }
         :population_island, input_html: { min: 0, max: 100 }
         :population_multi_racial, input_html: { min: 0, max: 100 }
         :population_other, input_html: { min: 0, max: 100 }

        h3 Zips served
         :zips_served

        h3 Poverty information of those served
         :at_fpl_or_below, input_html: { min: 0, max: 100 }
         :above_1_2_times_fpl, input_html: { min: 0, max: 100 }
         :greater_2_times_fpl, input_html: { min: 0, max: 100 }
         :poverty_unknown, input_html: { min: 0, max: 100 }

        h3 Ages served
         :ages_served

        h2 Executive Director
         :executive_director_name
         :executive_director_phone
         :executive_director_email

        h2 Program Contact Person
         :program_contact_name
         :program_contact_phone
         :program_contact_mobile
         :program_contact_email

        h2 Diaper Pick Up Person
         :pick_up_method, collection: %w[volunteers staff courier]
         :pick_up_name
         :pick_up_phone
         :pick_up_email

        h2 Agency Distribution Information
         :distribution_times
         :new_client_times
         :more_docs_required

        h2 Sources of Funding
         :sources_of_funding, collection: funding_sources, as: :check_boxes
         :sources_of_diapers, collection: diaper_sources, as: :check_boxes
         :diaper_budget, collection: %w[N/A Yes No], as: :radio_buttons
         :diaper_funding_source, collection: %w[N/A Yes No], as: :radio_buttons



Collections:
    DIAPER_USE = [
   'Emergency supplies for families (off site)',
   'Homeless shelter',
   'Domestic violence shelter',
   'On-site residential program',
   'Outreach',
   'Alcohol/Drug Recovery',
   'Daycare',
   'Foster Care',
   'Other'
  ]

  FUNDING_SOURCES = [
    'Grants - Foundation',
    'Grants - State',
    'Grants - Federal',
    'Corporate Donations',
    'Individual Donations',
    'Other'
  ]

  DIAPER_SOURCES = [
    'Purchase Retail',
    'Purchase Wholesale',
    'Diaper Drives',
    'Diaper Drives conducted by others',
    'Other'
  ]
"""

# RangeIntegerField = models.IntegerField

# Common lengths
CHOICE_LENGTH = 2
ZIP_LENGTH = 100
NAME_LENGTH = 1024
MEDIUM_LENGTH = 1024
DESCRIPTION_LENGTH = 4096

class Partner(models.Model):

    DISTRIBUTOR_AGENCY = 'Agency'
    DISTRIBUTOR_HOSPITAL = 'Hospital'
    DISTRIBUTOR_TYPES = (
        ('AG', DISTRIBUTOR_AGENCY),
        ('HO', DISTRIBUTOR_HOSPITAL),
    )

    AT_C3 = '501(c)3'
    AT_RELIGIOUS_ORGANIZATION = 'Religious Organization'
    AT_GOVERNMENT_ORGANIZATION = 'Government Organization'
    AGENCY_TYPES = (
        ('50', AT_C3),
        ('RE', AT_RELIGIOUS_ORGANIZATION),
        ('GO', AT_GOVERNMENT_ORGANIZATION),
    )

    POAS_C3_LETTER = '501(c)3 LETTER'
    POAS_GOOD_STANDING = 'Letter of Good Standing from Denominational Headquarters'
    POAS_GOVERNMENT_LETTERHEAD = 'Government Letterhead'
    PROOF_OF_AGENCY_STATUS_TYPE = (
        ('50', C3_LETTER),
        ('LE', GOOD_STANDING),
        ('GO', ),
    )

    DU_EMERGENCY_SUPPLIES = 'Emergency supplies for families (off site)'
    DU_HOMELES_SHELTER = 'Homeless shelter'
    DU_DOMESTIC_VIOLENCE_SHELTER = 'Domestic violence shelter'
    DU_ONSITE = 'On-site residential program'
    DU_OUTREACH = 'Outreach'
    DU_ALCOHOL = 'Alcohol/Drug Recovery'
    DU_DAYCARE = 'Daycare'
    DU_FOSTER_CARE = 'Foster Care'
    DU_OTHER = 'Other'
    DIAPER_USE = (
       ('EM', DU_EMERGENCY_SUPPLIES),
       ('HO', DU_HOMELES_SHELTER),
       ('DO', DU_DOMESTIC_VIOLENCE_SHELTER),
       ('ON', DU_ONSITE),
       ('OU', DU_OUTREACH),
       ('AL', DU_ALCOHOL),
       ('DA', DU_DAYCARE),
       ('FO', DU_FOSTER_CARE),
       ('OT', DU_OTHER),
    )

    PICKUP_VOLUNTEERS = 'VO'
    PICKUP_STAFF = 'ST'
    PICKUP_COURIER = 'CO'
    PICK_UP_METHODS = (
        (PICKUP_VOLUNTEERS, 'Volunteers'),
        (PICKUP_STAFF, 'Staff'),
        (PICKUP_COURIER, 'Courier'),
    )

    FS_FOUNDATION_GRANTS = 'FO'
    FS_STATE_GRANTS = 'ST'
    FS_FEDERAL_GRANTS = 'FE'
    FS_CORPORATE_DONATIONS = 'CO'
    FS_INDIVIDUAL_DONATIONS = 'IN'
    FS_OTHER = 'OT'
    FUNDING_SOURCES = (
        (FS_FOUNDATION_GRANTS, 'Grants - Foundation'),
        (FS_STATE_GRANTS, 'Grants - State'),
        (FS_FEDERAL_GRANTS, 'Grants - Federal'),
        (FS_CORPORATE_DONATIONS, 'Corporate Donations'),
        (FS_INDIVIDUAL_DONATIONS, 'Individual Donations'),
        (FS_OTHER, 'Other'),
    )

    DS_PURCHASE_RETAIL = 'PR'
    DS_PURCHASE_WHOLESALE = 'PH'
    DS_DIAPER_DRIVES = 'DD'
    DS_DIAPER_DRIVES_BY_OTHERS = 'DO'
    DS_OTHER = 'O'
    DIAPER_SOURCES = (
        (DS_PURCHASE_RETAIL, 'Purchase Retail'),
        (DS_PURCHASE_WHOLESALE, 'Purchase Wholesale'),
        (DS_DIAPER_DRIVES, 'Diaper Drives'),
        (DS_DIAPER_DRIVES_BY_OTHERS, 'Diaper Drives conducted by others'),
        (DS_OTHER, 'Other'),
    )

    # Angency Information
    name = models.CharField(max_length=2048, null=False, blank=False)
    distributor_type = models.CharField(max_length=2,
                                        choices=DISTRIBUTOR_TYPES)
    agency_types = models.ChoiceField(max_length=2,
                                      choices=AGENCY_TYPES)
    proof_of_agency_status = model.FileField() #  TODO: add file arguments
    proof_of_agency_status_type = models.CharField(max_length=CHOICE_LENGTH,
                                                   choices=PROOF_OF_AGENCY_STATUS_TYPE)
    agency_mission = models.CharField(max_length=DESCRIPTION_LENGTH)
    address_1 = models.CharField(max_length=MEDIUM_LENGTH)
    address_2 = models.CharField(max_length=MEDIUM_LENGTH)
    city = models.CharField(max_length=NAME_LENGTH)
    state = models.CharField(max_length=2, choices=load_choices('./states.txt'))
    zip_code = models.CharField(max_length=ZIP_LENGTH)

    # Media Information
    website = models.URLField()
    facebook = models.CharField(max_length=NAME_LENGTH,
                                help_text="Facebook page name (DO NOT include the URL)")
    twitter = models.CharField(max_length=NAME_LENGTH,
                               help_text="Twitter Handle")

    # Agency Stability

    founded = RangeIntegerField(min=1800, max=get_current_year())
    form_990 = models.FileField()
    program_name = models.CharField(max_length=NAME_LENGTH)
    program_description = models.CharField(max_length=DESCRIPTION_LENGTH)
    # TODO: age (possibly omit)
    case_management = models.BooleanField()
    evidence_based = models.BooleanField()
    evidence_based_description = models.CharField(max_length=DESCRIPTION_LENGTH)
    program_client_improvement = models.CharField(max_length=DESCRIPTION_LENGTH)
    diaper_use = models.CharField(max_length=CHOICE_LENGTH, choices=DIAPER_USE)
    other_diaper_use = models.CharField(max_length=DESCRIPTION_LENGTH)
    currently_provide_diapers = models.BooleanField()
    turn_away_child_care = models.BooleanField()

    # Program Address
    program_address1 = models.CharField(max_length=MEDIUM_LENGTH)
    program_address2 = models.CharField(max_length=MEDIUM_LENGTH)
    program_city = models.CharField(max_length=NAME_LENGTH)
    program_state = models.CharField(max_length=CHOICE_LENGTH,
                                     choices=load_choices('./states.txt'))
    program_zip_code = models.CharField(max_length=ZIP_LENGTH)

    # Organizational Capacity

    max_serve = models.IntegerField(help_text='Maximum number of people this organization can serve')
    incorporate_plan = models.CharField(max_length=DESCRIPTION_LENGTH)
    responsible_staff_position = models.BooleanField()
    storage_space = models.BooleanField()
    description_of_storage_space = models.CharField(max_length=DESCRIPTION_LENGTH)
    trusted_pickup = models.BooleanField()

    # Population served
    incmome_requirement_description = models.BooleanField()
    serve_income_circumstances = models.BooleanField()
    income_verification = models.BooleanField()
    internal_diaper_bank = models.BooleanField() # TODO: Is db=diaper bank?
    maac = models.BooleanField()

    # Ethnic composition of those served
    population_black = PercentageField()
    population_white = PercentageField()
    population_hispanic = PercentageField()
    population_asian = PercentageField()
    population_american_indian = PercentageField()
    population_island = PercentageField()
    population_multi_racial = PercentageField()
    population_other = PercentageField()

    # Zips served
    zip_codes_served = models.CharField(max_length=MEDIUM_LENGTH)

    # Poverty Information
    at_fpl_or_below = PercentageField()
    above_1_2_times_fpl = PercentageField()
    greater_2_times_fpl = PercentageField()
    poverty_unknown = PercentageField()

    # Ages served
    ages_served = models.CharField(max_length=MEDIUM_LENGTH)

    #Executive Director
    executive_director_name = models.CharField(max_length=MEDIUM_LENGTH)
    executive_director_phone = PhoneNumberField()
    executive_director_email = models.EmailField()

    # Program Contact Person
    program_contact_name = models.CharField(max_length=MEDIUM_LENGTH)
    program_contact_phone = PhoneNumberField()
    program_contact_mobile = PhoneNumberField()
    program_contact_email = models.EmailField()

    # Diaper Pickup Person
    pick_up_method = models.CharField(max_length=CHOICE_LENGTH,
                                      choices=PICK_UP_METHODS)
    pick_up_contact_name = models.CharField(max_length=MEDIUM_LENGTH)
    pick_up_contact_phone = PhoneNumberField()
    pick_up_contact_email = models.EmailField()

    # Agency Distribution Information
    distribution_times = models.CharField(max_length=MEDIUM_LENGTH)
    new_client_times = models.CharField(max_length=MEDIUM_LENGTH)
    more_docs_required = models.CharField(max_length=MEDIUM_LENGTH)

    # Sources of Funding
    funding_sources = models.ChoiceField(max_length=CHOICE_LENGTH,
                                         choices=FUNDING_SOURCES)
    sources_of_diapers = models.ChoiceField(max_length=CHOICE_LENGTH,
                                            choices=DIAPER_SOURCES)
    diaper_budget = models.BooleanField()
    diaper_funding_source = models.BooleanField()
