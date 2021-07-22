import os
import shutil


def backup_vanilla_assets(sc_path: str, vanilla_dir: str) -> bool:
    """
    Back-up the games assets
    :param sc_path: <str> path to stronghold crusader installation root dir
    :param vanilla_dir: <str> path to the vanilla directory
    :return: <bool> True if backup was succesful
    """
    speech_dir = os.path.join(sc_path, 'fx', 'Speech')
    binks_dir = os.path.join(sc_path, 'binks')
    aiv_dir = os.path.join(sc_path, 'aiv')

    fx_files = ['ab_siege_01.wav', 'ab_willattack_01.wav', 'ab_kick_player_01.wav', 'ab_thanks_01.wav', 'ab_req_01.wav',
                'ab_anger_02.wav', 'ab_team_losing_01.wav', 'ab_noattack_02.wav', 'ab_nervous_01.wav',
                'ab_ally_death_01.wav', 'ab_plead_01.wav', 'ab_helpsent_01.wav', 'ab_help_01.wav',
                'ab_boast_01.wav', 'ab_extra_01.wav', 'ab_vict_02.wav', 'ab_nervous_02.wav', 'ab_noattack_01.wav',
                'ab_vict_04.wav', 'ab_team_winning_01.wav', 'ab_vict_01.wav', 'ab_add_player_01.wav', 'ab_sent_01.wav',
                'ab_notsent_01.wav', 'ab_nohelp_01.wav', 'ab_taunt_02.wav', 'ab_taunt_04.wav', 'ab_nohelp_02.wav',
                'ab_vict_03.wav', 'ab_congrats_01.wav', 'ab_anger_01.wav', 'ab_taunt_03.wav', 'ab_taunt_01.wav',
                'ca_taunt_04.wav', 'ca_nohelp_01.wav', 'ca_help_01.wav', 'ca_nervous_02.wav', 'ca_anger_01.wav',
                'ca_vict_01.wav', 'ca_sent_01.wav', 'ca_anger_02.wav', 'ca_kick_player_01.wav', 'ca_team_losing_01.wav',
                'ca_plead_01.wav', 'ca_vict_04.wav', 'ca_team_winning_01.wav', 'ca_congrats_01.wav',
                'ca_noattack_01.wav', 'ca_boast_01.wav', 'ca_siege_01.wav', 'ca_ally_death_01.wav',
                'ca_willattack_01.wav', 'ca_notsent_01.wav', 'ca_nervous_01.wav', 'ca_vict_03.wav', 'ca_taunt_03.wav',
                'ca_thanks_01.wav', 'ca_vict_02.wav', 'ca_req_01.wav', 'ca_taunt_02.wav', 'ca_taunt_01.wav',
                'ca_helpsent_01.wav', 'ca_add_player_01.wav', 'ca_noattack_02.wav', 'ca_extra_01.wav',
                'ca_nohelp_02.wav', 'em_nervous_02.wav', 'em_team_losing_01.wav', 'em_noattack_01.wav',
                'em_ally_death_01.wav', 'em_taunt_01.wav', 'em_vict_01.wav', 'em_vict_04.wav', 'em_nohelp_02.wav',
                'em_anger_01.wav', 'em_taunt_04.wav', 'em_notsent_01.wav', 'em_vict_02.wav', 'em_anger_02.wav',
                'em_add_player_01.wav', 'em_extra_01.wav', 'em_req_01.wav', 'em_plead_01.wav', 'em_vict_03.wav',
                'em_taunt_02.wav', 'em_boast_01.wav', 'em_nohelp_01.wav', 'em_noattack_02.wav', 'em_willattack_01.wav',
                'em_kick_player_01.wav', 'em_congrats_01.wav', 'em_thanks_01.wav', 'em_taunt_03.wav',
                'em_team_winning_01.wav', 'em_sent_01.wav', 'em_help_01.wav', 'em_helpsent_01.wav', 'em_nervous_01.wav',
                'em_siege_01.wav', 'fr_vict_01.wav', 'fr_thanks_01.wav', 'fr_kick_player_01.wav', 'fr_boast_01.wav',
                'fr_notsent_01.wav', 'fr_vict_04.wav', 'fr_add_player_01.wav', 'fr_noattack_01.wav',
                'fr_congrats_01.wav', 'fr_nohelp_02.wav', 'fr_helpsent_01.wav', 'fr_nohelp_01.wav', 'fr_siege_01.wav',
                'fr_taunt_02.wav', 'fr_vict_03.wav', 'fr_taunt_03.wav', 'fr_vict_02.wav', 'fr_plead_01.wav',
                'fr_sent_01.wav', 'fr_willattack_01.wav', 'fr_noattack_02.wav', 'fr_team_winning_01.wav',
                'fr_taunt_04.wav', 'fr_ally_death_01.wav', 'fr_taunt_01.wav', 'fr_team_losing_01.wav', 'fr_req_01.wav',
                'fr_help_01.wav', 'fr_nervous_01.wav', 'fr_nervous_02.wav', 'fr_extra_01.wav', 'fr_anger_01.wav',
                'fr_anger_02.wav', 'ma_ally_death_01.wav', 'ma_siege_01.wav', 'ma_add_player_01.wav',
                'ma_team_losing_01.wav', 'ma_vict_02.wav', 'ma_nervous_01.wav', 'ma_noattack_01.wav', 'ma_req_01.wav',
                'ma_taunt_01.wav', 'ma_taunt_04.wav', 'ma_help_01.wav', 'ma_nohelp_02.wav', 'ma_vict_04.wav',
                'ma_vict_03.wav', 'ma_helpsent_01.wav', 'ma_boast_01.wav', 'ma_congrats_01.wav', 'ma_nohelp_01.wav',
                'ma_noattack_02.wav', 'ma_taunt_03.wav', 'ma_plead_01.wav', 'ma_taunt_02.wav', 'ma_anger_02.wav',
                'ma_sent_01.wav', 'ma_willattack_01.wav', 'ma_notsent_01.wav', 'ma_team_winning_01.wav',
                'ma_nervous_02.wav', 'ma_vict_01.wav', 'ma_kick_player_01.wav', 'ma_extra_01.wav', 'ma_thanks_01.wav',
                'ma_anger_01.wav', 'ni_taunt_02.wav', 'ni_vict_02.wav', 'ni_nervous_01.wav', 'ni_nervous_02.wav',
                'ni_taunt_04.wav', 'ni_team_losing_01.wav', 'ni_thanks_01.wav', 'ni_vict_04.wav', 'ni_vict_03.wav',
                'ni_ally_death_01.wav', 'ni_noattack_02.wav', 'ni_kick_player_01.wav', 'ni_vict_01.wav',
                'ni_noattack_01.wav', 'ni_congrats_01.wav', 'ni_helpsent_01.wav', 'ni_help_01.wav', 'ni_nohelp_02.wav',
                'ni_notsent_01.wav', 'ni_add_player_01.wav', 'ni_anger_02.wav', 'ni_req_01.wav', 'ni_boast_01.wav',
                'ni_team_winning_01.wav', 'ni_extra_01.wav', 'ni_siege_01.wav', 'ni_anger_01.wav', 'ni_plead_01.wav',
                'ni_taunt_01.wav', 'ni_nohelp_01.wav', 'ni_taunt_03.wav', 'ni_sent_01.wav', 'ni_willattack_01.wav',
                'pg_taunt_08.wav', 'pg_plead_03.wav', 'pg_taunt_07.wav', 'pg_plead_01.wav', 'pg_vict_02.wav',
                'pg_add_player.wav', 'pg_taunt_03.wav', 'pg_anger_04.wav', 'pg_taunt_06.wav', 'pg_taunt_01.wav',
                'pg_anger_01.wav', 'pg_taunt_05.wav', 'pg_anger_02.wav', 'pg_anger_03.wav', 'pg_vict_01.wav',
                'pg_taunt_04.wav', 'pg_taunt_02.wav', 'pg_plead_04.wav', 'pg_kick_player.wav', 'pg_vict_03.wav',
                'pg_vict_04.wav', 'pg_plead_02.wav', 'Pig_Attack.wav', 'Pig_Defeat.wav',
                'ph_taunt_02.wav', 'ph_plead_01.wav', 'ph_siege_01.wav', 'ph_vict_03.wav', 'ph_vict_02.wav',
                'ph_sent_01.wav', 'ph_willattack_01.wav', 'ph_taunt_04.wav', 'ph_taunt_01.wav', 'ph_req_01.wav',
                'ph_thanks_01.wav', 'ph_ally_death_01.wav', 'ph_team_winning_01.wav', 'ph_extra_01.wav',
                'ph_vict_01.wav', 'ph_helpsent_01.wav', 'ph_add_player_01.wav', 'ph_anger_02.wav', 'ph_nohelp_01.wav',
                'ph_nervous_01.wav', 'ph_help_01.wav', 'ph_taunt_03.wav', 'ph_noattack_01.wav', 'ph_nohelp_02.wav',
                'ph_vict_04.wav', 'ph_notsent_01.wav', 'ph_noattack_02.wav', 'ph_congrats_01.wav', 'ph_anger_01.wav',
                'ph_team_losing_01.wav', 'ph_nervous_02.wav', 'ph_kick_player_01.wav', 'ph_boast_01.wav',
                'ri_nohelp_02.wav', 'ri_siege_01.wav', 'ri_team_losing_01.wav', 'ri_notsent_01.wav', 'ri_nohelp_01.wav',
                'ri_anger_01.wav', 'ri_helpsent_01.wav', 'ri_boast_01.wav', 'ri_nervous_02.wav', 'ri_taunt_04.wav',
                'ri_taunt_02.wav', 'ri_vict_03.wav', 'ri_vict_02.wav', 'ri_kick_player_01.wav', 'ri_sent_01.wav',
                'ri_team_winning_01.wav', 'ri_nervous_01.wav', 'ri_extra_01.wav', 'ri_taunt_03.wav', 'ri_plead_01.wav',
                'ri_help_01.wav', 'ri_vict_01.wav', 'ri_noattack_02.wav', 'ri_vict_04.wav', 'ri_req_01.wav',
                'ri_anger_02.wav', 'ri_add_player_01.wav', 'ri_taunt_01.wav', 'ri_congrats_01.wav',
                'ri_noattack_01.wav', 'ri_thanks_01.wav', 'ri_ally_death_01.wav', 'ri_willattack_01.wav',
                'rt_anger_04.wav', 'rt_taunt_06.wav', 'rt_anger_03.wav', 'rt_vict_04.wav', 'rt_taunt_08.wav',
                'rt_add_player.wav', 'rt_vict_01.wav', 'rt_vict_02.wav', 'rt_taunt_05.wav', 'rt_anger_02.wav',
                'rt_vict_03.wav', 'rt_plead_04.wav', 'rt_taunt_01.wav', 'rt_plead_02.wav', 'rt_anger_01.wav',
                'rt_taunt_03.wav', 'rt_plead_01.wav', 'rt_taunt_02.wav', 'rt_taunt_07.wav', 'rt_taunt_04.wav',
                'rt_plead_03.wav', 'rt_kick_player.wav', 'Rat_Attack.wav', 'Rat_Defeat.wav',
                'sa_plead_01.wav', 'sa_thanks_01.wav', 'sa_sent_01.wav', 'sa_willattack_01.wav', 'sa_nohelp_01.wav',
                'sa_nervous_02.wav', 'sa_helpsent_01.wav', 'sa_anger_01.wav', 'sa_notsent_01.wav', 'sa_nervous_01.wav',
                'sa_noattack_01.wav', 'sa_ally_death_01.wav', 'sa_req_01.wav', 'sa_taunt_02.wav', 'sa_help_01.wav',
                'sa_noattack_02.wav', 'sa_vict_04.wav', 'sa_team_losing_01.wav', 'sa_taunt_01.wav',
                'sa_add_player_01.wav', 'sa_boast_01.wav', 'sa_taunt_04.wav', 'sa_vict_03.wav', 'sa_nohelp_02.wav',
                'sa_siege_01.wav', 'sa_kick_player_01.wav', 'sa_vict_02.wav', 'sa_vict_01.wav', 'sa_anger_02.wav',
                'sa_congrats_01.wav', 'sa_extra_01.wav', 'sa_taunt_03.wav', 'sa_team_winning_01.wav',
                'sh_vict_03.wav', 'sh_willattack_01.wav', 'sh_ally_death_01.wav', 'sh_taunt_03.wav',
                'sh_nervous_02.wav', 'sh_taunt_01.wav', 'sh_helpsent_01.wav', 'sh_add_player_01.wav',
                'sh_nohelp_02.wav', 'sh_extra_01.wav', 'sh_kick_player_01.wav', 'sh_sent_01.wav', 'sh_help_01.wav',
                'sh_vict_04.wav', 'sh_vict_02.wav', 'sh_req_01.wav', 'sh_vict_01.wav', 'sh_team_losing_01.wav',
                'sh_thanks_01.wav', 'sh_congrats_01.wav', 'sh_team_winning_01.wav', 'sh_taunt_02.wav',
                'sh_anger_01.wav', 'sh_taunt_04.wav', 'sh_anger_02.wav', 'sh_nervous_01.wav', 'sh_siege_01.wav',
                'sh_noattack_02.wav', 'sh_notsent_01.wav', 'sh_plead_01.wav', 'sh_nohelp_01.wav', 'sh_noattack_01.wav',
                'sh_boast_01.wav',
                'sn_taunt_02.wav', 'sn_plead_01.wav', 'sn_taunt_04.wav', 'sn_plead_04.wav', 'sn_taunt_05.wav',
                'sn_plead_02.wav', 'sn_taunt_03.wav', 'sn_kick_player.wav', 'sn_vict_01.wav', 'sn_anger_02.wav',
                'sn_taunt_06.wav', 'sn_vict_02.wav', 'sn_vict_04.wav', 'sn_add_player.wav', 'sn_taunt_07.wav',
                'sn_anger_04.wav', 'sn_anger_03.wav', 'sn_vict_03.wav', 'sn_plead_03.wav', 'sn_taunt_08.wav',
                'sn_anger_01.wav', 'sn_taunt_01.wav', 'Snake_Attack.wav', 'Snake_Defeat.wav',
                'su_vict_04.wav', 'su_willattack_01.wav', 'su_anger_01.wav', 'su_add_player_01.wav', 'su_siege_01.wav',
                'su_taunt_04.wav', 'su_thanks_01.wav', 'su_ally_death_01.wav', 'su_vict_03.wav', 'su_taunt_03.wav',
                'su_sent_01.wav', 'su_noattack_02.wav', 'su_nervous_01.wav', 'su_req_01.wav', 'su_taunt_02.wav',
                'su_helpsent_01.wav', 'su_extra_01.wav', 'su_vict_02.wav', 'su_nohelp_02.wav', 'su_noattack_01.wav',
                'su_notsent_01.wav', 'su_vict_01.wav', 'su_nervous_02.wav', 'su_nohelp_01.wav', 'su_plead_01.wav',
                'su_boast_01.wav', 'su_help_01.wav', 'su_kick_player_01.wav', 'su_team_winning_01.wav',
                'su_congrats_01.wav', 'su_team_losing_01.wav', 'su_taunt_01.wav', 'su_anger_02.wav',
                'wa_nohelp_02.wav', 'wa_ally_death_01.wav', 'wa_team_losing_01.wav', 'wa_noattack_01.wav',
                'wa_vict_02.wav', 'wa_sent_01.wav', 'wa_thanks_01.wav', 'wa_nervous_01.wav', 'wa_nohelp_01.wav',
                'wa_nervous_02.wav', 'wa_willattack_01.wav', 'wa_congrats_01.wav', 'wa_taunt_02.wav', 'wa_vict_01.wav',
                'wa_siege_01.wav', 'wa_help_01.wav', 'wa_kick_player_01.wav', 'wa_plead_01.wav', 'wa_extra_01.wav',
                'wa_vict_04.wav', 'wa_anger_02.wav', 'wa_notsent_01.wav', 'wa_anger_01.wav', 'wa_taunt_04.wav',
                'wa_team_winning_01.wav', 'wa_taunt_01.wav', 'wa_noattack_02.wav', 'wa_helpsent_01.wav',
                'wa_boast_01.wav', 'wa_vict_03.wav', 'wa_add_player_01.wav', 'wa_req_01.wav', 'wa_taunt_03.wav',
                'wf_taunt_01.wav', 'wf_taunt_02.wav', 'wf_plead_03.wav', 'wf_add_player.wav', 'wf_plead_04.wav',
                'wf_kick_player.wav', 'wf_anger_04.wav', 'wf_taunt_08.wav', 'wf_anger_03.wav', 'wf_plead_01.wav',
                'wf_plead_02.wav', 'wf_anger_02.wav', 'wf_taunt_07.wav', 'wf_vict_02.wav', 'wf_vict_04.wav',
                'wf_vict_01.wav', 'wf_taunt_03.wav', 'wf_anger_01.wav', 'wf_taunt_06.wav', 'wf_taunt_04.wav',
                'wf_vict_03.wav', 'wf_taunt_05.wav', 'Wolf_Defeat.wav', 'Wolf_Attack.wav']

    bik_files = ['abbot_confident.bik', 'abbot_natural.bik', 'abbot_nervous.bik', 'abbot_angry.bik',
                 'bad_arab_nervous.bik', 'bad_arab_anger.bik', 'bad_arab_taunt.bik', 'bad_arab_natural.bik',
                 'emir_angry.bik', 'emir_nervous.bik', 'emir_taunt.bik', 'emir_natural.bik',
                 'fred_taunt.bik', 'fred_anger.bik', 'fred_nervous.bik', 'fred_natural.bik',
                 'ma_angry.bik', 'ma_natural.bik', 'ma_taunt.bik', 'ma_nervous.bik',
                 'nazir_taunt.bik', 'nazir_natural.bik', 'nazir_nervous.bik', 'nazir_angry.bik',
                 'philip_taunt.bik', 'philip_anger.bik', 'philip_nervous.bik', 'philip_natural.bik',
                 'richard_anger.bik', 'richard_nervous.bik', 'richard_natural.bik', 'richard_taunting.bik',
                 'rt_vict1.bik', 'rt_plead2.bik', 'rt_vict2.bik', 'rt_plead3.bik', 'rt_plead1.bik', 'rt_anger1.bik',
                 'rt_taunt1.bik', 'rt_taunt2.bik',
                 'saladin_taunting.bik', 'saladin_angry.bik', 'saladin_nervous.bik', 'saladin_natural.bik',
                 'sheriff_anger.bik', 'sheriff_taunt.bik', 'sheriff_natural.bik', 'sheriff_nervous.bik',
                 'sn_plead2.bik', 'sn_anger1.bik', 'sn_taunt1.bik', 'sn_plead1.bik', 'sn_vict2.bik', 'sn_taunt2.bik',
                 'sn_vict1.bik',
                 'sultan_natural.bik', 'sultan_taunt.bik', 'sultan_nervous.bik', 'sultan_anger.bik',
                 'vizir_taunt.bik', 'vizir_nervous.bik', 'vizir_angry.bik', 'vizir_natural.bik',
                 'wf_plead2.bik', 'wf_taunt1.bik', 'wf_vict2.bik', 'wf_anger1.bik', 'wf_taunt2.bik', 'wf_plead1.bik',
                 'wf_vict1.bik']

    aiv_files = ['Abbot1.aiv', 'Abbot2.aiv', 'Abbot3.aiv', 'Abbot4.aiv', 'Abbot5.aiv', 'Abbot6.aiv', 'Abbot7.aiv',
                 'Abbot8.aiv', 'Emir1.aiv', 'Emir2.aiv', 'Emir3.aiv', 'Emir4.aiv', 'Emir5.aiv', 'Emir6.aiv',
                 'Emir7.aiv', 'Emir8.aiv', 'Nizar1.aiv', 'Nizar2.aiv', 'Nizar3.aiv', 'Nizar4.aiv', 'Nizar5.aiv',
                 'Nizar6.aiv', 'Nizar7.aiv', 'Nizar8.aiv', 'Sultan1.aiv', 'Sultan2.aiv', 'Sultan3.aiv', 'Sultan4.aiv',
                 'Sultan5.aiv', 'Sultan6.aiv', 'Sultan7.aiv', 'Sultan8.aiv', 'caliph1.aiv', 'caliph2.aiv',
                 'caliph3.aiv', 'caliph4.aiv', 'caliph5.aiv', 'caliph6.aiv', 'caliph7.aiv', 'caliph8.aiv',
                 'frederick1.aiv', 'frederick2.aiv', 'frederick3.aiv', 'frederick4.aiv', 'frederick5.aiv',
                 'frederick6.aiv', 'frederick7.aiv', 'frederick8.aiv', 'marshal1.aiv', 'marshal2.aiv', 'marshal3.aiv',
                 'marshal4.aiv', 'marshal5.aiv', 'marshal6.aiv', 'marshal7.aiv', 'marshal8.aiv', 'phillip1.aiv',
                 'phillip2.aiv', 'phillip3.aiv', 'phillip4.aiv', 'phillip5.aiv', 'phillip6.aiv', 'phillip7.aiv',
                 'phillip8.aiv', 'pig1.aiv', 'pig2.aiv', 'pig3.aiv', 'pig4.aiv', 'pig5.aiv', 'pig6.aiv', 'pig7.aiv',
                 'pig8.aiv', 'rat1.aiv', 'rat2.aiv', 'rat3.aiv', 'rat4.aiv', 'rat5.aiv', 'rat6.aiv', 'rat7.aiv',
                 'rat8.aiv', 'richard1.aiv', 'richard2.aiv', 'richard3.aiv', 'richard4.aiv', 'richard5.aiv',
                 'richard6.aiv', 'richard7.aiv', 'richard8.aiv', 'saladin1.aiv', 'saladin2.aiv', 'saladin3.aiv',
                 'saladin4.aiv', 'saladin5.aiv', 'saladin6.aiv', 'saladin7.aiv', 'saladin8.aiv', 'sheriff1.aiv',
                 'sheriff2.aiv', 'sheriff3.aiv', 'sheriff4.aiv', 'sheriff5.aiv', 'sheriff6.aiv', 'sheriff7.aiv',
                 'sheriff8.aiv', 'snake1.aiv', 'snake2.aiv', 'snake3.aiv', 'snake4.aiv', 'snake5.aiv', 'snake6.aiv',
                 'snake7.aiv', 'snake8.aiv', 'wazir1.aiv', 'wazir2.aiv', 'wazir3.aiv', 'wazir4.aiv', 'wazir5.aiv',
                 'wazir6.aiv', 'wazir7.aiv', 'wazir8.aiv', 'wolf1.aiv', 'wolf2.aiv', 'wolf3.aiv', 'wolf4.aiv',
                 'wolf5.aiv', 'wolf5E.aiv', 'wolf6.aiv', 'wolf7.aiv', 'wolf8.aiv']

    # back up speech files
    speech_backup_dir = os.path.join(vanilla_dir, 'speech')
    if not os.path.exists(speech_backup_dir):
        os.makedirs(speech_backup_dir)
    for file in fx_files:
        shutil.copy2(os.path.join(speech_dir, file), os.path.join(speech_backup_dir, file))

    # back up bink files
    binks_backup_dir = os.path.join(vanilla_dir, 'binks')
    if not os.path.exists(binks_backup_dir):
        os.makedirs(binks_backup_dir)
    for file in bik_files:
        shutil.copy2(os.path.join(binks_dir, file), os.path.join(binks_backup_dir, file))

    # back up aiv files
    aiv_backup_dir = os.path.join(vanilla_dir, 'aiv')
    if not os.path.exists(aiv_backup_dir):
        os.makedirs(aiv_backup_dir)
    for file in aiv_files:
        shutil.copy2(os.path.join(aiv_dir, file), os.path.join(aiv_backup_dir, file))

    return True
