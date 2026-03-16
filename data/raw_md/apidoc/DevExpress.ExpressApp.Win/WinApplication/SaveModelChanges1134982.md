---
uid: DevExpress.ExpressApp.Win.WinApplication.SaveModelChanges
name: SaveModelChanges()
type: Method
summary: Saves the [Application Model](xref:112580) changes made by an end-user, up to the current moment, to the storage (_Model.User.xafml_ file, by default).
syntax:
  content: public override void SaveModelChanges()
seealso: []
---
Overrides the [XafApplication.SaveModelChanges](xref:DevExpress.ExpressApp.XafApplication.SaveModelChanges) method. By default, this method is called when the application is closed. So, all the changes made from the application start until the end are saved to the _Model.User.xafml_ file. You can call this method at any time during the application run. For example, you can implement an [Action](xref:112622) that allows end-users to save the changes made up to the current moment. To prevent saving changes at the end of the application run, set the [WinApplication.IgnoreUserModelDiffs](xref:DevExpress.ExpressApp.Win.WinApplication.IgnoreUserModelDiffs) property to **true**.

You can save user changes to another storage; for example, to the database. For this purpose, handle the [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) event.