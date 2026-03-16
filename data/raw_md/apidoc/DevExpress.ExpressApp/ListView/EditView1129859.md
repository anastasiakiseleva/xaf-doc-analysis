---
uid: DevExpress.ExpressApp.ListView.EditView
name: EditView
type: Property
summary: Provides access to the Detail View displayed together with a List View.
syntax:
  content: public DetailView EditView { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DetailView
    description: The [](xref:DevExpress.ExpressApp.DetailView) object representing a detail view displayed with the current list view.
seealso:
- linkId: DevExpress.ExpressApp.ListView.EditViewCreated
---
XAF displays a List View together with a Detail View when the [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode) property of the appropriate [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node is set to **ListViewAndDetailView**. In this scenario, the Detail View demonstrates the object currently focused in the List View's List Editor:

![Tutorial_UIC_Lesson17_2](~/images/tutorial_uic_lesson17_2115512.png)

The **EditView** property allows you to customize this Detail View and access its View Items. To do this, you can use the following properties: [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items), [CompositeView.LayoutManager](xref:DevExpress.ExpressApp.CompositeView.LayoutManager), and [DetailView.Model](xref:DevExpress.ExpressApp.DetailView.Model).

The following example demonstrates how to access and customize a Property Editor of a Detail View in **MasterDetailMode**:

# [C#](#tab/tabid-csharp)

```csharp{10,11}
using System.Linq;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.SystemModule;

namespace MySolution.Module.Controllers {
    public class UpdateShortcutViewController : ViewController<ListView> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if(View.EditView != null) {
                ListPropertyEditor detailsPropertyEditor = View.EditView.Items.OfType<ListPropertyEditor>().FirstOrDefault();
                if(detailsPropertyEditor?.Frame != null) {
                    NewObjectViewController newObjectViewController = detailsPropertyEditor.Frame.GetController<NewObjectViewController>();
                    if(newObjectViewController != null) {
                        newObjectViewController.NewObjectAction.Shortcut = "CtrlI";
                    }
                }
            }
        }
    }
}
```
***
