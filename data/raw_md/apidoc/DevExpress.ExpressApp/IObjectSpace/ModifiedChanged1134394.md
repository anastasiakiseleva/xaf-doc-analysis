---
uid: DevExpress.ExpressApp.IObjectSpace.ModifiedChanged
name: ModifiedChanged
type: Event
summary: Occurs when the current Object Space's [IObjectSpace.IsModified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified) state is changed.
syntax:
  content: event EventHandler ModifiedChanged
seealso: []
---
In the [](xref:DevExpress.ExpressApp.BaseObjectSpace) descendant, you don't have to raise the **ModifiedChanged** event. It is raised in the protected **BaseObjectSpace.SetIsModified** method after the [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified) property has changed.

Handle this event to execute custom code when the Object Space's Modified state is changed. However, it is already handled internally to change [Actions](xref:112622) states in dependence of the [IObjectSpace.IsModified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified) property value.

[!include[](~/templates/modifiedchanged_code_snippet.md)]