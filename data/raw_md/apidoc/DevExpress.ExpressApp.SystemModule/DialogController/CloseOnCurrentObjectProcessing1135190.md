---
uid: DevExpress.ExpressApp.SystemModule.DialogController.CloseOnCurrentObjectProcessing
name: CloseOnCurrentObjectProcessing
type: Property
summary: Specifies whether or not the dialog is closed when a row in the List Editor is clicked.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool CloseOnCurrentObjectProcessing { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a popup dialog is closed when a row in the List Editor is clicked; otherwise - **false**.'
seealso: []
---
When set to false, the [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction) Action is executed when a row is clicked.