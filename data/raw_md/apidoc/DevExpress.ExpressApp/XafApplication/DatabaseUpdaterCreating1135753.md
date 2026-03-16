---
uid: DevExpress.ExpressApp.XafApplication.DatabaseUpdaterCreating
name: DatabaseUpdaterCreating
type: Event
summary: Occurs when creating a database updater.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<DatabaseUpdaterEventArgs> DatabaseUpdaterCreating
seealso: []
---
This event is intended for internal use. To manually update the application's database, handle the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event, and use the database updater, accessible via the handler's [DatabaseVersionMismatchEventArgs.Updater](xref:DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs.Updater) parameter.