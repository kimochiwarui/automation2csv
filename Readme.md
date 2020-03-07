## automation2csv
It is db exporter.

To create custom export preset for exporter incorporate key in ** and add + as prefix e.g. \*+Model\*, \*+Trim\*, \*+DrivabilityValue\*


Here is a list of all keys, 95% are the same as db table headers. Returned data is mostly metric.

This list of almost full to the in game, with notable exception of wheelbase, 200m g-force, Trim Material cost, Trim Engineering Time and Trim Production Units.

### Names

| Key      |      Description      |
| -------- | :-------------------: |
| Model    |    Car Model name     |
| Trim     |     Car Trim name     |
| Family   |  Engine Family name   |
| Variant  |  Engine Variant name  |
| Year     |       Trim Year       |
| BodyType | "Sedan" / "Hatchback" |

### Calculated Automation stats
| Key                     |
| ----------------------- |
| DrivabilityValue        |             
| SportinessValue         |            
| ComfortValue            |             
| PrestigeValue           |
| SafetyValue             |
| Practicality            |
| Utility                 |
| Offroad                 |
| Reliability             |
| EnvironmentalResistance |

### Trim Stats
| Key             |  Description   |
| --------------- | :------------: |
| FootPrintWidth  | Vehicle Width  |
| FootPrintLength | Vehicle Length |
| Economy         |   in l/100km   |
| Weight          |     in kg      |
| CargoVolume     |       l        |
| Emissions       | trim emission  |
| FullSeats       |      # of      |
| TempSeats       |      # of      |
| RON             |   in number    |
| ServiceCosts    |                |
| Price           | Assumed Price  |

### Perfomance
| Key             |  Description  |
| --------------- | :-----------: |
| HundredTime     |     0-100     |
| QuarterMileTime |    seconds    |
| KilometerTime   |    seconds    |
| TopSpeed        |    in km/h    |
| Cornering       |  20m g-force  |
| BrakingDistance |    meters     |
| TowWeight       |      kg       |

#### Chassis
| Key             |       Description       |
| --------------- | :---------------------: |
| Chassis         | Choice of Ladder/Monock |
| ChassisMaterial |   Material of chassis   |
| EnginePlacement |     Engine Position     |
| FrontSuspension |
| RearSuspension  |
| PanelMaterial   |
| QualityChassis  |

### Drivetrain
| Key               |         Description          |
| ----------------- | :--------------------------: |
| DriveType         |       4x4/AWD/RWD/FWD        |
| GearboxType       |                              |
| GearboxRatios     |          # of gears          |
| Differential      |      Differential type       |
| PowerDistribution |   in number, 0 rwd - 1 fwd   |
| QualityGearbox    | # of Quality points spent on |


### Tyres
| Key             |   Description   |
| --------------- | :-------------: |
| TyreType        | Crossply/Radial |
| Tyres           |  Tyre compound  |
| OverallDiameter |    of wheel     |
| RimDiameter     |       in        |
| FrontTyreWidth  |       mm        |
| RearTyreWidth   |       mm        |
| RimMaterial     | Chosen material |
| QualityTyre     |                 |

### Brakes 
| Key               |     Description      |
| ----------------- | :------------------: |
| FrontBrakeType    |     Drums/Discs      |
| FrontBrakeOptions |    # of calipers     |
| FrontPadType      |       Overall        |
| FrontPadSize      |      Brake Size      |
| RearBrakeType     |     Drums/Discs      |
| RearBrakeOptions  |    # of calipers     |
| RearPadSize       |      Brake Size      |
| BrakeBias         | number, 0 through 1, |
| QualityBrakes     |                      |

### Aero
| Key              |        Description         |
| ---------------- | :------------------------: |
| Undertray        |        Name of one         |
| Downforce        | amout of,   0-none, 1-100% |
| ActiveWing       |            y/n             |
| ActiveCooling    |            y/n             |
| InclinationFront | Front and rear wing angle  |
| InclinationRear  |          in 0 - 1          |

### Interior, Driver Assists and Safety
| Key                |        Description         |
| ------------------ | :------------------------: |
| Interior           |      Chosen Interior       |
| Entertainment      |    Chosen Entertainment    |
| PowerSteering      |       Same as above        |
| Assists            |            -//-            |
| Safety             |            -//-            |
| QualityInterior    |        for Interior        |
| QualityElectronics | for Assists/Power Steering |
| QualitySafety      |         for Safety         |

### Suspension
| Key               |   Description    |
| ----------------- | :--------------: |
| Springs           | Type of springs  |
| Dampers           | Type of dampers  |
| SwayBars          | Type of sway bar |
| FrontCamber       |      angle       |
| RearCamber        |      angle       |
| QualitySuspension |                  |

### Engine Configuration
| Key           |       Description       |
| ------------- | :---------------------: |
| BlockType     |   inline/v# 60*/Boxer   |
| BlockConfig   | Inline-3/v8 60*/Boxer 6 |
| BlockMaterial |        Material         |
| Head          |   Head configuration    |
| HeadMaterial  |        Material         |
| Valves        |       Valve Count       |
| VVL           |           Y/N           |
| Bore          |  Bore of Engine Family  |
| Stroke        | Stroke of Engine Family |

### Engine Stats
| Key                   | Description |
| --------------------- | :---------: |
| EngineWeight          |     kg      |
| PerfomanceIndex       |
| PeakTorque            |     idk     |
| PeakTorqueRPM         |
| PeakPower             |     hp      |
| PeakPowerRPM          |
| PeakBoost             |
| PeakBoostRPM          |
| MaxRPM                |
| Capacity              |   litres    |
| ManHours              |
| Noise                 |
| Responsiveness        |
| Smoothness            |
| EngineEngineeringTime |
| EngineMaterialCost    |
| EngineServiceCost     |

### Engine Extended Configuration/Stats 
| Key                  |         Description          |
| -------------------- | :--------------------------: |
| CoolingRequired      |
| EngineEmissions      |
| IdleSpeed            |
| VarianBore           |
| VariantStroke        |
| Crank                |           type of            |
| Conrods              |           type of            |
| Pistons              |           type of            |
| VVT                  |             y/n              |
| Compression          |
| CamProfileSetting    |
| VVLCamProfileSetting |
| Aspiration           |      NA/SingleTurbo/TT       |
| AspirationType       |     NA/Forced Induction      |
| AspirationOption     |    Ball/Journal Bearings     |
| IntercoolerSetting   |       as relative 0-1        |
| ARRatio              |
| FuelSystemType       |           Carb/Inj           |
| FuelSystem           |      MPFI/DCOE/2BBRRRL       |
| IntakeManifold       |   Single/Twin/Per Cylinder   |
| Intake               |   Standart/Perfomance/Race   |
| FuelType             | string like "Super Unleaded" |
| Headers              |
| ExhaustCount         |
| Cat                  |   Catalytic converter type   |
| Muffler1             |
| Muffler2             |
| QualityBottomEnd     |
| QualityTopEnd        |
| QualityAspiration    |
| QualityFuelSystem    |
| QualityExhaust       |