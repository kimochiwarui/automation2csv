def replaceValues(arg, argValue):
    switcher = {
        'DriveType': {
            'DriveType_TransRWD_Name': 'RWD',
            'DriveType_TransFWD_Name': 'FWD',
            'DriveType_LongRWD_Name': 'RWD',
            'DriveType_Long4X4_Name': '4x4',
            'DriveType_Long4WD_Name': 'AWD'
        },
        'GearboxType': {
            'GearboxType_Manual_Name': 'Manual',
            'GearboxType_AutoAdv_Name': 'Adv. Automatic',
            'GearboxType_Sequential_Name': 'Robotic',
            'GearboxType_SequentialDblClutch_Name': 'DCT'
        },
        'GearboxRatios': {
            'GearRatio_1_Name': '1 Speed',
            'GearRatio_2_Name': '2 Speed',
            'GearRatio_3_Name': '3 Speed',
            'GearRatio_4_Name': '4 Speed',
            'GearRatio_5_Name': '5 Speed',
            'GearRatio_6_Name': '6 Speed',
            'GearRatio_7_Name': '7 Speed',
            'GearRatio_8_Name': '8 Speed',
            'GearRatio_9_Name': '9 Speed',
        },
        'Differential': {
            'Diff_Standard_Name': 'Open Diff',
            #  
            'Diff_Locker_Name': 'Auto locked',
            'Diff_GearedLSD_Name': 'Geared Diff',
            'Diff_ViscLSD_Name': 'Viscous DIff',
            'Diff_ElecLSD_Name': 'El'
        },
        # 'PowerDistribution': {} to do,
        'TyreType': {
            # 
            'TyreType_Radial_Name': 'Radial tyres',
        },
        'Tyres': {
            # offroad tyres
            'TyreType_LongHardRoad_Name': 'Hard tyres',
            'TyreType_MedComp_Name': 'Medium tyres',
            'TyreType_SportComp_Name': 'Sport tyres',
            'TyreType_SemiSlick_Name': 'Semi Slick tyres'
        },
        'RimMaterial': {
            'RimMaterial_Steel_Name': 'Steel',
            'RimMaterial_Mag_Name': 'Magnesium',
            'RimMaterial_Alloy_Name': 'Alloy'
            # CF
        },
        'FrontBrakeType': {
            # drum
            # drum x2
            'BrakeDisc_Solid_Name': 'Solid front disc brakes',
            'BrakeDisc_Vented_Name': 'Vented front disc brakes',
            # CF
        },
        'FrontBrakeOptions': {
            'BrakeCaliper_1Piston_Name': 'Single Piston',
            'BrakeCaliper_2Piston_Name': 'Dual Piston',
            'BrakeCaliper_3Piston_Name': 'Triple Piston',
            'BrakeCaliper_4Piston_Name': 'Four Piston',
            'BrakeCaliper_6Piston_Name': 'Six Piston',
        },
        'RearBrakeType': {
            'Brake_Drum_Name': 'Drums',
            'BrakeDisc_Solid_Name': 'Solid Disc Brakes',
            'BrakeDisc_Vented_Name': 'Vented Disc Brakes'
        },
        'RearBrakeOptions': {
            'BrakeCaliper_1Piston_Name': 'Single Piston',
            'BrakeCaliper_2Piston_Name': 'Dual Piston',
            'BrakeCaliper_3Piston_Name': 'Triple Piston',
            'BrakeCaliper_4Piston_Name': 'Four Piston',
            'BrakeCaliper_6Piston_Name': 'Six Piston',
        },
        'Undertray': {
            'Undertray_None_Name': 'None',
            'Undertray_Offroad_Name': 'Offroad',
            'Undertray_SemiClad_Name': 'Semi Clad',
            'Undertray_FullyClad_Name': 'Fully Clad',
            # Downforce
        },
        'FrontRowSeats': {
            'SeatOption_2_ShortName': '2 Full Front Seats',
            # ???
        },
        'SecondRowSeats': {
            'SeatOption_None_ShortName': 'No rear seats',
            'SeatOption_2Small_ShortName': '2 Small Rear seats',
            'SeatOption_3_ShortName': '3 Full Rear Seats',
            # ???
        },
        'Interior': {
            #  ????
            'Interior_SuperLight_Name': 'Basic Interior',
            'Interior_Standard_Name': 'Standart Interior',
            'Interior_Premium_Name': 'Premium Interior',
            'Interior_Luxury_Name': 'Luxury Interior',
            'Interior_HandMade_Name': 'Hand Made Interior',
        },
        'Entertainment': {
            'Entertain_None_Name': 'None',
            # 
            'Entertain_Basic_8Track_Name': 'Basic 8 Track',
            # 
            'Entertain_Basic_Cassette_Name': 'Basic Cassette Player',
            'Entertain_Premium_Cassette_Name': 'Premium Cassete Player',
            # 
            'Entertain_Premium_CD_Name': 'Premium CD Player',
            # 
            'Entertain_Basic_Infotainment_Name': 'Basic Infotainment',
            'Entertain_Standard_Infotainment_Name': 'Standart Infotainment',
            # 
            'Entertain_Luxury_HUD_Name': 'Luxury HUD'
        },
        'PowerSteering': {
            'DriveAssist_PowerSteer_None_Name': 'None',
            'DriveAssist_PowerSteer_Name': 'Hydralic',
            'DriveAssist_PowerSteer_Variable_Name': 'Variable Hydralic',
            'DriveAssist_PowerSteer_Electric_Name': 'Elictric',
            'DriveAssist_PowerSteer_Electric_Variable_Name': 'Variable Electric',
        },
        'DriveAssist': {
            'DriveAssist_None_Name': 'None',
            'DriveAssist_TractionPackage1_Name': 'ABS',
            'DriveAssist_TractionPackage2_Name': 'TC+ABS',
            'DriveAssist_TractionPackage3_Name': 'ESC',
            'DriveAssist_TractionPackage4_Name': 'ESC+LC',
        },
        'Safety': {
            'Safety_Standard_60s_Name': 'Standart 60s',
            # 
            'Safety_Advanced_70s_Name': 'Advanced 70s',
            # 
            'Safety_Standard_80s_Name': 'Standary 80s',
            # 
            'Safety_Basic_90s_Name': 'Basic 90s',
            # 
            'Safety_Basic_00s_Name': 'Basic 00',
            'Safety_Standard_00s_Name': 'Standart 00s',
            # 
            'Safety_Basic_10s_Name': 'Basic 10s',
            # 
            'Safety_Advanced_20s_Name': 'Advanced 20s'
        },
        'Springs': {
            'Springs_Passive_Name': 'Standart',
            'Springs_Progressive_Name': 'Progressive',
            'Springs_Air_Name': 'Air',

        },
        'Dampers': {
            'Dampers_Passive_Name': 'Twin-tube Dampers',
            'Dampers_Advanced_Name': 'Gas Monotube'
        },
        'SwayBars': {
            'SwayBars_Passive_Name': 'Standart',
            'SwayBars_Offroad_Name': 'Offroad',
            'SwayBars_SemiActive_Name': 'Semi Active'
        },
        # 
        # MODEL
        # 
        'Chassis': {
            'Chassis_Ladder_Name': 'Ladder',
            'Chassis_SpaceFrame_Name': 'Spaceframe',
            'Chassis_Monocoque_Name': 'Monocoque',
            'Chassis_SemiSpaceFrame_Name': 'Semispaceframe',
            'Chassis_LightTruckMonocoque_Name': 'Light Truck Monocoque'
        },
        'ChassisMaterial': {
            'ChassisMat_Steel_Name': 'Steel',
            'ChassisMat_GalvanizedSteel_Name': 'Galvanized Steel',
            'ChassisMat_AHSSteel_Name': 'AHS Steel',
            'ChassisMat_Alu_Name': 'Aluminium',
            'ChassisMat_AHSLight_Name': 'Light AHS Steel'
        },
        'EnginePlacement': {
            'EngPlace_FrTransverse_Name': 'Front Transverse',
            'EngPlace_FrLong_Name': 'Front Longitudunal',
            'EngPlace_MidTransverse_Name': 'Mid Transverse',
            # 
        },
        'FrontSuspension': {
            'Suspend_SolAxCoil_Name': 'Solid Axel Coil',
            'Suspend_MacPher_Name': 'Macpherson',
            'Suspend_DblWishbone_Name': 'Double Wishbone',
        },
        'RearSuspension': {
            'Suspend_SolAxCoil_Name': 'Solid Axel Coil',
            'Suspend_MacPher_Name': 'Macpherson',
            'Suspend_SemiTrailArm_Name': 'Semitrailing Arm',
            'Suspend_Torsion_Name': 'Torsion Beam',
            'Suspend_Multilink_Name': 'Multilink',
        },
        'PanelMaterial': {
            'PanelMat_Steel_Name': 'Steel',
            'PanelMat_TreatedSteel_Name': 'Treated Steel',
            'PanelMat_Alu_Name': 'Aluminium',
            'PanelMat_PartialAlu_Name': 'Partially Aluminium',
            'PanelMat_CRSteel_Name': 'Corrosion Resistant Steel',
        },
        # 
        #  Variant
        #
        'Crank': {
            'CrankMat_Iron_Name': 'Cast',
            'CrankMat_Forged_Name': 'Forged',
            'CrankMat_IronFP_Name': 'Cast Flatplane',
            'CrankMat_ForgedFP_Name': 'Forged Flatplane',
            'CrankMat_Billet_Name': 'Billet',
        },
        'Conrods': {
            'RodMat_Cast_Name': 'Cast',
        },
        'Pistons': {
            'Piston_Cast_Name': 'Cast',
            'Piston_Forged_Name': 'Forged',
            'Piston_LightForged_Name': 'Ligweight Forged',
            'Piston_LowFCast_Name': 'Low Friction Cast',
            'Piston_HypCast_Name': 'Hypereutic Cast',
        },
        'VVT': {
            'VarValves_None_Name': 'None',
            'VarValves_VVTSOHC_Name': 'Variable Cams',
            'VarValves_VVTDOHC_Name': 'Double Variable Cams'
        },
        'Aspiration': {
            'Aspiration_Natural_Name': 'Naturally Aspirated',
            'Turbo_Single_Name': 'Single Turbo',
            'Turbo_Twin_Name': 'Twin Turbo',
        },
        'FuelSystemType': {
            'FuelSys_Carb_Name': 'Carbulators',
            'FuelSys_Inj_Name': 'Injection',
        },
        'FuelSystem': {
            'FuelSys_Carb_2Barrel_Name': '2 Barrel',
            'FuelSys_Carb_4Barrel_Name': '4 Barrel',
            'FuelSys_Carb_DCOE_Name': 'DCOE',
            'FuelSys_Inj_MultiEFI_Name': 'Multipoint Fuel Injection',
            'FuelSys_Inj_Direct_Name': 'Direct Injection'
        },
        'IntakeManifold': {
            'FuelSys_CarbIntake_Single_Name': 'Single Carb',
            'FuelSys_InjIntake_Single_Name': 'Single Injection',
            'FuelSys_InjIntake_PerCyl_Name': 'Per Cylinder Injection',
        },
        'Intake': {
            'FuelSys_CarbFilter_Standard_Name': 'Standart',
            'FuelSys_CarbFilter_Race_Name': 'Race Intake',
            'FuelSys_InjFilter_Standard_Name': 'Standart',
            'FuelSys_InjFilter_Perform_Name': 'Pefromance',
        },
        'Headers': {
            'Header_ShortCast_Name': 'Short Cast',
            'Header_Tube_Name': 'Tubular',
            'Header_LongTube_Name': 'Long Tubular',
        },
        'ExhaustCount': {
            'Exhausts_1_Name': 'Single pipe',
            'Exhausts_2_Name': 'Dual Pipe'
        }
    }
    if arg in switcher:
        return switcher.get(arg).get(argValue, argValue)
    return argValue