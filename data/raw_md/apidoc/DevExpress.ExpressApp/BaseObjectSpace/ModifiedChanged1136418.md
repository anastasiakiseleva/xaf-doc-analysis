---
uid: DevExpress.ExpressApp.BaseObjectSpace.ModifiedChanged
name: ModifiedChanged
type: Event
summary: Occurs when the current Object Space's [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified) state is changed.
syntax:
  content: public event EventHandler ModifiedChanged
seealso: []
---
An Object Space is considered modified when at least one persistent object belonging to it is changed (created, modified or deleted). This state is in effect until the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method is called. The [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified) property specifies whether the Object Space is modified. After its value is changed, the **ModifiedChanged** event is raised. Handle this event to execute custom code.

[comment]: <> (<\!--<para>However, it is already handled internally to change <%UrlDocument$112622#Action%> states in dependence of the <see cref="P:DevExpress.ExpressApp.BaseObjectSpace.IsModified"/> property value.</para>-->)