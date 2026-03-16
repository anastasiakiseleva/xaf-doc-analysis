---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectReloaded
name: ObjectReloaded
type: Event
summary: Occurs after an object is reloaded from the database.
syntax:
  content: event EventHandler<ObjectManipulatingEventArgs> ObjectReloaded
seealso: []
---
In the @DevExpress.ExpressApp.BaseObjectSpace descendant, invoke the **BaseObjectSpace.OnObjectReloaded** method to raise the **ObjectReloaded** event.

[!include[objectreloaded-codesnippet](~/templates/objectreloaded-codesnippet.md)]
