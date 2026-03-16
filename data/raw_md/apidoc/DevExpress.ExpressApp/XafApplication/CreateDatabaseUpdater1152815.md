---
uid: DevExpress.ExpressApp.XafApplication.CreateDatabaseUpdater(DevExpress.ExpressApp.IObjectSpaceProvider)
name: CreateDatabaseUpdater(IObjectSpaceProvider)
type: Method
summary: Creates a Database Updater for a specified Object Space Provider.
syntax:
  content: public virtual DatabaseUpdaterBase CreateDatabaseUpdater(IObjectSpaceProvider objectSpaceProvider)
  parameters:
  - id: objectSpaceProvider
    type: DevExpress.ExpressApp.IObjectSpaceProvider
    description: An [](xref:DevExpress.ExpressApp.IObjectSpaceProvider) Object Space Provider.
  return:
    type: DevExpress.ExpressApp.Updating.DatabaseUpdaterBase
    description: A **DatabaseUpdaterBase** object that handles the database update process.
seealso: []
---
The **CreateDatabaseUpdater** method triggers the [XafApplication.DatabaseUpdaterCreating](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdaterCreating) event.