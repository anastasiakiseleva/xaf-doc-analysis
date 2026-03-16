---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.TreeList
name: TreeList
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)'s control.
syntax:
  content: public TreeList TreeList { get; }
  parameters: []
  return:
    type: DevExpress.XtraTreeList.TreeList
    description: A [](xref:DevExpress.XtraTreeList.TreeList) object that is the **TreeListEditor**'s control.
seealso: []
---
You can use this property to customize the List Editor's control. Generally, the recommended place to do this is a custom [Controller](xref:112621)'s [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) event handler. The [](xref:402154) article illustrates this approach.

If you need to execute a custom action after a List Editor's control has been created, handle the [ListEditor.ControlsCreated](xref:DevExpress.ExpressApp.Editors.ListEditor.ControlsCreated) event.