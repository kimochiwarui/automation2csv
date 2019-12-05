## automation2csv
It is db exporter.

To create custom export preset for exporter incorporate key in ** and add + as prefix e.g. \*+Model\*, \*+Trim\*, \*+DrivabilityValue\*


Here is a list of all keys, they are the same as db table headers. 

#### Models
| Key             |
| --------------- |
| Model           |
| Chassis         |        
| ChassisMaterial |        
| FrontSuspension |        
| RearSuspension  |        
| PanelMaterial   |       
| QualityChassis  |        

### Calculated
| Key                     | Description |
| ----------------------- | :---------: |
| DrivabilityValue        |             |
| SportinessValue         |             |
| ComfortValue            |             |
| PrestigeValue           |
| SafetyValue             |
| Economy                 |
| Practicality            |
| Utility                 |
| Offroad                 |
| Weight                  |    in kg    |
| HundredTime             |    0-100    |
| TopSpeed                |
| KilometerTime           |
| BrakingDistance         |
| CargoVolume             |
| QuarterMileTime         |
| ServiceCosts            |
| EnvironmentalResistance |
| Emissions               |
| Cornering               |   20m gf    |
| BodyType                |
| TowWeight               |
| FullSeats               |
| TempSeats               |
| Reliability             |
| Year                    |  Trim Year  |
| FuelType                |
| RON                     |
| Price                   |

#### Trims
| Key                   |       Description       |
| --------------------- | :---------------------: |
| FootPrintWidth        |      Vehicle Width      |
| FootrpintLength       |     Vehicle Length      |
| Height                |                         |
| Trim                  |        Trim Name        |
| DriveType             |                         |
| GearboxType           |     Eg manual/Auto      |
| GearboxRatios         |       # of gears        |
| Differential          |    Differential type    |
| PowerDistribution     | in number 0 rwd - 1 fwd |
| TyreType              |     Crossply/Radial     |
| Tyres                 |      Tyre compound      |
| OverallDiameter       |         of tyre         |
| RimDiameter           |                         |
| FrontTyreWidth        |                         |
| RearTyreWidth         |                         |
| RimMaterial           |                         |
| FrontBrakeType        |       Drums/Discs       |
| FrontBrakeTypeOptions |      # of calipers      |
| FrontPadType          |    overall Pad type     |
| FrontPadSize          |       Brake Size        |
| RearBrakeType         |       Drums/Discs       |
| RearBrakeOptions      |                         |
| RearPadSize           |                         |
| BrakeBias             |    Relative(???????)    |
| Undertray             |                         |
| Downforce             |     0-none, 1-100%      |
| ActiveWing            |                         |
| ActiveCooling         |                         |
| InclinationFront      |    Front wing angle     |
| InclinationRear       |                         |
| Interior              |                         |
| Entertainment         |                         |
| PowerSteering         |                         |
| Assists               |     Driver Assists      |
| Safety                |                         |
| Springs               |                         |
| Dampers               |                         |
| SwayBars              |                         |
| FrontCamber           |                         |
| RearCamber            |                         |
| QualityBody           |                         |
| QualityGearbox        |                         |
| QualityTyre           |                         |
| QualityBrakes         |                         |
| QualityInterior       |                         |
| QualityElectronics    |                         |
| QualitySafety         |                         |
| QualitySuspension     |                         |

#### Engine Family

| Key           |       Description       |
| ------------- | :---------------------: |
| Family        |       Family Name       |
| BlockType     |   inline/v# 60*/Boxer   |
| BlockConfig   | Inline-3/v8 60*/Boxer 6 |
| BlockMaterial |                         |
| Head          |   Head configuration    |
| HeadMaterial  |                         |
| Valves        |       Valve Count       |
| VVL           |           Y/N           |
| Bore          |
| Stroke        |


#### Engine Variant

| Key                  |       Description        |
| -------------------- | :----------------------: |
| Variant              |       Variant Name       |
| EngineWeight         |
| CoolingRequired      |
| Emissions            |
| EngineeringTime      |
| IdleSpeed            |
| ManHours             |
| MaterialCost         |
| Noise                |
| PeakBoost            |
| PeakBoostRPM         |
| PerfomanceIndex      |
| Responsiveness       |
| ServiceCost          |
| Smoothness           |
| PeakTorqueRPM        |
| PeakPower            |
| PeakPowerRPM         |
| MaxRPM               |
| VarianBore           |
| VariantStroke        |
| Capacity             |
| Crank                |
| Conrods              |
| Pistons              |
| VVT                  |
| Compression          |
| CamProfileSetting    |
| VVLCamProfileSetting |
| Aspiration           |    NA/SingleTurbo/TT     |
| AspirationType       |         NA/Turbo         |
| AspirationOption     |  Ball/Journal Bearings   |
| IntercoolerSetting   |     as relative 0-1      |
| ARRatio              |
| BoostCutOff          |
| FuelSystemType       |         Carb/Inj         |
| FuelSystem           |    MPFI/DCOE/2BBRRRL     |
| IntakeManifold       | Single/Twin/Per Cylinder |
| Intake               | Standart/Perfomance/Race |
| FuelType             |
| RPMLimit             |       Fuel Cut Off       |
| Headers              |
| ExhaustCount         |
| Cat                  |
| Muffler1             |
| Muffler2             |
| QualityBottomEnd     |
| QualityTopEnd        |
| QualityAspiration    |
| QualityFuelSystem    |
| QualityExhaust       |