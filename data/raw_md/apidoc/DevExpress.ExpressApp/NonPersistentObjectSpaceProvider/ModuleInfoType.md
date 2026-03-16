---
uid: DevExpress.ExpressApp.NonPersistentObjectSpaceProvider.ModuleInfoType
name: ModuleInfoType
type: Property
summary: Gets the type of the class that is mapped to the **ModuleInfo** table in the database.
syntax:
  content: public Type ModuleInfoType { get; }
  parameters: []
  return:
    type: System.Type
    description: A type of class that corresponds to the **ModuleInfo** database table.
seealso: []
---
When the [XafApplication.CheckCompatibilityType](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibilityType) or [NonPersistentObjectSpaceProvider.CheckCompatibilityType](xref:DevExpress.ExpressApp.NonPersistentObjectSpaceProvider.CheckCompatibilityType) property is set to `ModuleInfo`, a **ModuleInfo** table is created in the database to check the compatibility of the application and its database. This table stores information on the modules the application uses. This information is required when checking the compatibility of the database and application