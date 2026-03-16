---
uid: DevExpress.ExpressApp.Win.IModelOptionsTabbedMdiLayout.RestoreTabbedMdiLayout
name: RestoreTabbedMdiLayout
type: Property
summary: Indicates whether to restore the tabs arrangement when starting an MDI application.
syntax:
  content: |-
    [DefaultValue(true)]
    bool RestoreTabbedMdiLayout { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the tabs arrangement must be restored; otherwise, **false**.'
seealso: []
---
When an [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) is used by a Windows Forms application, and this strategy shows Views in the tabbed mode (see [MdiShowViewStrategy.MdiMode](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy.MdiMode)), consider whether you need to save the tabs arrangement when closing the application and restore them when starting the application again. To set this option, use the **RestoreTabbedMdiLayout** property of the **Options** node in the Model Editor.