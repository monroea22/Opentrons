# 1-5 plates worth of primers (half skirt inserted into alumininum block or green skirt plate)
# into 1.5 ml or 2 ml tube

metadata = {
    'protocolName': 'primer_mix_LcaP1 ',
    'author': 'AAM, last updated 3/24/23',
    'description': 'Pool GT seq primers (variable volumes) into one tube.',
    'apiLevel': '2.11'
}

def run(protocol):
    ########## EDIT THESE RUN OPTIONS AS NEEDED ##########

    # location of p20 single channel ('left' or 'right', all lowercase and in single quotes)
    pipette_mount_20 = 'right'

    # type of tube samples will be pooled into ('1.5ml' or '2ml')
    tube_type = '1.5ml'

    # number of plates (integar, max 9)
    num_plates = 4

    # sample volume info
    # paste data from csv here (in between '''  ''')
    input_data = '''
    source_slot,source_well,tube_well,vol_dna
	6,A1,A1,2
	6,A2,A1,1
	6,A3,A1,2
	6,A4,A1,2
	6,A5,A1,2
	6,A6,A1,4
	6,A7,A1,1
	6,A8,A1,2
	6,A9,A1,2
	6,A10,A1,4
	6,A11,A1,2
	6,A12,A1,2
	6,B1,A1,4
	6,B3,A1,2
	6,B4,A1,2
	6,B5,A1,1
	6,B7,A1,2
	6,B8,A1,2
	6,B9,A1,2
	6,B10,A1,2
	6,B12,A1,2
	6,C1,A1,2
	6,C2,A1,2
	6,C3,A1,4
	6,C4,A1,2
	6,C5,A1,2
	6,C6,A1,2
	6,C7,A1,2
	6,C8,A1,2
	6,C9,A1,2
	6,C10,A1,2
	6,C11,A1,1
	6,C12,A1,2
	6,D1,A1,1
	6,D2,A1,2
	6,D3,A1,1
	6,D4,A1,2
	6,D5,A1,2
	6,D6,A1,2
	6,D7,A1,2
	6,D8,A1,2
	6,D9,A1,2
	6,D10,A1,1
	6,D11,A1,1
	6,D12,A1,2
	6,E1,A1,2
	6,E2,A1,2
	6,E3,A1,1
	6,E4,A1,2
	6,E5,A1,2
	6,E6,A1,2
	6,E7,A1,4
	6,E8,A1,4
	6,E9,A1,2
	6,E10,A1,2
	6,E11,A1,2
	6,E12,A1,2
	6,F1,A1,4
	6,F2,A1,2
	6,F3,A1,4
	6,F4,A1,1
	6,F5,A1,1
	6,F6,A1,2
	6,F7,A1,2
	6,F8,A1,2
	6,F9,A1,4
	6,F10,A1,2
	6,F11,A1,1
	6,F12,A1,2
	6,G1,A1,1
	6,G2,A1,4
	6,G3,A1,2
	6,G4,A1,2
	6,G5,A1,1
	6,G6,A1,1
	6,G8,A1,2
	6,G9,A1,1
	6,G10,A1,2
	6,G11,A1,1
	6,H1,A1,2
	6,H2,A1,4
	6,H3,A1,4
	6,H4,A1,4
	6,H5,A1,2
	6,H6,A1,2
	6,H7,A1,2
	6,H8,A1,2
	6,H9,A1,2
	6,H10,A1,4
	6,H11,A1,4
	6,H12,A1,1
	7,A1,A1,1
	7,A2,A1,1
	7,A3,A1,1
	7,A4,A1,1
	7,A5,A1,4
	7,A6,A1,1
	7,A7,A1,2
	7,A8,A1,2
	7,A9,A1,2
	7,A10,A1,2
	7,A11,A1,2
	7,A12,A1,2
	7,B1,A1,2
	7,B2,A1,4
	7,B3,A1,4
	7,B4,A1,4
	7,B5,A1,4
	7,B6,A1,4
	7,B7,A1,2
	7,B8,A1,2
	7,B9,A1,4
	7,B10,A1,4
	7,B11,A1,4
	7,B12,A1,2
	7,C1,A1,2
	7,C2,A1,2
	7,C3,A1,2
	7,C4,A1,2
	7,C5,A1,2
	7,C6,A1,2
	7,C8,A1,4
	7,C9,A1,1
	7,C10,A1,2
	7,C11,A1,1
	7,C12,A1,1
	7,D1,A1,2
	7,D2,A1,2
	7,D3,A1,1
	7,D4,A1,2
	7,D5,A1,2
	7,D6,A1,1
	7,D7,A1,2
	7,D8,A1,1
	7,D9,A1,1
	7,D10,A1,2
	7,D11,A1,2
	7,D12,A1,1
	7,E1,A1,4
	7,E2,A1,2
	7,E3,A1,2
	7,E4,A1,2
	7,E5,A1,1
	7,E6,A1,2
	7,E7,A1,4
	7,E8,A1,4
	7,E10,A1,2
	7,E11,A1,2
	7,E12,A1,4
	7,F1,A1,1
	7,F2,A1,1
	7,F3,A1,2
	7,F5,A1,1
	7,F6,A1,2
	7,F7,A1,2
	7,F8,A1,4
	7,F9,A1,1
	7,F10,A1,1
	7,F11,A1,2
	7,F12,A1,2
	7,G2,A1,1
	7,G4,A1,4
	7,G5,A1,2
	7,G7,A1,1
	7,G8,A1,1
	7,G9,A1,1
	7,G11,A1,4
	7,G12,A1,4
	7,H1,A1,4
	7,H2,A1,4
	7,H3,A1,4
	7,H4,A1,4
	7,H5,A1,4
	7,H6,A1,2
	7,H7,A1,4
	7,H8,A1,4
	7,H9,A1,2
	7,H10,A1,4
	7,H11,A1,4
	7,H12,A1,4
	8,A1,A1,4
	8,A2,A1,1
	8,A3,A1,2
	8,A4,A1,1
	8,A5,A1,1
	8,A6,A1,2
	8,A7,A1,2
	8,A8,A1,1
	8,A9,A1,1
	8,A10,A1,1
	8,A11,A1,1
	8,A12,A1,4
	8,B1,A1,1
	8,B2,A1,1
	8,B3,A1,4
	8,B5,A1,4
	8,B6,A1,2
	8,B7,A1,2
	8,B8,A1,2
	8,B9,A1,2
	8,B11,A1,2
	8,B12,A1,1
	8,C1,A1,2
	8,C3,A1,2
	8,C4,A1,2
	8,C5,A1,1
	8,C6,A1,4
	8,C7,A1,1
	8,C8,A1,2
	8,C9,A1,1
	8,C10,A1,1
	8,C11,A1,2
	8,C12,A1,2
	8,D1,A1,1
	8,D2,A1,1
	8,D3,A1,4
	8,D5,A1,2
	8,D6,A1,2
	8,D7,A1,2
	8,D10,A1,1
	8,D11,A1,2
	8,D12,A1,1
	8,E1,A1,1
	8,E2,A1,2
	8,E3,A1,1
	8,E4,A1,2
	8,E5,A1,2
	8,E6,A1,1
	8,E7,A1,1
	8,E9,A1,2
	8,E10,A1,2
	8,E11,A1,2
	8,E12,A1,1
	8,F1,A1,2
	8,F2,A1,1
	8,F3,A1,1
	8,F4,A1,1
	8,F5,A1,2
	8,F6,A1,1
	8,F7,A1,1
	8,F8,A1,2
	8,F9,A1,2
	8,F11,A1,1
	8,F12,A1,4
	8,G1,A1,1
	8,G2,A1,1
	8,G3,A1,1
	8,G4,A1,2
	8,G5,A1,2
	8,G8,A1,1
	8,G9,A1,1
	8,G10,A1,1
	8,G11,A1,2
	8,G12,A1,1
	8,H1,A1,1
	8,H2,A1,1
	8,H3,A1,4
	8,H4,A1,1
	8,H5,A1,2
	8,H6,A1,4
	8,H7,A1,2
	8,H8,A1,2
	8,H9,A1,2
	8,H10,A1,2
	8,H11,A1,1
	8,H12,A1,2
	9,A1,A1,1
	9,A2,A1,2
	9,A3,A1,2
	9,A4,A1,1
	9,A5,A1,1
	9,A6,A1,1
	9,A7,A1,1
	9,A8,A1,2
	9,A9,A1,2
	9,A10,A1,1
	9,A11,A1,1
	9,A12,A1,1
	9,B1,A1,1
	9,B3,A1,1
	9,B4,A1,2
	9,B5,A1,4
	9,B6,A1,1
	9,B7,A1,2
	9,B8,A1,2
	9,B9,A1,1
	9,B11,A1,2
	9,B12,A1,2
	9,C1,A1,1
	9,C2,A1,1
	9,C3,A1,1
	9,C4,A1,2
	9,C5,A1,1
	9,C6,A1,1
	9,C7,A1,2
	9,C8,A1,2
	9,C9,A1,2
	9,C10,A1,2
	9,C11,A1,2
	9,C12,A1,1
	9,D1,A1,1
	9,D2,A1,1
	9,D3,A1,1
	9,D4,A1,1
	9,D5,A1,2
	9,D6,A1,2
	9,D7,A1,2
	9,D8,A1,1
	9,D9,A1,1
	9,D10,A1,1
	9,D11,A1,1
	9,D12,A1,1
	9,E1,A1,2
	9,E2,A1,1
	9,E3,A1,1
	9,E4,A1,1
	9,E5,A1,1
	9,E6,A1,2
	9,E7,A1,1
    '''

    ########## DO NOT EDIT BELOW THIS LINE ##########

    # turn on lights if not on already
    protocol.set_rail_lights(True)

    # Define hardware, pipettes/tips, plates
    # load tips
    tips20 = [protocol.load_labware(
            'opentrons_96_tiprack_20ul', str(slot)) for slot in [
            2, 3, 4, 5]]

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
    slot_range = list(range(6, 6 + num_plates))
    [protocol.load_labware('vwr_96_wellplate_200ul_greenplate', str(slot)) for slot in slot_range]

    # parse input data
    csv_data = [[val.strip() for val in line.split(',')]
                for line in input_data.splitlines()
                if line.split(',')[0].strip()][1:]

    # set aspirate and dispense speeds
    p20.flow_rate.aspirate = 150
    p20.flow_rate.dispense = 150


    # set starting tube
    current_tube = 'A1'
    # add primer to tube
    for row in csv_data:
        source_well = protocol.loaded_labwares[int(row[0])].wells_by_name()[row[1]]
        dest_tube = tube_rack.wells_by_name()[row[2]]
        vol_dna = float(row[3])
        # check volume
        if vol_dna < 1.0 or vol_dna > 20.0:
            raise Exception("Invalid volume of dna. Must be between 1.0-20.0")
        # round to 2 decimal places
        vol_dna = round(vol_dna, 2)
        # use p20 if appropriate volume
        if 0 < vol_dna <= 20:
            p20.pick_up_tip()
            p20.aspirate(vol_dna, source_well)
            p20.touch_tip()
            p20.dispense(vol_dna, dest_tube.bottom())
            p20.blow_out()
            p20.touch_tip()
            p20.drop_tip()

    # turn off lights
    protocol.set_rail_lights(False)


