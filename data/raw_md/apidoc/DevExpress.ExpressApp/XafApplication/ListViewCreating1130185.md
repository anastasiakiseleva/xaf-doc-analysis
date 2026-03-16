---
uid: DevExpress.ExpressApp.XafApplication.ListViewCreating
name: ListViewCreating
type: Event
summary: Occurs when creating a List View.
syntax:
  content: public event EventHandler<ListViewCreatingEventArgs> ListViewCreating
seealso: []
---
Handle this event to provide a custom List View instead of a default one. Use the handler's [ListViewCreatingEventArgs.View](xref:DevExpress.ExpressApp.ListViewCreatingEventArgs.View) parameter to get information on the created List View. To do this, use the application's [XafApplication.FindModelView](xref:DevExpress.ExpressApp.XafApplication.FindModelView(System.String)) method passing the View ID as a parameter. To create a List View, use the collection source passed as the handler's [ListViewCreatingEventArgs.CollectionSource](xref:DevExpress.ExpressApp.ListViewCreatingEventArgs.CollectionSource) parameter. To specify whether the List View is root, use the handler's [ViewCreatingEventArgs.IsRoot](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.IsRoot) parameter.

The following example demonstrates how to handle the **ListViewCreating** event:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Model;

namespace MySolution.Module {
    public sealed partial class MySolutionModule : ModuleBase {
        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.ListViewCreating += application_ListViewCreating;
        }
        void application_ListViewCreating(object sender, ListViewCreatingEventArgs e) {
            IModelListView modeListView = ((XafApplication)sender).FindModelView(e.ViewID) as IModelListView;
            if (modeListView != null) {
                modeListView.MasterDetailMode = MasterDetailMode.ListViewAndDetailView;
            }
        }
    }
}
```
***

[`ModuleBase`]: xref:DevExpress.ExpressApp.ModuleBase
[`Setup`]: xref:DevExpress.ExpressApp.ModuleBase.Setup(DevExpress.ExpressApp.XafApplication)
[`ListViewCreatingEventArgs`]: xref:DevExpress.ExpressApp.ListViewCreatingEventArgs
[`XafApplication`]: xref:DevExpress.ExpressApp.XafApplication
[`FindModelView`]: xref:DevExpress.ExpressApp.XafApplication.FindModelView(System.String)
[`IModelListView`]: xref:DevExpress.ExpressApp.Model.IModelListView
[`/\.(MasterDetailMode)/`]: xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode
[`ListViewAndDetailView`]: xref:DevExpress.ExpressApp.MasterDetailMode.ListViewAndDetailView
[`ViewID`]: xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID