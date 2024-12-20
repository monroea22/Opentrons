# one pcr plate worth of samples half skirt inserted into alumininum block or green skirt plate
# into 1.5 ml or 2 ml tube

metadata = {
    'protocolName': 'lca1 abcde pool',
    'author': 'AAM, last updated 4/10/23',
    'description': 'Pool GT seq samples (variable volumes) into one tube.',
    'apiLevel': '2.11'
}

def run(protocol):
    ########## EDIT THESE RUN OPTIONS AS NEEDED ##########

    # location of p20 single channel ('left' or 'right', all lowercase and in single quotes)
    pipette_mount_20 = 'right'

    # type of tube samples will be pooled into ('1.5ml' or '2ml')
    tube_type = '1.5ml'

    # number of plates (integar, max 9)
    num_plates = 5

    # sample volume info
    # paste data from csv here (in between '''  ''')
    input_data = '''
    source_slot,source_well,tube_well,vol_dna
	3,A1,A1,1.65
	3,A2,A1,1.72
	3,A3,A1,1.89
	3,A4,A1,1.56
	3,A5,A1,1.38
	3,A6,A1,2.32
	3,A7,A1,2.55
	3,A8,A1,3.25
	3,A9,A1,1.99
	3,A10,A1,3.12
	3,A11,A1,1.5
	3,A12,A1,1.98
	3,B1,A1,4.28
	3,B2,A1,3.05
	3,B3,A1,2.59
	3,B4,A1,3.22
	3,B5,A1,2.88
	3,B6,A1,2.78
	3,B7,A1,3.11
	3,B8,A1,2.22
	3,B9,A1,2.06
	3,B10,A1,1.97
	3,B11,A1,5.2
	3,B12,A1,2.22
	3,C1,A1,2.15
	3,C2,A1,1.56
	3,C3,A1,2.12
	3,C4,A1,1.46
	3,C5,A1,1.87
	3,C6,A1,1.07
	3,C7,A1,1.29
	3,C8,A1,1.17
	3,C9,A1,1.42
	3,C10,A1,2.28
	3,C11,A1,1.67
	3,C12,A1,1.67
	3,D1,A1,1.73
	3,D2,A1,2.17
	3,D3,A1,1.28
	3,D4,A1,2.02
	3,D6,A1,1.01
	3,D7,A1,1.55
	3,D8,A1,1.84
	3,D9,A1,0.98
	3,D10,A1,1.66
	3,D11,A1,1.44
	3,D12,A1,1.36
	3,E1,A1,1.33
	3,E2,A1,1.99
	3,E3,A1,1.58
	3,E4,A1,1.1
	3,E5,A1,1.32
	3,E6,A1,1.51
	3,E7,A1,1.7
	3,E8,A1,1.08
	3,E9,A1,1.06
	3,E10,A1,1.26
	3,E11,A1,1.19
	3,E12,A1,1.91
	3,F1,A1,1.91
	3,F2,A1,2.03
	3,F3,A1,1.38
	3,F4,A1,1.08
	3,F5,A1,1.51
	3,F6,A1,1.28
	3,F7,A1,1.55
	3,F8,A1,1.03
	3,F9,A1,2.54
	3,F10,A1,1.12
	3,F11,A1,1.14
	3,F12,A1,1.22
	3,G1,A1,1.65
	3,G2,A1,2.27
	3,G3,A1,1.8
	3,G4,A1,1.43
	3,G5,A1,1.71
	3,G6,A1,1.31
	3,G7,A1,1.28
	3,G8,A1,1.22
	3,G9,A1,1.34
	3,G10,A1,1.69
	3,G11,A1,1.96
	3,G12,A1,2.23
	3,H1,A1,2.7
	3,H2,A1,3.47
	3,H3,A1,2.36
	3,H4,A1,2.39
	3,H5,A1,3.83
	3,H6,A1,1.92
	3,H7,A1,6
	3,H8,A1,1.64
	3,H9,A1,2.2
	3,H10,A1,3.99
	4,A1,B3,2.17
	4,A2,B3,3.2
	4,A3,B3,1.93
	4,A4,B3,2.35
	4,A5,B3,2.22
	4,A6,B3,3.59
	4,A7,B3,3.11
	4,A8,B3,2.28
	4,A9,B3,1.78
	4,A10,B3,2.55
	4,A11,B3,2.53
	4,A12,B3,2.58
	4,B1,B3,6.19
	4,B2,B3,6.3
	4,B3,B3,4.36
	4,B4,B3,4.74
	4,B5,B3,4.86
	4,B6,B3,4.41
	4,B7,B3,4.53
	4,B8,B3,5.54
	4,B9,B3,4.79
	4,B10,B3,3.72
	4,B11,B3,5.14
	4,B12,B3,4.51
	4,C1,B3,2.51
	4,C2,B3,1.81
	4,C3,B3,3.13
	4,C4,B3,2
	4,C5,B3,3.69
	4,C6,B3,1.68
	4,C7,B3,2.2
	4,C8,B3,2.14
	4,C9,B3,2.01
	4,C10,B3,3.73
	4,C11,B3,1.65
	4,C12,B3,1.41
	4,D1,B3,1.53
	4,D2,B3,1.9
	4,D3,B3,1.75
	4,D4,B3,1.79
	4,D5,B3,1.85
	4,D6,B3,1.3
	4,D7,B3,1.7
	4,D8,B3,1.5
	4,D9,B3,1.32
	4,D10,B3,2.27
	4,D11,B3,2.07
	4,D12,B3,1.7
	4,E1,B3,1.34
	4,E2,B3,1.68
	4,E3,B3,2.02
	4,E4,B3,1.9
	4,E5,B3,1.78
	4,E6,B3,1.96
	4,E7,B3,2.52
	4,E8,B3,1.59
	4,E9,B3,1.4
	4,E10,B3,1.8
	4,E11,B3,1.8
	4,E12,B3,2.53
	4,F1,B3,1.99
	4,F2,B3,2.72
	4,F4,B3,1.63
	4,F5,B3,1.52
	4,F6,B3,2.35
	4,F7,B3,2.14
	4,F8,B3,1.58
	4,F10,B3,1.6
	4,F11,B3,1.58
	4,F12,B3,2.51
	4,G2,B3,4.62
	4,G3,B3,2.1
	4,G4,B3,1.73
	4,G5,B3,2.33
	4,G6,B3,2.75
	4,G8,B3,1.85
	4,G9,B3,2.91
	4,G10,B3,2.76
	4,G11,B3,1.81
	4,G12,B3,3.68
	4,H2,B3,4.12
	4,H3,B3,5.13
	4,H4,B3,2.83
	4,H5,B3,4.06
	4,H6,B3,7
	4,H7,B3,2.63
	4,H8,B3,3.51
	4,H9,B3,2.31
	4,H10,B3,2.2
	5,A1,C6,2.15
	5,A2,C6,2.22
	5,A3,C6,1.91
	5,A4,C6,2
	5,A5,C6,1.97
	5,A6,C6,3.09
	5,A7,C6,2.79
	5,A8,C6,2.22
	5,A9,C6,1.59
	5,A10,C6,5.26
	5,A11,C6,2.02
	5,B1,C6,6.72
	5,B2,C6,6.63
	5,B4,C6,3.08
	5,B5,C6,6.58
	5,B6,C6,2.8
	5,B8,C6,5.41
	5,B9,C6,3.64
	5,B10,C6,2.46
	5,B11,C6,2.5
	5,B12,C6,2.79
	5,C1,C6,1.71
	5,C2,C6,1.84
	5,C3,C6,2.48
	5,C4,C6,1.58
	5,C5,C6,2.24
	5,C6,C6,1.52
	5,C7,C6,1.82
	5,C8,C6,1.58
	5,C9,C6,1.72
	5,C10,C6,1.99
	5,C11,C6,1.45
	5,C12,C6,1.63
	5,D1,C6,1.59
	5,D2,C6,2.11
	5,D3,C6,2.6
	5,D4,C6,1.96
	5,D5,C6,1.76
	5,D6,C6,1.21
	5,D7,C6,1.51
	5,D8,C6,2.25
	5,D9,C6,1.08
	5,D10,C6,1.67
	5,D11,C6,1.97
	5,D12,C6,1.17
	5,E1,C6,1.52
	5,E2,C6,1.94
	5,E3,C6,1.88
	5,E4,C6,1.66
	5,E5,C6,2.29
	5,E6,C6,1.73
	5,E7,C6,1.79
	5,E8,C6,2.43
	5,E9,C6,1.89
	5,E10,C6,1.91
	5,E11,C6,1.4
	5,E12,C6,1.56
	5,F1,C6,2.01
	5,F2,C6,2.67
	5,F3,C6,1.91
	5,F4,C6,1.69
	5,F5,C6,1.71
	5,F6,C6,2.07
	5,F7,C6,1.7
	5,F8,C6,1.26
	5,F9,C6,1.73
	5,F10,C6,1.34
	5,F11,C6,2.55
	5,F12,C6,1.57
	5,G1,C6,1.89
	5,G2,C6,2.76
	5,G3,C6,1.78
	5,G4,C6,2.06
	5,G5,C6,2.89
	5,G6,C6,1.88
	5,G7,C6,2.48
	5,G8,C6,1.71
	5,G9,C6,2.43
	5,G10,C6,2.34
	5,G11,C6,2.07
	5,G12,C6,2.61
	5,H3,C6,2.77
	5,H4,C6,6.07
	5,H5,C6,2.4
	5,H6,C6,7
	5,H7,C6,3.04
	5,H8,C6,6.69
	5,H9,C6,5.29
	5,H10,C6,3.45
	6,A1,D1,4.26
	6,A2,D1,2.04
	6,A3,D1,4.95
	6,A4,D1,2.52
	6,A5,D1,3.73
	6,A6,D1,3.43
	6,A7,D1,6.65
	6,A8,D1,2.47
	6,A9,D1,1.85
	6,A12,D1,2.64
	6,B1,D1,5.48
	6,B2,D1,5.48
	6,B3,D1,6.92
	6,B4,D1,3
	6,B5,D1,3.04
	6,B11,D1,5.24
	6,C1,D1,2.48
	6,C2,D1,1.87
	6,C3,D1,5.15
	6,C4,D1,2.32
	6,C5,D1,3.06
	6,C6,D1,1.45
	6,C7,D1,2.51
	6,C8,D1,2.95
	6,C9,D1,2.3
	6,C10,D1,2.63
	6,C11,D1,2.62
	6,C12,D1,3.36
	6,D1,D1,2.24
	6,D2,D1,3.04
	6,D3,D1,2.45
	6,D4,D1,2.29
	6,D5,D1,2.65
	6,D6,D1,1.27
	6,D7,D1,2.31
	6,D8,D1,2.11
	6,D9,D1,1.47
	6,D10,D1,2.08
	6,D11,D1,2.93
	6,D12,D1,1.77
	6,E1,D1,1.91
	6,E2,D1,1.85
	6,E3,D1,2.03
	6,E4,D1,2.17
	6,E5,D1,2.51
	6,E6,D1,2.83
	6,E7,D1,2.63
	6,E8,D1,1.97
	6,E9,D1,1.61
	6,E10,D1,1.89
	6,E11,D1,1.63
	6,E12,D1,2.28
	6,F1,D1,2.51
	6,F5,D1,2.37
	6,F6,D1,2.1
	6,F8,D1,1.68
	6,F12,D1,1.93
	6,G1,D1,1.83
	6,G2,D1,1.76
	6,G3,D1,2.37
	6,G4,D1,1.51
	6,G5,D1,2.29
	6,G6,D1,1.7
	6,G7,D1,3.25
	6,G8,D1,2.54
	6,G9,D1,1.49
	6,G10,D1,2.17
	6,G11,D1,1.77
	6,G12,D1,2.62
	6,H2,D1,2.75
	6,H3,D1,7
	6,H4,D1,2.63
	6,H6,D1,2.29
	6,H7,D1,3.29
	6,H8,D1,2.73
	6,H9,D1,3.12
	6,H10,D1,2.09
	7,A1,D3,2.38
	7,A2,D3,3.54
	7,A3,D3,2.35
	7,A4,D3,2.81
	7,A5,D3,3.01
	7,A6,D3,2.43
	7,A7,D3,3.39
	7,A8,D3,2.27
	7,A9,D3,7
	7,A10,D3,6.34
	7,A11,D3,6.17
	7,A12,D3,5.46
	7,B1,D3,4.72
	7,B2,D3,3.64
	7,B3,D3,3.11
	7,B4,D3,4.19
	7,B5,D3,3.93
	7,B6,D3,3.69
	7,B7,D3,3.29
	7,B8,D3,3.84
	7,B9,D3,2.96
	7,B10,D3,2.92
	7,B11,D3,3.1
	7,B12,D3,2.63
	7,C1,D3,2.14
	7,C2,D3,2.75
	7,C3,D3,3.48
	7,C4,D3,2.65
	7,C5,D3,2.26
	7,C6,D3,1.66
	7,C7,D3,2.2
	7,C8,D3,2.1
	7,C9,D3,2.22
	7,C10,D3,2.91
	7,C11,D3,2.18
	7,C12,D3,2.06
	7,D1,D3,2.13
	7,D2,D3,2.22
	7,D3,D3,2.49
	7,D4,D3,1.98
	7,D5,D3,2.08
	7,D6,D3,1.89
	7,D7,D3,2.1
	7,D8,D3,1.98
	7,D9,D3,1.86
	7,D10,D3,1.97
	7,D11,D3,3.3
	7,D12,D3,1.97
	7,E1,D3,2.2
	7,E2,D3,2.96
	7,E3,D3,2.09
	7,E4,D3,2.16
	7,E5,D3,2.21
	7,E6,D3,2.61
	7,E7,D3,2.23
	7,E8,D3,2.65
	7,E9,D3,1.91
	7,E10,D3,1.91
	7,E11,D3,1.83
	7,E12,D3,2.07
	7,F1,D3,2.3
	7,F2,D3,2.44
	7,F3,D3,2.4
	7,F4,D3,2.26
	7,F5,D3,2.02
	7,F6,D3,3.38
	7,F7,D3,3.51
	7,F8,D3,2.24
	7,F9,D3,2.32
	7,F10,D3,2.06
	7,F11,D3,1.99
	7,F12,D3,2.66
	7,G1,D3,4.14
	7,G2,D3,3.42
	7,G3,D3,2.21
	7,G4,D3,2.17
	7,G5,D3,3.13
	7,G6,D3,5.23
	7,G7,D3,5.59
	7,G8,D3,1.93
	7,G9,D3,2.09
	7,G10,D3,3.54
	7,G11,D3,2.44
	7,H1,D3,5.81
	7,H2,D3,3.01
	7,H3,D3,2.73
	7,H4,D3,2.94
	7,H5,D3,2.52
	7,H6,D3,2.33
	7,H7,D3,2.28
	7,H8,D3,2.53
	7,H9,D3,2.27
	7,H10,D3,2.23
    '''

    ########## DO NOT EDIT BELOW THIS LINE ##########

    # turn on lights if not on already
    protocol.set_rail_lights(True)

    # Define hardware, pipettes/tips, plates
    # load tips
    tips20 = [protocol.load_labware(
            'opentrons_96_tiprack_20ul', str(slot)) for slot in [
            2]]

    # specify pipette, mount location, and tips
    p20 = protocol.load_instrument("p20_single_gen2", mount=pipette_mount_20, tip_racks=tips20)

    # load reagent labware and specify reagents in each well/columns
    if tube_type == '1.5ml':
        tube_rack = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', 1)
    elif tube_type == '2ml':
        tube_rack = protocol.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', 1)
    else:
        raise Exception('Must specify tube type (1.5ml or 2ml tube)')


    # load plates
    slot_range = list(range(3, 3 + num_plates))
    [protocol.load_labware('vwr_96_wellplate_200ul_greenplate', str(slot)) for slot in slot_range]

    # parse input data
    csv_data = [[val.strip() for val in line.split(',')]
                for line in input_data.splitlines()
                if line.split(',')[0].strip()][1:]

    # set aspirate and dispense speeds
    p20.flow_rate.aspirate = 150
    p20.flow_rate.dispense = 150


    p20.pick_up_tip()
    # set starting tube
    current_tube = 'A1'
    # add dna to tube
    for row in csv_data:
        source_well = protocol.loaded_labwares[int(row[0])].wells_by_name()[row[1]]
        dest_tube = tube_rack.wells_by_name()[row[2]]
        vol_dna = float(row[3])
        vol_dna = round(vol_dna, 2)
        # if the new destination tube isnt the same as what the previous run, change tips
        if row[2] != current_tube:
            p20.drop_tip()
            p20.pick_up_tip()
        # check volume
        if vol_dna < 1.0 or vol_dna > 20.0:
            raise Exception("Invalid volume of dna. Must be between 1.0-20.0")
        p20.aspirate(vol_dna, source_well)
        p20.touch_tip()
        p20.dispense(vol_dna, dest_tube.bottom())
        p20.move_to(dest_tube.top())
        p20.blow_out()
        p20.touch_tip()
        # update current tube to compare on next round
        current_tube = row[2]

    p20.drop_tip()

    ### make sure the tube checking thing works ###

    # turn off lights
    protocol.set_rail_lights(False)
