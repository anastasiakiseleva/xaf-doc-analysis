---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.ModuleInfoType
name: ModuleInfoType
type: Property
summary: Gets the type of the class whose objects are persisted to the `ModuleInfo` table in the database.
syntax:
  content: public Type ModuleInfoType { get; }
  parameters: []
  return:
    type: System.Type
    description: A type of the class corresponding to the `ModuleInfo` database table.
seealso: []
---
When the [XafApplication.CheckCompatibilityType](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibilityType) or [XPObjectSpaceProvider.CheckCompatibilityType](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.CheckCompatibilityType) property is set to `ModuleInfo`, a **ModuleInfo** table is created in the database to check the compatibility of the application and its database. This table stores information on the modules used in the application. This information is required when checking the compatibility of the database and application.

The `ModuleInfoType` property gets the type of the class that is mapped to the `ModuleInfo` table in the database.