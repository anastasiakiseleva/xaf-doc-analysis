---
uid: DevExpress.ExpressApp.XafApplication.CheckCompatibility
name: CheckCompatibility()
type: Method
summary: Checks whether the application and database are compatible, and if not, tries to make them compatible.
syntax:
  content: public void CheckCompatibility()
seealso: []
---
If the application is being run in the debugging mode, this method raises the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event. Otherwise, the database and application compatibility is checked. If the database cannot be opened or its version is older than the actual application version, the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event is raised. You can override this by handling the [XafApplication.CustomCheckCompatibility](xref:DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility) event.

Generally, you do not need to use this method. It is called everywhere where the database and application compatibility must be checked. For instance, when you need to create an Object Space, use the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method, which calls the **CheckCompatibility** method before creating a new Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)).