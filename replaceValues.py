def replaceValues(arg, argValue):
    switcher = {
        'BodyType': {
            'EBodyType::EBT_COUPE': 'Coupe',
            'EBodyType::EBT_HATCHBACK': 'Hatchback',
            'EBodyType::EBT_CONVERTIBLE': 'Convertable',
            'EBodyType::EBT_VAN': 'Van',
            'EBodyType::EBT_PEOPLEMOVER': 'MPV',
            'EBodyType::EBT_TRUCK': 'Truck',
            'EBodyType::EBT_SUV': 'SUV',
            'EBodyType::EBT_WAGON': 'Wagon',
            'EBodyType::EBT_SEDAN': 'Sedan',
        },
        'DriveType': {
            'DriveType_TransRWD_Name': 'RWD',
            'DriveType_TransFWD_Name': 'FWD',
            'DriveType_LongRWD_Name': 'RWD',
            'DriveType_Long4X4_Name': '4x4',
            'DriveType_Long4WD_Name': 'AWD'
        },
        'GearboxType': {
            'GearboxType_Manual_Name': 'Manual',
            'GearboxType_Auto_Name': 'Automatic',
            'GearboxType_AutoAdv_Name': 'Adv. Automatic',
            'GearboxType_Sequential_Name': 'Sequential',
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
            'Diff_Locker_Name': 'Manual Locker',
            'Diff_AutoLocker_Name': 'Automatic Locker',
            'Diff_GearedLSD_Name': 'Geared LSD',
            'Diff_ViscLSD_Name': 'Viscous LSD',
            'Diff_ElecLSD_Name': 'Electric LSD'
        },
        'TyreType': {
            'TyreType_CrossPly_Name': 'Cross Ply',
            'TyreType_Radial_Name': 'Radial Tyres',
        },
        'Tyres': {
            'TyreType_SemiOffRoad_Name': 'Chunky Offroad',
            'TyreType_LongHardRoad_Name': 'Hard Compound',
            'TyreType_MedComp_Name': 'Medium Compound',
            'TyreType_SportComp_Name': 'Sport Compound',
            'TyreType_SemiSlick_Name': 'Semi Slick'
        },
        'RimMaterial': {
            'RimMaterial_Steel_Name': 'Steel',
            'RimMaterial_Mag_Name': 'Magnesium',
            'RimMaterial_Alloy_Name': 'Alloy',
            'RimMaterial_CF_Name': 'Carbon Fiber',
        },
        'FrontBrakeType': {
            'Brake_Drum_Name': 'Drum (SLS)',
            'Brake_TwinLeadingDrum_Name': 'Drum (2LS)',
            'BrakeDisc_Solid_Name': 'Solid Disc',
            'BrakeDisc_Vented_Name': 'Vented Disc',
            'BrakeDisc_CarCeramic_Name': 'Carbon Ceramic'
        },
        'FrontBrakeOptions': {
            'Brake_DrumOption_Name': 'Drums',
            'BrakeCaliper_1Piston_Name': '1 Piston',
            'BrakeCaliper_2Piston_Name': '2 Piston',
            'BrakeCaliper_3Piston_Name': '3 Piston',
            'BrakeCaliper_4Piston_Name': '4 Piston',
            'BrakeCaliper_6Piston_Name': '6 Piston',
        },
        'RearBrakeType': {
            'Brake_Drum_Name': 'Drums',
            'BrakeDisc_Solid_Name': 'Solid Disc Brakes',
            'BrakeDisc_Vented_Name': 'Vented Disc Brakes',
            'BrakeDisc_CarCeramic_Name': 'Carbon Ceramic'
        },
        'RearBrakeOptions': {
            'Brake_DrumOption_Name': 'Drums',
            'BrakeCaliper_1Piston_Name': '1 Piston',
            'BrakeCaliper_2Piston_Name': '2 Piston',
            'BrakeCaliper_3Piston_Name': '3 Piston',
            'BrakeCaliper_4Piston_Name': '4 Piston',
            'BrakeCaliper_6Piston_Name': '6 Piston',
        },
        'Undertray': {
            'Undertray_None_Name': 'None',
            'Undertray_Offroad_Name': 'Offroad',
            'Undertray_SemiClad_Name': 'Semi Clad',
            'Undertray_FullyClad_Name': 'Fully Clad',
            'Undertray_Downforce_Name': 'Downforce'
        },
        'ActiveWing': {
            'ActiveAero_None_Name': 'None',
            'ActiveAero_Wing_Name': 'Active Wing'
        },
        'ActiveCooling': {
            'ActiveAero_None_Name': 'None',
            'ActiveAero_Cooling_Name': 'Cooling Flaps'
        },
        'Interior': {
            'Interior_Basic_Name': 'Basic Interior',
            'Interior_Standard_Name': 'Standart Interior',
            'Interior_Premium_Name': 'Premium Interior',
            'Interior_SuperLight_Name': 'Sport Interior',
            'Interior_Luxury_Name': 'Luxury Interior',
            'Interior_HandMade_Name': 'Hand Made Interior',
        },
        'Entertainment': {
            'Entertain_None_Name': 'None',
            #
            'Entertain_Basic_AM_Name': 'Basic AM Radio',
            'Entertain_Standard_AM_Name': 'Standart AM Radio',
            'Entertain_Premium_AM_Name': 'Premium AM Radio',
            'Entertain_Luxury_AM_Name': 'Luxury AM Radio',
            'Entertain_Phonograph_Name': 'Phonograph',
            # 
            'Entertain_Basic_8Track_Name': 'Basic 8 Track',
            'Entertain_Standard_8Track_Name': 'Standart 8 Track',
            'Entertain_Premium_8Track_Name': 'Premium 8 Track',
            'Entertain_Luxury_8Track_Name': 'Luxury 8 Track',
            # 
            'Entertain_Basic_Cassette_Name': 'Basic Cassette Player',
            'Entertain_Standard_Cassette_Name': 'Standart Cassette Player',
            'Entertain_Premium_Cassette_Name': 'Premium Cassete Player',
            'Entertain_Luxury_Cassette_Name': 'Luxury Cassete Player',
            # 
            'Entertain_Basic_CD_Name': 'Basic CD Player',
            'Entertain_Standard_CD_Name': 'Standart CD Player',
            'Entertain_Premium_CD_Name': 'Premium CD Player',
            'Entertain_Luxury_CD_Name': 'Luxury CD Player',
            # 
            'Entertain_Basic_Infotainment_Name': 'Basic Infotainment',
            'Entertain_Standard_Infotainment_Name': 'Standart Infotainment',
            'Entertain_Premium_Infotainment_Name': 'Premium Infotainment',
            'Entertain_Luxury_Infotainment_Name': 'Luxury Infotainment',
            # 
            'Entertain_Basic_HUD_Name': 'Basic HUD',
            'Entertain_Standard_HUD_Name': 'Standart HUD',
            'Entertain_Premium_HUD_Name': 'Premium HUD',
            'Entertain_Luxury_HUD_Name': 'Luxury HUD',
        },
        'PowerSteering': {
            'DriveAssist_PowerSteer_None_Name': 'None',
            'DriveAssist_PowerSteer_Name': 'Hydralic',
            'DriveAssist_PowerSteer_Variable_Name': 'Variable Hydralic',
            'DriveAssist_PowerSteer_Electric_Name': 'Electric',
            'DriveAssist_PowerSteer_Electric_Variable_Name': 'Variable Electric',
        },
        'Assist': {
            'DriveAssist_None_Name': 'None',
            'DriveAssist_TractionPackage1_Name': 'ABS',
            'DriveAssist_TractionPackage2_Name': 'TC+ABS',
            'DriveAssist_TractionPackage3_Name': 'ESC',
            'DriveAssist_TractionPackage4_Name': 'ESC+LC',
        },
        'Safety': {
            'Safety_None_Name': 'None',
            'Safety_Basic_40s_Name': 'Basic 40s',
            'Safety_Standard_40s_Name': 'Standart 40s',
            'Safety_Advanced_40s_Name': 'Advanced 40s',
            'Safety_Basic_50s_Name': 'Basic 50s',
            'Safety_Standard_50s_Name': 'Standart 50s',
            'Safety_Advanced_50s_Name': 'Advanced 50s',
            
            'Safety_Basic_60s_Name': 'Basic 60s',
            'Safety_Standard_60s_Name': 'Standart 60s',
            'Safety_Advanced_60s_Name': 'Advanced 60s',
            
            'Safety_Basic_70s_Name': 'Basic 70s',
            'Safety_Standard_70s_Name': 'Standart 70s',
            'Safety_Advanced_70s_Name': 'Advanced 70s',
            
            'Safety_Basic_80s_Name': 'Standart 80s',
            'Safety_Standard_80s_Name': 'Standart 80s',
            'Safety_Advanced_80s_Name': 'Advanced 80s',
            
            'Safety_Basic_90s_Name': 'Basic 90s',
            'Safety_Standard_90s_Name': 'Standart 90s',
            'Safety_Advanced_90s_Name': 'Advanced 90s',
            
            'Safety_Basic_00s_Name': 'Basic 00',
            'Safety_Standard_00s_Name': 'Standart 00s',
            'Safety_Advanced_00s_Name': 'Advanced 00s',
            
            'Safety_Basic_10s_Name': 'Basic 10s',
            'Safety_Standard_10s_Name': 'Standart 10s',
            'Safety_Advanced_10s_Name': 'Advanced 10s',
            
            'Safety_Basic_20s_Name': 'Basic 20s',
            'Safety_Standard_20s_Name': 'Standart 20s',
            'Safety_Advanced_20s_Name': 'Advanced 20s',
        },
        'Springs': {
            'Springs_Passive_Name': 'Standart',
            'Springs_Progressive_Name': 'Progressive',
            'Springs_Hydro_Name': 'Hydropneumatic',
            'Springs_Air_Name': 'Air',
            'Springs_ActiveSport_Name': 'Active Sport',
            'Springs_ActiveComfort_Name': 'Active Comfort'
        },
        'Dampers': {
            'Dampers_Passive_Name': 'Twin-Tube',
            'Dampers_Advanced_Name': 'Gas Mono-Tube',
            'Dampers_Adaptive_Name': 'Adaptive',
            'Dampers_SemiActive_Name': 'Semi Active'
        },
        'SwayBars': {
            'SwayBars_Passive_Name': 'Passive',
            'SwayBars_SemiActive_Name': 'Semi Active',
            'SwayBars_Offroad_Name': 'Offroad',
            'SwayBars_Active_Name': 'Active',
        },
        # 
        # MODEL
        # 
        'Chassis': {
            'Chassis_Ladder_Name': 'Ladder',
            'Chassis_SpaceFrame_Name': 'Spaceframe',
            'Chassis_Monocoque_Name': 'Monocoque',
            'Chassis_SemiSpaceFrame_Name': 'Semi Space Frame',
            'Chassis_LightTruckMonocoque_Name': 'Light Truck Monocoque'
        },
        'ChassisMaterial': {
            'ChassisMat_Steel_Name': 'Steel',
            'ChassisMat_GalvanizedSteel_Name': 'Galvanized Steel',
            'ChassisMat_CRESteel_Name': 'Corrosion Resistant Steel',
            'ChassisMat_AHSSteel_Name': 'AHS Steel',
            'ChassisMat_AHSLight_Name': 'Light AHS Steel',
            'ChassisMat_Alu_Name': 'Aluminium',
            'ChassisMat_GluedAlu_Name': 'Glued Aluminium',
            'ChassisMat_CarFibre_Name': 'Carbon Fibre'
        },
        'EnginePlacement': {
            'EngPlace_FrTransverse_Name': 'Front Transverse',
            'EngPlace_FrLong_Name': 'Front Longitudinal',
            'EngPlace_MidTransverse_Name': 'Mid Transverse',
            'EngPlace_MidLong_Name': 'Mid Longitudinal',
            'EngPlace_RearLong_Name': 'Rear Longitudinal'
            # Rear Trans?
        },
        'FrontSuspension': {
            'Suspend_SolAxLeaf_Name': 'Solid Axel Leaf',
            'Suspend_SolAxCoil_Name': 'Solid Axel Coil',
            'Suspend_MacPher_Name': 'Macpherson',
            'Suspend_DblWishbone_Name': 'Double Wishbone',
            'Suspend_Pushrod_Name': 'Pushrod'
        },
        'RearSuspension': {
            'Suspend_SolAxLeaf_Name': 'Solid Axel Leaf',
            'Suspend_SolAxCoil_Name': 'Solid Axel Coil',
            'Suspend_MacPher_Name': 'Macpherson',
            'Suspend_SemiTrailArm_Name': 'Semitrailing Arm',
            'Suspend_DblWishbone_Name': 'Double Wishbone',
            'Suspend_Torsion_Name': 'Torsion Beam',
            'Suspend_Multilink_Name': 'Multilink',
            'Suspend_Pushrod_Name': 'Pushrod'
        },
        'PanelMaterial': {
            'PanelMat_Steel_Name': 'Steel',
            'PanelMat_TreatedSteel_Name': 'Treated Steel',
            'PanelMat_Alu_Name': 'Aluminium',
            'PanelMat_PartialAlu_Name': 'Partially Aluminium',
            'PanelMat_CRSteel_Name': 'Corrosion Resistant Steel',
            'PanelMat_FibreGlass_Name': 'Fibre Glass',
            'PanelMat_CarbonFibre_Name': 'Carbon Fiber'
        },
        # 
        #  Variant
        #
        'Crank': {
            'CrankMat_Iron_Name': 'Cast Iron',
            'CrankMat_Forged_Name': 'Forged Steel',
            'CrankMat_IronFP_Name': 'Cast Iron Flat plane',
            'CrankMat_ForgedFP_Name': 'Forged Steel Flat Plane',
            'CrankMat_Billet_Name': 'Billet Steel',
            'CrankMat_BilletFP_Name': 'Billet Steel Flat Plane'
        },
        'Conrods': {
            'RodMat_Cast_Name': 'Cast',
            'RodMat_HeavyCast_Name': 'Heavy Duty Cast',
            'RodMat_HBeam_Name': 'Heavy Duty Forged',
            'RodMat_IBSteel_Name': 'Lightweight Forged',
            'RodMat_IBTit_Name': 'Lightweight Titanium'
        },
        'Pistons': {
            'Piston_Cast_Name': 'Cast',
            'Piston_HeavyCast_Name': 'Heavy Duty Cast',
            'Piston_Forged_Name': 'Forged',
            'Piston_LightForged_Name': 'Ligweight Forged',
            'Piston_LowFCast_Name': 'Low Friction Cast',
            'Piston_HypCast_Name': 'Hypereutectic Cast',
        },
        'VVT': {
            'VarValves_None_Name': 'None',
            'VarValves_VVTOHV_Name': 'Variable Cam',
            'VarValves_VVTSOHC_Name': 'Variable Cam',
            'VarValves_VVTIntakeCam_Name': 'Intake VVT',
            'VarValves_VVTDOHC_Name': 'Double VVT'
        },
        'Aspiration': {
            'Aspiration_Natural_Name': 'Naturally Aspirated',
            'Turbo_Single_Name': 'Single Turbo',
            'Turbo_Twin_Name': 'Twin Turbo',
        },
        'AspirationType': {
            'Aspiration_Natural_Name': 'Naturally Aspirated',
            'Aspiration_Turbo_Name': 'Forced Induction'
        },
        'AspirationOption': {
            'NoOption_Name': 'None',
            'TurboBearing_Journal_Name': 'Journal Bearing',
            'TurboBearing_BallBearing_Name': 'Ball Bearing'
        },
        'FuelType': {
            'FuelType_LowQLead_Name': 'Low Quality',
            'FuelType_RegLead_Name': 'Regular Leaded',
            'FuelType_Super_Name': 'Super Leaded',
            'FuelType_RegUnlead_Name': 'Regular',
            'FuelType_Premium_Name': 'Premium',
            'FuelType_SuperPrem_Name': 'Super',
            'FuelType_Super100_Name': 'Ultimate'
        },
        'FuelSystemType': {
            'FuelSys_Carb_Name': 'Carburetor',
            'FuelSys_Inj_Name': 'Injection',
        },
        'FuelSystem': {
            'FuelSys_Carb_1Barrel_Name': '1 BRL',
            'FuelSys_Carb_1BarrelEco_Name': '1 BRL Eco',
            'FuelSys_Carb_2Barrel_Name': '2 BRL',
            'FuelSys_Carb_4Barrel_Name': '4 BRL',
            'FuelSys_Carb_DCOE_Name': 'DCOE',
            'FuelSys_Inj_Mech_Name': 'MFI',
            'FuelSys_Inj_SingEFI_Name': 'SPFI',
            'FuelSys_Inj_MultiEFI_Name': 'MPFI',
            'FuelSys_Inj_Direct_Name': 'Direct Injection'
        },
        'IntakeManifold': {
            'FuelSys_CarbIntake_Single_Name': 'Single Carb',
            'FuelSys_CarbIntake_Twin_Name': 'Twin Carb',
            'FuelSys_CarbIntake_Triple_Name': 'Triple Carb',
            'FuelSys_CarbIntake_Quad_Name': 'Four Carb',
            'FuelSys_CarbIntake_Penta_Name': 'Five Carb',
            'FuelSys_CarbIntake_Hexa_Name': 'Six Carb',
            'FuelSys_InjIntake_Single_Name': 'Single Injection',
            'FuelSys_InjIntake_Twin_Name': 'Twin Injection',
            'FuelSys_InjIntake_PerCyl_Name': 'Per Cylinder',
        },
        'Intake': {
            'FuelSys_CarbFilter_Standard_Name': 'Standart Intake',
            'FuelSys_CarbFilter_Perfom_Name': 'Pefromance Intake',
            'FuelSys_CarbFilter_Race_Name': 'Race Intake',
            'FuelSys_InjFilter_Standard_Name': 'Standart Intake',
            'FuelSys_InjFilter_Perform_Name': 'Pefromance Intake',
            'FuelSys_InjFilter_Race_Name': 'Race Intake'
        },
        'Headers': {
            'Header_CastLog_Name': 'Cast Log',
            'Header_ShortCast_Name': 'Short Cast',
            'Header_Tube_Name': 'Tubular',
            'Header_LongTube_Name': 'Long Tubular',
            'Header_RaceTube_Name': 'Race Tubular'
        },
        'ExhaustCount': {
            'Exhausts_1_Name': 'Single Pipe',
            'Exhausts_2_Name': 'Dual Pipe'
        },
        'Cat': {
            'CatConvert_None_Name': 'None',
            'CatConvert_2Way_Name': 'Two-way',
            'CatConvert_3Way_Name': 'Three-way',
            'CatConvert_High3Way_Name': 'High Flow Three-way'
        },
        'Muffler1': {
            'Muffler_None_Name': 'None',
            'Muffler_Straight_Name': 'Straight Through',
            'Muffler_Confused_Name': 'Baffled',
            'Muffler_Reverse_Name': 'Reverse Flow'
        },
        'Muffler2': {
            'Muffler_None_Name': 'None',
            'Muffler_Straight_Name': 'Straight Through',
            'Muffler_Confused_Name': 'Baffled',
            'Muffler_Reverse_Name': 'Reverse Flow'
        },
        'BlockConfig': {
            'EngBlock_Inl3_Name': 'Inline-3',
            'EngBlock_Inl4_Name': 'Inline-4',
            'EngBlock_Inl5_Name': 'Inline-5',
            'EngBlock_Inl6_Name': 'Inline-6',
            'EngBlock_V6_Name': 'V6',
            'EngBlock_V8_Name': 'V8',
            'EngBlock_V10_Name': 'V12',
            'EngBlock_V12_Name': 'V12',
            'EngBlock_V16_Name': 'V16',
            'EngBlock_Box4_Name': 'Boxer-4',
            'EngBlock_Box6_Name': 'Boxer-6',
        },
        'BlockType': {
            'EngBlock_V60_Name': 'V 60°',
            'EngBlock_V90_Name': 'V 90°',
            'EngBlock_Inl_Name': 'Inline',
            'EngBlock_Boxer_Name': 'Boxer'
        },
        'BlockMaterial': {
            'EngBlockMat_Iron_Name': 'Cast Iron',
            'EngBlockMat_Alu_Name': 'Aluminium',
            'EngBlockMat_AluSil_Name': 'AlSi',
            'EngBlockMat_Mg_Name': 'Magnesium',
        },
        'Head': {
            'Head_PushRod_Name': 'Push Rod',
            'Head_DirectOHC_Name': 'Direct Acting OHC',
            'Head_OHC_Name': 'SOHC',
            'Head_DuelOHC_Name': 'DOHC'
        },
        'HeadMaterial': {
            'HeadMat_Iron_Name': 'Cast Iron',
            'HeadMat_Alu_Name': 'Aluminium',
            'EngBlockMat_AluSil_Name': 'AlSi'
        },
        'Valves': {
            'ValveCount_1_Name': '1',
            'ValveCount_2_Name': '2',
            'ValveCount_3_Name': '3',
            'ValveCount_4_Name': '4',
            'ValveCount_5_Name': '5'
        },
        'VVL': {
            'VarValves_None_Name': 'None',
            'VarValves_VVL_Name': 'VVL'
        }
    }

    toInt = {
        'FootPrintWidth',
        'FootPrintLength',
        'OverallDiameter',
        'FrontPadSize',
        'RearPadSize',
        'CargoVolume',
        'FullSeats',
        'TempSeats',
        'Year',
        'BodyYear',
        'RPMLimit',
        'PeakBoostRPM',
        'PeakTorqueRPM',
        'PeakPowerRPM',
        'MaxRPM'
    }

    toFloat2 = {
        'Cornering',
        'Capacity'
    }

    if arg == 'FootPrintWidth':
        # From cm to m
        return round(argValue / 100, 2)
    elif arg == 'FootPrintLength':
        return round(argValue / 100, 2)

    if arg == 'PeakPower':
        # Convert kW to HP
        return round(argValue * 1.34102208, 1)

    if arg in toInt:
        return int(argValue)

    if arg in toFloat2:
        return round(argValue, 2)

    if arg in switcher:
        return switcher.get(arg).get(argValue, argValue)

    if type(argValue) is float:
        return round(argValue, 1)
    return argValue
        