---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1.OptimisticLockDetection
name: OptimisticLockDetection
type: Property
summary: Specifies whether XAF identifies conflicting changes by using just the object's concurrency token or by assessing all object properties.
syntax:
  content: |-
    [DefaultValue(OptimisticLockDetection.AllFields)]
    public OptimisticLockDetection OptimisticLockDetection { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.OptimisticLockDetection
    description: A conflict detection strategy.
seealso: []
---
For detailed information, refer to the following topic: [](xref:405384).