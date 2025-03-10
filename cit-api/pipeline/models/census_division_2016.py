from django.contrib.gis.db import models
from django.contrib.gis.db.models import MultiPolygonField
from django.contrib.gis.geos import Point

from pipeline.constants import WGS84_SRID


class census_division_2016(models.Model):

    census_year = models.IntegerField(null=True)
    census_division_id = models.IntegerField(primary_key=True, null=False, blank=False)
    census_division_name = models.CharField(max_length=127)
    census_division_type_code = models.CharField(max_length=12, null=True)
    census_division_type_desc = models.CharField(max_length=127, null=True)
    geom = models.MultiPolygonField(srid=WGS84_SRID, null=True)
    geom_simplified = models.MultiPolygonField(srid=WGS84_SRID, null=True)
    global_nonresp_sf_pct = models.FloatField(null=True)
    global_nonresp_lf_pct = models.FloatField(null=True)
    commute_total_by_mode = models.IntegerField(null=True)
    commute_car_driver = models.IntegerField(null=True)
    commute_car_passenger = models.IntegerField(null=True)
    commute_public_transit = models.IntegerField(null=True)
    commute_walk = models.IntegerField(null=True)
    commute_bicycle = models.IntegerField(null=True)
    commute_total_by_duration = models.IntegerField(null=True)
    commute_durtn_0_14 = models.IntegerField(null=True)
    commute_durtn_15_29 = models.IntegerField(null=True)
    commute_durtn_30_44 = models.IntegerField(null=True)
    commute_durtn_45_59 = models.IntegerField(null=True)
    commute_durtn_60plus = models.IntegerField(null=True)
    education_15plus_under_gr12 = models.IntegerField(null=True)
    education_15plus_gr12 = models.IntegerField(null=True)
    education_15plus_postsec = models.IntegerField(null=True)
    education_15plus_apprentice = models.IntegerField(null=True)
    education_15plus_college_cert = models.IntegerField(null=True)
    education_15plus_univ_blw_bach = models.IntegerField(null=True)
    education_15plus_univ_bachelor = models.IntegerField(null=True)
    education_15plus_univ_master = models.IntegerField(null=True)
    education_15plus_univ_doctor = models.IntegerField(null=True)
    education_25_64_under_gr12 = models.IntegerField(null=True)
    education_25_64_gr12 = models.IntegerField(null=True)
    education_25_64_postsec = models.IntegerField(null=True)
    education_25_64_apprentice = models.IntegerField(null=True)
    education_25_64_college_cert = models.IntegerField(null=True)
    education_25_64_univ_blw_bach = models.IntegerField(null=True)
    education_25_64_univ_bachelor = models.IntegerField(null=True)
    education_25_64_univ_master = models.IntegerField(null=True)
    education_25_64_univ_doctor = models.IntegerField(null=True)
    pop_total_2016 = models.IntegerField(null=True)
    pop_total_2011 = models.IntegerField(null=True)
    pop_2011_2016_pct_change = models.FloatField(null=True)
    pop_density_per_sq_km = models.IntegerField(null=True)
    land_area_sq_km = models.IntegerField(null=True)
    aboriginal_identity = models.IntegerField(null=True)
    hshld_income_median = models.FloatField(null=True)
    hshld_income_5kunder = models.IntegerField(null=True)
    hshld_income_5k_10k = models.IntegerField(null=True)
    hshld_income_10k_15k = models.IntegerField(null=True)
    hshld_income_15k_20k = models.IntegerField(null=True)
    hshld_income_20k_25k = models.IntegerField(null=True)
    hshld_income_25k_30k = models.IntegerField(null=True)
    hshld_income_30k_35k = models.IntegerField(null=True)
    hshld_income_35k_40k = models.IntegerField(null=True)
    hshld_income_40k_45k = models.IntegerField(null=True)
    hshld_income_45k_50k = models.IntegerField(null=True)
    hshld_income_50k_60k = models.IntegerField(null=True)
    hshld_income_60k_70k = models.IntegerField(null=True)
    hshld_income_70k_80k = models.IntegerField(null=True)
    hshld_income_80k_90k = models.IntegerField(null=True)
    hshld_income_90k_100k = models.IntegerField(null=True)
    hshld_income_100kplus = models.IntegerField(null=True)
    hshld_income_100k_125k = models.IntegerField(null=True)
    hshld_income_125k_150k = models.IntegerField(null=True)
    hshld_income_150k_200k = models.IntegerField(null=True)
    hshld_income_200kplus = models.IntegerField(null=True)
    total_low_income_status = models.IntegerField(null=True)
    total_low_income_status_0_5 = models.IntegerField(null=True)
    total_low_income_status_0_17 = models.IntegerField(null=True)
    total_low_income_status_18_64 = models.IntegerField(null=True)
    total_low_income_status_65plus = models.IntegerField(null=True)
    employment_income_percent = models.FloatField(null=True)
    industry_accomm_food = models.IntegerField(null=True)
    industry_admin_waste = models.IntegerField(null=True)
    industry_agriculture = models.IntegerField(null=True)
    industry_arts_rec = models.IntegerField(null=True)
    industry_construction = models.IntegerField(null=True)
    industry_education = models.IntegerField(null=True)
    industry_finance_insurance = models.IntegerField(null=True)
    industry_health = models.IntegerField(null=True)
    industry_info_cultural = models.IntegerField(null=True)
    industry_management = models.IntegerField(null=True)
    industry_manufacturing = models.IntegerField(null=True)
    industry_mining = models.IntegerField(null=True)
    industry_other = models.IntegerField(null=True)
    industry_professional = models.IntegerField(null=True)
    industry_public_admin = models.IntegerField(null=True)
    industry_realestate = models.IntegerField(null=True)
    industry_retail = models.IntegerField(null=True)
    industry_transport = models.IntegerField(null=True)
    industry_utilities = models.IntegerField(null=True)
    industry_wholesale = models.IntegerField(null=True)
    labour_force_total = models.IntegerField(null=True)
    labour_force_male = models.FloatField(null=True)
    labour_force_female = models.FloatField(null=True)
    num_employed = models.IntegerField(null=True)
    num_unemployed = models.IntegerField(null=True)
    num_not_in_labour_force = models.IntegerField(null=True)
    labour_force_particip_tot_pct = models.FloatField(null=True)
    labour_force_particip_ml_pct = models.FloatField(null=True)
    labour_force_particip_fm_pct = models.FloatField(null=True)
    employment_rate = models.FloatField(null=True)
    unemployment_rate = models.FloatField(null=True)
    work_full_year_full_time = models.IntegerField(null=True)
    work_part_time = models.IntegerField(null=True)
    self_employed = models.IntegerField(null=True)
    total_lang_most_often_at_home = models.IntegerField(null=True)
    single_responses = models.IntegerField(null=True)
    official_languages = models.IntegerField(null=True)
    english = models.IntegerField(null=True)
    french = models.IntegerField(null=True)
    non_official_languages = models.IntegerField(null=True)
    aboriginal_languages = models.IntegerField(null=True)
    algonquian_languages = models.IntegerField(null=True)
    blackfoot = models.IntegerField(null=True)
    cree_montagnais_languages = models.IntegerField(null=True)
    atikamekw = models.IntegerField(null=True)
    montagnais_innu = models.IntegerField(null=True)
    moose_cree = models.IntegerField(null=True)
    naskapi = models.IntegerField(null=True)
    northern_east_cree = models.IntegerField(null=True)
    plains_cree = models.IntegerField(null=True)
    southern_east_cree = models.IntegerField(null=True)
    swampy_cree = models.IntegerField(null=True)
    woods_cree = models.IntegerField(null=True)
    cree_n_o_s = models.IntegerField(null=True)
    eastern_algonquian_languages = models.IntegerField(null=True)
    malecite = models.IntegerField(null=True)
    mikmaq = models.IntegerField(null=True)
    ojibway_potawatomi_languages = models.IntegerField(null=True)
    algonquin = models.IntegerField(null=True)
    ojibway = models.IntegerField(null=True)
    oji_cree = models.IntegerField(null=True)
    ottawa_odawa = models.IntegerField(null=True)
    algonquian_languages_n_i_e = models.IntegerField(null=True)
    athabaskan_languages = models.IntegerField(null=True)
    northern_athabaskan_languages = models.IntegerField(null=True)
    babine_wetsuweten = models.IntegerField(null=True)
    beaver = models.IntegerField(null=True)
    carrier = models.IntegerField(null=True)
    chilcotin = models.IntegerField(null=True)
    dene = models.IntegerField(null=True)
    dogrib_tlicho = models.IntegerField(null=True)
    gwichin = models.IntegerField(null=True)
    sarsi_sarcee = models.IntegerField(null=True)
    sekani = models.IntegerField(null=True)
    slavey_hare_languages = models.IntegerField(null=True)
    north_slavey_hare = models.IntegerField(null=True)
    south_slavey = models.IntegerField(null=True)
    slavey_n_o_s = models.IntegerField(null=True)
    tahltan_languages = models.IntegerField(null=True)
    kaska_nahani = models.IntegerField(null=True)
    tahltan = models.IntegerField(null=True)
    tutchone_languages = models.IntegerField(null=True)
    northern_tutchone = models.IntegerField(null=True)
    southern_tutchone = models.IntegerField(null=True)
    athabaskan_languages_n_i_e = models.IntegerField(null=True)
    haida = models.IntegerField(null=True)
    inuit_languages = models.IntegerField(null=True)
    inuinnaqtun_inuvialuktun = models.IntegerField(null=True)
    inuktitut = models.IntegerField(null=True)
    inuit_languages_n_i_e = models.IntegerField(null=True)
    iroquoian_languages = models.IntegerField(null=True)
    cayuga = models.IntegerField(null=True)
    mohawk = models.IntegerField(null=True)
    oneida = models.IntegerField(null=True)
    iroquoian_languages_n_i_e = models.IntegerField(null=True)
    kutenai = models.IntegerField(null=True)
    michif = models.IntegerField(null=True)
    salish_languages = models.IntegerField(null=True)
    comox = models.IntegerField(null=True)
    halkomelem = models.IntegerField(null=True)
    lillooet = models.IntegerField(null=True)
    okanagan = models.IntegerField(null=True)
    shuswap_secwepemctsin = models.IntegerField(null=True)
    squamish = models.IntegerField(null=True)
    straits = models.IntegerField(null=True)
    thompson_ntlakapamux = models.IntegerField(null=True)
    salish_languages_n_i_e = models.IntegerField(null=True)
    siouan_languages = models.IntegerField(null=True)
    dakota = models.IntegerField(null=True)
    stoney = models.IntegerField(null=True)
    siouan_languages_n_i_e = models.IntegerField(null=True)
    tlingit = models.IntegerField(null=True)
    tsimshian_languages = models.IntegerField(null=True)
    gitxsan_gitksan = models.IntegerField(null=True)
    nisgaa = models.IntegerField(null=True)
    tsimshian = models.IntegerField(null=True)
    wakashan_languages = models.IntegerField(null=True)
    haisla = models.IntegerField(null=True)
    heiltsuk = models.IntegerField(null=True)
    kwakiutl_kwakwala = models.IntegerField(null=True)
    nuu_chah_nulth_nootka = models.IntegerField(null=True)
    wakashan_languages_n_i_e = models.IntegerField(null=True)
    aboriginal_languages_n_o_s = models.IntegerField(null=True)
    non_aboriginal_languages = models.IntegerField(null=True)
    afro_asiatic_languages = models.IntegerField(null=True)
    berber_languages = models.IntegerField(null=True)
    kabyle = models.IntegerField(null=True)
    berber_languages_n_i_e = models.IntegerField(null=True)
    cushitic_languages = models.IntegerField(null=True)
    bilen = models.IntegerField(null=True)
    oromo = models.IntegerField(null=True)
    somali = models.IntegerField(null=True)
    cushitic_languages_n_i_e = models.IntegerField(null=True)
    semitic_languages = models.IntegerField(null=True)
    amharic = models.IntegerField(null=True)
    arabic = models.IntegerField(null=True)
    assyrian_neo_aramaic = models.IntegerField(null=True)
    chaldean_neo_aramaic = models.IntegerField(null=True)
    harari = models.IntegerField(null=True)
    hebrew = models.IntegerField(null=True)
    maltese = models.IntegerField(null=True)
    tigrigna = models.IntegerField(null=True)
    semitic_languages_n_i_e = models.IntegerField(null=True)
    afro_asiatic_languages_n_i_e = models.IntegerField(null=True)
    austro_asiatic_languages = models.IntegerField(null=True)
    khmer_cambodian = models.IntegerField(null=True)
    vietnamese = models.IntegerField(null=True)
    austro_asiatic_languages_n_i_e = models.IntegerField(null=True)
    austronesian_languages = models.IntegerField(null=True)
    bikol = models.IntegerField(null=True)
    cebuano = models.IntegerField(null=True)
    fijian = models.IntegerField(null=True)
    hiligaynon = models.IntegerField(null=True)
    ilocano = models.IntegerField(null=True)
    malagasy = models.IntegerField(null=True)
    malay = models.IntegerField(null=True)
    pampangan_kapampangan = models.IntegerField(null=True)
    pangasinan = models.IntegerField(null=True)
    tagalog_pilipino_filipino = models.IntegerField(null=True)
    waray_waray = models.IntegerField(null=True)
    austronesian_languages_n_i_e = models.IntegerField(null=True)
    creole_languages = models.IntegerField(null=True)
    haitian_creole = models.IntegerField(null=True)
    creole_n_o_s = models.IntegerField(null=True)
    creole_languages_n_i_e = models.IntegerField(null=True)
    dravidian_languages = models.IntegerField(null=True)
    kannada = models.IntegerField(null=True)
    malayalam = models.IntegerField(null=True)
    tamil = models.IntegerField(null=True)
    telugu = models.IntegerField(null=True)
    dravidian_languages_n_i_e = models.IntegerField(null=True)
    hmong_mien_languages = models.IntegerField(null=True)
    indo_european_languages = models.IntegerField(null=True)
    albanian = models.IntegerField(null=True)
    armenian = models.IntegerField(null=True)
    balto_slavic_languages = models.IntegerField(null=True)
    baltic_languages = models.IntegerField(null=True)
    latvian = models.IntegerField(null=True)
    lithuanian = models.IntegerField(null=True)
    slavic_languages = models.IntegerField(null=True)
    belarusan = models.IntegerField(null=True)
    bosnian = models.IntegerField(null=True)
    bulgarian = models.IntegerField(null=True)
    croatian = models.IntegerField(null=True)
    czech = models.IntegerField(null=True)
    macedonian = models.IntegerField(null=True)
    polish = models.IntegerField(null=True)
    russian = models.IntegerField(null=True)
    serbian = models.IntegerField(null=True)
    serbo_croatian = models.IntegerField(null=True)
    slovak = models.IntegerField(null=True)
    slovene_slovenian = models.IntegerField(null=True)
    ukrainian = models.IntegerField(null=True)
    slavic_languages_n_i_e = models.IntegerField(null=True)
    celtic_languages = models.IntegerField(null=True)
    scottish_gaelic = models.IntegerField(null=True)
    welsh = models.IntegerField(null=True)
    celtic_languages_n_i_e = models.IntegerField(null=True)
    germanic_languages = models.IntegerField(null=True)
    afrikaans = models.IntegerField(null=True)
    danish = models.IntegerField(null=True)
    dutch = models.IntegerField(null=True)
    frisian = models.IntegerField(null=True)
    german = models.IntegerField(null=True)
    icelandic = models.IntegerField(null=True)
    norwegian = models.IntegerField(null=True)
    swedish = models.IntegerField(null=True)
    vlaams_flemish = models.IntegerField(null=True)
    yiddish = models.IntegerField(null=True)
    germanic_languages_n_i_e = models.IntegerField(null=True)
    greek = models.IntegerField(null=True)
    indo_iranian_languages = models.IntegerField(null=True)
    indo_aryan_languages = models.IntegerField(null=True)
    bengali = models.IntegerField(null=True)
    gujarati = models.IntegerField(null=True)
    hindi = models.IntegerField(null=True)
    kashmiri = models.IntegerField(null=True)
    konkani = models.IntegerField(null=True)
    marathi = models.IntegerField(null=True)
    nepali = models.IntegerField(null=True)
    oriya_odia = models.IntegerField(null=True)
    punjabi_panjabi = models.IntegerField(null=True)
    sindhi = models.IntegerField(null=True)
    sinhala_sinhalese = models.IntegerField(null=True)
    urdu = models.IntegerField(null=True)
    iranian_languages = models.IntegerField(null=True)
    kurdish = models.IntegerField(null=True)
    pashto = models.IntegerField(null=True)
    persian_farsi = models.IntegerField(null=True)
    indo_iranian_languages_n_i_e = models.IntegerField(null=True)
    italic_romance_languages = models.IntegerField(null=True)
    catalan = models.IntegerField(null=True)
    italian = models.IntegerField(null=True)
    portuguese = models.IntegerField(null=True)
    romanian = models.IntegerField(null=True)
    spanish = models.IntegerField(null=True)
    italic_romance_langs_n_i_e = models.IntegerField(null=True)
    japanese = models.IntegerField(null=True)
    kartvelian_languages = models.IntegerField(null=True)
    georgian = models.IntegerField(null=True)
    korean = models.IntegerField(null=True)
    mongolic_languages = models.IntegerField(null=True)
    mongolian = models.IntegerField(null=True)
    niger_congo_languages = models.IntegerField(null=True)
    akan_twi = models.IntegerField(null=True)
    bamanankan = models.IntegerField(null=True)
    edo = models.IntegerField(null=True)
    ewe = models.IntegerField(null=True)
    fulah_pular_pulaar_fulfulde = models.IntegerField(null=True)
    ga = models.IntegerField(null=True)
    ganda = models.IntegerField(null=True)
    igbo = models.IntegerField(null=True)
    lingala = models.IntegerField(null=True)
    rundi_kirundi = models.IntegerField(null=True)
    kinyarwanda_rwanda = models.IntegerField(null=True)
    shona = models.IntegerField(null=True)
    swahili = models.IntegerField(null=True)
    wolof = models.IntegerField(null=True)
    yoruba = models.IntegerField(null=True)
    niger_congo_languages_n_i_e = models.IntegerField(null=True)
    nilo_saharan_languages = models.IntegerField(null=True)
    dinka = models.IntegerField(null=True)
    nilo_saharan_languages_n_i_e = models.IntegerField(null=True)
    sign_languages = models.IntegerField(null=True)
    american_sign_language = models.IntegerField(null=True)
    quebec_sign_language = models.IntegerField(null=True)
    sign_languages_n_i_e = models.IntegerField(null=True)
    sino_tibetan_languages = models.IntegerField(null=True)
    chinese_languages = models.IntegerField(null=True)
    cantonese = models.IntegerField(null=True)
    hakka = models.IntegerField(null=True)
    mandarin = models.IntegerField(null=True)
    min_dong = models.IntegerField(null=True)
    min_nan = models.IntegerField(null=True)
    wu_shanghainese = models.IntegerField(null=True)
    chinese_n_o_s = models.IntegerField(null=True)
    chinese_languages_n_i_e = models.IntegerField(null=True)
    tibeto_burman_languages = models.IntegerField(null=True)
    burmese = models.IntegerField(null=True)
    karenic_languages = models.IntegerField(null=True)
    tibetan = models.IntegerField(null=True)
    tibeto_burman_languages_n_i_e = models.IntegerField(null=True)
    tai_kadai_languages = models.IntegerField(null=True)
    lao = models.IntegerField(null=True)
    thai = models.IntegerField(null=True)
    tai_kadai_languages_n_i_e = models.IntegerField(null=True)
    turkic_languages = models.IntegerField(null=True)
    azerbaijani = models.IntegerField(null=True)
    turkish = models.IntegerField(null=True)
    uyghur = models.IntegerField(null=True)
    uzbek = models.IntegerField(null=True)
    turkic_languages_n_i_e = models.IntegerField(null=True)
    uralic_languages = models.IntegerField(null=True)
    estonian = models.IntegerField(null=True)
    finnish = models.IntegerField(null=True)
    hungarian = models.IntegerField(null=True)
    uralic_languages_n_i_e = models.IntegerField(null=True)
    other_languages_n_i_e = models.IntegerField(null=True)
    multiple_responses = models.IntegerField(null=True)
    english_and_french = models.IntegerField(null=True)
    english_and_non_official_langs = models.IntegerField(null=True)
    french_and_non_official_lang = models.IntegerField(null=True)
    english_french_non_offcl_lang = models.IntegerField(null=True)
    total_other_langs = models.IntegerField(null=True)
    othr_none = models.IntegerField(null=True)
    othr_english = models.IntegerField(null=True)
    othr_french = models.IntegerField(null=True)
    othr_non_official_language = models.IntegerField(null=True)
    othr_aboriginal = models.IntegerField(null=True)
    othr_non_aboriginal = models.IntegerField(null=True)
    othr_english_and_french = models.IntegerField(null=True)
    othr_english_non_official_lang = models.IntegerField(null=True)
    othr_french_non_official_lang = models.IntegerField(null=True)
    english_french_non_offl_lang = models.IntegerField(null=True)
    occupation_management = models.IntegerField(null=True)
    occupation_business = models.IntegerField(null=True)
    occupation_science = models.IntegerField(null=True)
    occupation_health = models.IntegerField(null=True)
    occupation_education_law = models.IntegerField(null=True)
    occupation_art_culture_rec = models.IntegerField(null=True)
    occupation_sales_service = models.IntegerField(null=True)
    occupation_trades_transport = models.IntegerField(null=True)
    occupation_resources = models.IntegerField(null=True)
    occupation_manufacturing = models.IntegerField(null=True)
    pop_age_14_and_under = models.IntegerField(null=True)
    pop_age_4_and_under = models.IntegerField(null=True)
    pop_age_5_9 = models.IntegerField(null=True)
    pop_age_10_14 = models.IntegerField(null=True)
    pop_age_15_64 = models.IntegerField(null=True)
    pop_age_15_19 = models.IntegerField(null=True)
    pop_age_20_24 = models.IntegerField(null=True)
    pop_age_25_29 = models.IntegerField(null=True)
    pop_age_30_34 = models.IntegerField(null=True)
    pop_age_35_39 = models.IntegerField(null=True)
    pop_age_40_44 = models.IntegerField(null=True)
    pop_age_45_49 = models.IntegerField(null=True)
    pop_age_50_54 = models.IntegerField(null=True)
    pop_age_55_59 = models.IntegerField(null=True)
    pop_age_60_64 = models.IntegerField(null=True)
    pop_age_65_and_over = models.IntegerField(null=True)
    pop_age_65_69 = models.IntegerField(null=True)
    pop_age_70_74 = models.IntegerField(null=True)
    pop_age_75_79 = models.IntegerField(null=True)
    pop_age_80_84 = models.IntegerField(null=True)
    pop_age_85_and_over = models.IntegerField(null=True)
    pop_age_85_89 = models.IntegerField(null=True)
    pop_age_90_94 = models.IntegerField(null=True)
    pop_age_95_99 = models.IntegerField(null=True)
    pop_age_100_and_over = models.IntegerField(null=True)
    pop_average_age = models.FloatField(null=True)
    pop_median_age = models.FloatField(null=True)
    pop_age_4_and_under_male = models.IntegerField(null=True)
    pop_age_5_9_male = models.IntegerField(null=True)
    pop_age_10_14_male = models.IntegerField(null=True)
    pop_age_14_and_under_male = models.IntegerField(null=True)
    pop_age_15_19_male = models.IntegerField(null=True)
    pop_age_15_64_male = models.IntegerField(null=True)
    pop_age_20_24_male = models.IntegerField(null=True)
    pop_age_25_29_male = models.IntegerField(null=True)
    pop_age_30_34_male = models.IntegerField(null=True)
    pop_age_35_39_male = models.IntegerField(null=True)
    pop_age_40_44_male = models.IntegerField(null=True)
    pop_age_45_49_male = models.IntegerField(null=True)
    pop_age_50_54_male = models.IntegerField(null=True)
    pop_age_55_59_male = models.IntegerField(null=True)
    pop_age_60_64_male = models.IntegerField(null=True)
    pop_age_65_69_male = models.IntegerField(null=True)
    pop_age_65_and_over_male = models.IntegerField(null=True)
    pop_age_70_74_male = models.IntegerField(null=True)
    pop_age_75_79_male = models.IntegerField(null=True)
    pop_age_80_84_male = models.IntegerField(null=True)
    pop_age_85_89_male = models.IntegerField(null=True)
    pop_age_85_and_over_male = models.IntegerField(null=True)
    pop_age_90_94_male = models.IntegerField(null=True)
    pop_age_95_99_male = models.IntegerField(null=True)
    pop_age_100_and_over_male = models.IntegerField(null=True)
    pop_average_age_male = models.IntegerField(null=True)
    pop_median_age_male = models.IntegerField(null=True)
    pop_age_4_and_under_female = models.IntegerField(null=True)
    pop_age_5_9_female = models.IntegerField(null=True)
    pop_age_10_14_female = models.IntegerField(null=True)
    pop_age_14_and_under_female = models.IntegerField(null=True)
    pop_age_15_19_female = models.IntegerField(null=True)
    pop_age_15_64_female = models.IntegerField(null=True)
    pop_age_20_24_female = models.IntegerField(null=True)
    pop_age_25_29_female = models.IntegerField(null=True)
    pop_age_30_34_female = models.IntegerField(null=True)
    pop_age_35_39_female = models.IntegerField(null=True)
    pop_age_40_44_female = models.IntegerField(null=True)
    pop_age_45_49_female = models.IntegerField(null=True)
    pop_age_50_54_female = models.IntegerField(null=True)
    pop_age_55_59_female = models.IntegerField(null=True)
    pop_age_60_64_female = models.IntegerField(null=True)
    pop_age_65_69_female = models.IntegerField(null=True)
    pop_age_65_and_over_female = models.IntegerField(null=True)
    pop_age_70_74_female = models.IntegerField(null=True)
    pop_age_75_79_female = models.IntegerField(null=True)
    pop_age_80_84_female = models.IntegerField(null=True)
    pop_age_85_89_female = models.IntegerField(null=True)
    pop_age_85_and_over_female = models.IntegerField(null=True)
    pop_age_90_94_female = models.IntegerField(null=True)
    pop_age_95_99_female = models.IntegerField(null=True)
    pop_age_100_and_over_female = models.IntegerField(null=True)
    pop_average_age_female = models.IntegerField(null=True)
    pop_median_age_female = models.IntegerField(null=True)
    total_private_dwellings = models.IntegerField(null=True)
    privte_dwellings_usual_resdnts = models.IntegerField(null=True)
    dwelling_median_value = models.IntegerField(null=True)
    apartments_flat_duplex = models.IntegerField(null=True)
    apartments_short_bldg = models.IntegerField(null=True)
    apartments_tall_bldg = models.IntegerField(null=True)
    avg_household_size = models.FloatField(null=True)
    avg_mthly_shlter_costs_ownd = models.IntegerField(null=True)
    avg_mthly_shlter_costs_rented = models.IntegerField(null=True)
    median_mthly_shlter_costs_ownd = models.IntegerField(null=True)
    median_mthly_shlter_costs_rntd = models.IntegerField(null=True)
    moveable_dwelling = models.IntegerField(null=True)
    num_spending_30pctplus_shelter = models.IntegerField(null=True)
    num_spending_lt30pct_shelter = models.IntegerField(null=True)
    other_attached_dwelling = models.IntegerField(null=True)
    pct_owner_hslds_shelter_30pctp = models.FloatField(null=True)
    pct_tennt_hslds_shelter_30pctp = models.FloatField(null=True)
    semi_detached_house = models.IntegerField(null=True)
    single_detached_house = models.IntegerField(null=True)
    total_private_hslds_band_hsng = models.IntegerField(null=True)
    total_private_hslds_by_size = models.IntegerField(null=True)
    total_private_hslds_by_tenure = models.IntegerField(null=True)
    total_private_hslds_owned = models.IntegerField(null=True)
    total_private_hslds_rented = models.IntegerField(null=True)
    visible_minority_num_male = models.IntegerField(null=True)
    visible_minority_num_female = models.IntegerField(null=True)
    visible_minority_pct_male = models.FloatField(null=True)
    visible_minority_pct_female = models.FloatField(null=True)
    feature_area_sqm = models.FloatField(null=True)
    feature_length_m = models.FloatField(null=True)

    class Meta:
        ordering = ("census_division_id", )

    def __str__(self):
        return self.census_division_name
