metadata = {
    'protocolName': 'gtseq pcr2',
    'author': 'aam, updated 3/8/23',
    'source': 'Protocol Library',
    'apiLevel': '2.0'
    }


def run(protocol):

    tc_mod = protocol.load_module('thermocycler')



    # Close lid
    if tc_mod.lid_position != 'closed':
        tc_mod.close_lid()

    # lid temperature set
    tc_mod.set_lid_temperature(105)

    # initialization
    tc_mod.set_block_temperature(95, hold_time_minutes=15,
                                 block_max_volume=10)

    # run profile
    profile = [
        {'temperature': 98, 'hold_time_seconds': 10},
        {'temperature': 65, 'hold_time_seconds': 30,},
        {'temperature': 72, 'hold_time_seconds': 30}
    ]

    tc_mod.execute_profile(steps=profile, repetitions=10,
                           block_max_volume=10)
                           
	# final elongation

    tc_mod.set_block_temperature(72, hold_time_minutes=5,
                                 block_max_volume=10)
                                 
    # final hold
    tc_mod.deactivate_lid()
    tc_mod.set_block_temperature(4)
