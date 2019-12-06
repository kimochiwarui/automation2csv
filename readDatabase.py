import sqlite3
from sqlite3 import Error


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def readDatabase(databasePointer):
    data = []
    conn = sqlite3.connect(databasePointer)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("""SELECT
    UID,
    MUID,
    VUID,
    Name as Trim,
    FootPrintWidth,
    FootPrintLength,
    DriveType,
    GearboxType,
    GearboxRatios,
    Differential,
    TyreType,
    Tyres,
    OverallDiameter,
    RimDiameter,
    FrontTyreWidth,
    RearTyreWidth,
    FrontRimOffset,
    RearRimOffset,
    RimMaterial,
    FrontBrakeType,
    FrontBrakeOptions,
    FrontPadType,
    FrontPadSize,
    RearBrakeType,
    RearBrakeOptions,
    RearPadSize,
    BrakeBias,
    Undertray,
    Downforce,
    ActiveWing,
    ActiveCooling,
    InclinationFront,
    InclinationRear,
    Interior,
    Entertainment,
    PowerSteering,
    Assist,
    Safety,
    Springs,
    Dampers,
    SwayBars,
    FrontCamber,
    RearCamber,
    QualityBody,
    QualityGearbox,
    QualityTyre,
    QualityBrakes,
    QualityInterior,
    QualityElectronics,
    QualitySafety,
    QualitySuspension
    FROM Trims""")
    trims = c.fetchall()
    for d in trims:
        data.append(d)

    for d in data:
        c.execute("""SELECT
        Name as Model,
        Chassis,
        ChassisMaterial,
        EnginePlacement,
        FrontSuspension,
        RearSuspension,
        PanelMaterial,
        QualityChassis
        FROM Models WHERE UID=?""", (d["MUID"],))
        model = c.fetchone()
        for key in model:
            d[key] = model[key]

        c.execute("""SELECT
        GameVersion,
        BodyType,
        Year
        BodyYear,
        DrivabilityValue,
        SportinessValue,
        ComfortValue,
        PrestigeValue,
        SafetyValue,
        Practicality,
        Utility,
        Offroad,
        Weight,
        Economy,
        CargoVolume,
        EnvironmentalResistance,
        Emissions,
        TowWeight,
        FullSeats,
        TempSeats,
        Reliability,
        Cornering,
        HundredTime,
        TopSpeed,
        KilometerTime,
        BrakingDistance,
        QuarterMileTime,
        PowerDistribution,
        Price,
        ServiceCosts
        FROM TrimResults WHERE UID=?""", (d["UID"],))
        trimResult = c.fetchone()
        if trimResult is not None:
            for key in trimResult:
                d[key] = trimResult[key]
            
        c.execute("""SELECT
        FUID,
        Name as Variant,
        Crank,
        Conrods,
        Pistons,
        VVT,
        Aspiration,
        AspirationType,
        AspirationOption,
        IntercoolerSetting,
        FuelSystemType,
        FuelSystem,
        IntakeManifold,
        Intake,
        FuelType,
        Headers,
        ExhaustCount,
        Cat,
        Muffler1,
        Muffler2,
        Bore as VarianBore,
        Stroke as VariantStroke,
        Capacity,
        Compression,
        CamProfileSetting,
        VVLCamProfileSetting,
        AFR,
        IgnitionTimingSetting,
        ARRatio,
        QualityBottomEnd,
        QualityTopEnd,
        QualityAspiration,
        QualityFuelSystem,
        QualityExhaust
        FROM Variants WHERE UID=?""", (d['VUID'],))
        variant = c.fetchone()
        for key in variant:
            d[key] = variant[key]

        c.execute("""SELECT
        Name as Family,
        BlockConfig,
        BlockMaterial,
        BlockType,
        Head,
        HeadMaterial,
        Valves,
        VVL,
        Bore,
        Stroke
        FROM Families WHERE UID=?""", (d['FUID'],))
        family = c.fetchone()
        for key in family:
            d[key] = family[key]

        c.execute("""SELECT
        CoolingRequired,
        IdleSpeed,
        Noise,
        PeakBoost,
        PeakBoostRPM,
        PeakTorque,
        PeakTorqueRPM,
        PeakPower,
        PeakPowerRPM,
        MaxRPM,
        RON,
        PerformanceIndex,
        Responsiveness,
        Smoothness,
        Weight as EngineWeight,
        EngineeringTime as EngineEngineeringTime,
        Emissions as EngineEmissions,
        ManHours,
        MaterialCost as EngineMaterialCost,
        ServiceCost as EngineServiceCost
        FROM EngineResults WHERE UID=?""", (d['VUID'],))
        engineResult = c.fetchone()
        if engineResult is not None:       
            for key in engineResult:
                d[key] = engineResult[key]
    return data