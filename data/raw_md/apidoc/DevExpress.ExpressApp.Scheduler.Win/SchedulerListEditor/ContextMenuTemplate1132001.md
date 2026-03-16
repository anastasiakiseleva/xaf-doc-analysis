---
uid: DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor.ContextMenuTemplate
name: ContextMenuTemplate
type: Property
summary: Returns a null reference.
syntax:
  content: public override IContextMenuTemplate ContextMenuTemplate { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.IContextMenuTemplate
    description: "`null`"
seealso: []
---
Since the scheduling control used by the `SchedulerListEditor` provides its own context menu, the `ContextMenuTemplate` property always returns `null`.

For information on the context menu templates, refer to the [ListEditor.ContextMenuTemplate](xref:DevExpress.ExpressApp.Editors.ListEditor.ContextMenuTemplate) property description.