---
uid: DevExpress.ExpressApp.CustomCheckCompatibilityEventArgs.ObjectSpaceProvider
name: ObjectSpaceProvider
type: Property
summary: |-
  Specifies the Object Space Provider for compatibility checking. Use this parameter to create a Session or an Object Space to work with the database.
  
  Note that XAF uses the first registered Object Space Provider to pass it as the `ObjectSpaceProvider` argument. Ensure that @DevExpress.ExpressApp.NonPersistentObjectSpaceProvider is not the first registered Provider in your application.
syntax:
  content: public IObjectSpaceProvider ObjectSpaceProvider { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.IObjectSpaceProvider
    description: An [](xref:DevExpress.ExpressApp.IObjectSpaceProvider) object representing the Object Space Provider to be used for compatibility checking purposes.
seealso: []
---
