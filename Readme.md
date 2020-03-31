## automation2csv
It is Automation Game db exporter.

![](https://i.imgur.com/6Pa5p1e.png)

Either run with python or run app.exe file in dist.
To create custom export preset for exporter incorporate key in ** and add + as prefix e.g. \*+Model\*, \*+Trim\*, \*+Drivability\* save that as txt file in same folder as run executable.

### Legend
Here is a list of all exportable keys, 80% are the same as db table headers. Returned data is mostly metric.

This list of almost full to the one in game, with notable exception of wheelbase, 200m g-force, Trim Material cost, Trim Engineering Time and Trim Production Units, Interior Space.

### Names

| Key      |                Description                |
| -------- | :---------------------------------------: |
| Model    |                Model name                 |
| Trim     |                 Trim name                 |
| Family   |               Engine Family               |
| Variant  |              Engine Variant               |
| Year     |                 Trim Year                 |
| BodyType | "Sedan" / "Hatchback" (line as in editor) |

### Calculated Automation stats
| Key                     |
| ----------------------- |
| Drivability             |
| Sportiness              |
| Comfort                 |
| Prestige                |
| Safety                  |
| Practicality            |
| Utility                 |
| Offroad                 |
| Reliability             |
| EnvironmentalResistance |

### Trim Stats
| Key             |       Description        |
| --------------- | :----------------------: |
| FootPrintWidth  | Vehicle Width in metres  |
| FootPrintLength | Vehicle Length in metres |
| Economy         |        in l/100km        |
| Weight          |          in kg           |
| CargoVolume     |        in litres         |
| Emissions       |      Trim emission       |
| FullSeats       |           # of           |
| TempSeats       |           # of           |
| RON             |   Required RON rating    |
| ServiceCosts    |         in $AGD          |
| Price           |  Assumed Price in $AGD   |

### Perfomance
| Key             | Description |
| --------------- | :---------: |
| HundredTime     |    0-100    |
| QuarterMileTime |   seconds   |
| KilometerTime   |   seconds   |
| TopSpeed        |   in km/h   |
| Cornering       | 20m g-force |
| BrakingDistance |   meters    |
| TowWeight       |     kg      |

### Chassis
| Key             |     Description      |
| --------------- | :------------------: |
| Chassis         |    for all below     |
| ChassisMaterial |  line as in editor   |
| EnginePlacement |                      |
| FrontSuspension |                      |
| RearSuspension  |                      |
| PanelMaterial   |                      |
| QualityChassis  | Quality points spent |

### Drivetrain
| Key               |                        Description                         |
| ----------------- | :--------------------------------------------------------: |
| DriveType         |                       for all below                        |
| GearboxType       |                     line as in editor                      |
| GearboxRatios     |                         # of gears                         |
| SpeedLimiter      |                     in km/h, 0 - none                      |
| Differential      |                     line as in editor                      |
| PowerDistribution | Float number, useful for awd vehicles, 0 - rwd and 1 - fwd |
| QualityGearbox    |                    Quality points spent                    |


### Tyres
| Key             |     Description      |
| --------------- | :------------------: |
| TyreType        |   Crossply/Radial    |
| Tyres           |    Tyre compound     |
| OverallDiameter |     millimeters      |
| RimDiameter     |        inches        |
| FrontTyreWidth  |     millimeters      |
| RearTyreWidth   |     millimeters      |
| RimMaterial     |   Chosen material    |
| QualityTyre     | Quality points spent |

### Brakes 
| Key               |               Description               |
| ----------------- | :-------------------------------------: |
| FrontBrakeType    |     Drums/Discs (line as in editor)     |
| FrontBrakeOptions |    # of calipers (line as in editor)    |
| FrontPadSize      |         Front Brake Size in mm          |
| RearBrakeType     |     Drums/Discs (line as in editor)     |
| RearBrakeOptions  |    # of calipers (line as in editor)    |
| RearPadSize       |          Rear Brake Size in mm          |
| PadType           | Float number, 0 to 1 where 0 is softest |
| BrakeBias         |          Float number, 0 to 1           |
| QualityBrakes     |          Quality points spent           |

### Aero
| Key                    |                   Description                    |
| ---------------------- | :----------------------------------------------: |
| Undertray              |                line as in editor                 |
| Downforce              |         Float number, 0 - none, 1 - 100%         |
| ActiveWing             |                line as in editor                 |
| ActiveCooling          |                line as in editor                 |
| InclinationFront       | Float number, Front wing angle, 0 - 0%, 1 - 100% |
| InclinationRear        |          Float number, Rear wing angle           |
| CoolingAirflowFraction |               Float number, 0 to 1               |
| BrakeCoolingFraction   |               Float number, 0 to 1               |
| QualityAero            |               Quality points spent               |

### Interior, Driver Assists and Safety
| Key                |                  Description                   |
| ------------------ | :--------------------------------------------: |
| Interior           |                 for all below                  |
| Entertainment      |               line as in editor                |
| PowerSteering      |                                                |
| Assists            |                                                |
| SafetyFeatures     |                                                |
| QualityInterior    |        Quality points spent on Interior        |
| QualityElectronics | Quality points spent on Assists/Power Steering |
| QualitySafety      |         Quality points spent on Safety         |

### Suspension
| Key                   |     Description      |
| --------------------- | :------------------: |
| Springs               |    for all below     |
| Dampers               |  line as in editor   |
| SwayBars              |                      |
| FrontCamber           |        angle         |
| RearCamber            |        angle         |
| FrontSpringStiffness  |  idk for all below   |
| RearSpringStiffness   |
| FrontDamperStiffness  |
| RearDumperStiffness   |
| FrontSwayBarStiffness |
| RearSwayBarStiffness  |
| RideHeight            |
| SuspensionOffset      |
| BaseFrontTrackWidth   |
| BaseRearTrackWidth    |
| QualitySuspension     | Quality points spent |

### Engine Configuration
| Key           |                 Description                 |
| ------------- | :-----------------------------------------: |
| BlockType     |   inline/v# 60*/Boxer (line as in editor)   |
| BlockConfig   | Inline-3/v8 60*/Boxer 6 (line as in editor) |
| BlockMaterial |                  Material                   |
| Head          |             Head configuration              |
| HeadMaterial  |                  Material                   |
| Valves        |                 Valve Count                 |
| VVL           |                     Y/N                     |
| Bore          |            Bore of Engine Family            |
| Stroke        |           Stroke of Engine Family           |

### Engine Stats
| Key                |            Description            |
| ------------------ | :-------------------------------: |
| EngineWeight       |                kg                 |
| PerfomanceIndex    |               index               |
| PeakTorque         |               in Nm               |
| PeakTorqueRPM      |        Rpm at peak Torque         |
| PeakPower          |  in HP (converted those from kW)  |
| PeakPowerRPM       |         Rpm at peak Power         |
| PeakBoost          |         Peak boost at bar         |
| PeakBoostRPM       | Rpm at which Turbo spools at full |
| MaxRPM             |              Redline              |
| Capacity           |             in litres             |
| Noise              |               index               |
| Responsiveness     |               index               |
| Smoothness         |               index               |
| EnginePU           |      Engine Production Units      |
| EngineET           |      Engine Engineering Time      |
| EngineMaterialCost |       Engine Material Cost        |
| EngineServiceCost  |        Engine Service Cost        |

### Engine Extended Configuration/Stats 
| Key                   |                 Description                 |
| --------------------- | :-----------------------------------------: |
| CoolingRequired       |                    index                    |
| EngineEmissions       |                    index                    |
| IdleSpeed             |                  Idle RPM                   |
| VarianBore            |             number as in editor             |
| VariantStroke         |             number as in editor             |
| Crank                 |       for all below line as in editor       |
| Conrods               |                                             |
| Pistons               |                                             |
| VVT                   |                                             |
| Compression           |              Compression ratio              |
| CamProfileSetting     |             Number from 0 to 1              |
| VVLCamProfileSetting  |                same as above                |
| Aspiration            |              NA/SingleTurbo/TT              |
| AspirationType        |             NA/Forced Induction             |
| AspirationOption      |            Ball/Journal Bearings            |
| IntercoolerSetting    |            Float number, 0 to 1             |
| ARRatio               |             number as in editor             |
| FuelSystemType        |            Carburated/Injection             |
| FuelSystem            | MPFI/DCOE/2BBRRRL Carb  (line as in editor) |
| IntakeManifold        |  Single/Twin/Twin Carb (line as in editor)  |
| Intake                |       Intake type (line as in editor)       |
| FuelType              |    "Super Unleaded" (line as in editor)     |
| AFR                   |              Air to Fuel Ratio              |
| IgnitionTimingSetting |                Float, 0 to 1                |
| Headers               |              line as in editor              |
| ExhaustCount          |                                             |
| ExhaustDiameter       |                   inches                    |
| Cat                   |          Catalytic converter type           |
| Muffler1              |              line as in editor              |
| Muffler2              |              line as in editor              |
| QualityBottomEnd      |                Points spent                 |
| QualityTopEnd         |
| QualityAspiration     |
| QualityFuelSystem     |
| QualityExhaust        |