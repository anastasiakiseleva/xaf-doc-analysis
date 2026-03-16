---
uid: DevExpress.ExpressApp.XafApplication.SaveModelChanges
name: SaveModelChanges()
type: Method
summary: Saves the changes made by an end-user, up to the current moment, to the differences storage.
syntax:
  content: public virtual void SaveModelChanges()
seealso: []
---

XAF calls this method when it needs to save user settings. You can call it at any time during the application run. For example, you can implement an [Action](xref:112622) that allows users to save the changes.

You can save user changes to another storage; for example, to the database. For this purpose, handle the [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) event.

## Example

[!include[save-app-state-example](~/templates/save-app-state-example.md)]
