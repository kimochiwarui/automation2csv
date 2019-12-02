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
    DriveType,
    GearboxType,
    GearboxRatios,
    Differential,
    PowerDistribution,
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
    FrontRowSeats,
    SecondRowSeats,
    ThirdRowSeats,
    Interior,
    Entertainment,
    PowerSteering,
    Assist,
    Safety,
    Springs,
    Dampers,
    SwayBars,
    FrontCamber,
    RearCamber
    FROM Trims""")
    rows = c.fetchall()
    for d in rows:
        data.append(d)
    for d in data:
        c.execute("""SELECT
        Name as Model,
        Chassis,
        ChassisMaterial,
        EnginePlacement,
        FrontSuspension,
        RearSuspension,
        PanelMaterial
        FROM Models WHERE UID=?""", (d["MUID"],))
        model = c.fetchone()
        for key in model:
            d[key] = model[key]

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
        AFR,
        RPMLimit,
        ARRatio,
        BoostCutOff
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
        FROM Families WHERE UID=?""",
                  (d['FUID'],))
        family = c.fetchone()
        for key in family:
            d[key] = family[key]
    return data