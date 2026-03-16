---
uid: DevExpress.ExpressApp.IObjectSpace.Reloaded
name: Reloaded
type: Event
summary: Occurs after the current Object Space reconnects to the database.
syntax:
  content: event EventHandler Reloaded
seealso: []
---
In the [](xref:DevExpress.ExpressApp.BaseObjectSpace) descendant, override the **BaseObjectSpace.Reload** method. Invoke the **BaseObjectSpace.OnReloaded** method in this override to raise the **Reloaded** event.

The **Reloaded** event handler updates [Action](xref:112622) states and all objects that are retrieved with the newly established connection.

[!include[<24-26><29-31>](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]