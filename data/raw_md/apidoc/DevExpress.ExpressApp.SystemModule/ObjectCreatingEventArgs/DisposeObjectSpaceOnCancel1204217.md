---
uid: DevExpress.ExpressApp.SystemModule.ObjectCreatingEventArgs.DisposeObjectSpaceOnCancel
name: DisposeObjectSpaceOnCancel
type: Property
summary: Specified whether or not an Object Space should be disposed on canceling a new object creation.
syntax:
  content: public bool DisposeObjectSpaceOnCancel { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if an Object Space should be disposed on canceling a new object creation, otherwise, **false**.'
seealso: []
---
Set this argument to **true** only when the [ObjectCreatingEventArgs.Cancel](xref:DevExpress.ExpressApp.SystemModule.ObjectCreatingEventArgs.Cancel) argument is set to **true**.