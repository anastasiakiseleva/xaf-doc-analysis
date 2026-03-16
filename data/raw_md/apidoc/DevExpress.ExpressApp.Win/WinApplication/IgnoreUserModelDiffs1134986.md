---
uid: DevExpress.ExpressApp.Win.WinApplication.IgnoreUserModelDiffs
name: IgnoreUserModelDiffs
type: Property
summary: Specifies if the user model differences are ignored.
syntax:
  content: |-
    [Browsable(false)]
    public bool IgnoreUserModelDiffs { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the user model differences are ignored, otherwise - **false**.'
seealso: []
---
This property is set to **false** by default. You can pass the "-IgnoreUserModelDiffs" command line argument, when running a Windows Forms application, and this property will be set to **true** when instantiating the [](xref:DevExpress.ExpressApp.Win.WinApplication). When set to **true**, runtime customizations are saved to the previous writable difference storage (_Model.xafml_, by default).