---
uid: DevExpress.ExpressApp.ListView.CreateCustomCurrentObjectDetailView
name: CreateCustomCurrentObjectDetailView
type: Event
summary: Occurs when the current List View is updated, and when its current object is changed.
syntax:
  content: public event EventHandler<CreateCustomCurrentObjectDetailViewEventArgs> CreateCustomCurrentObjectDetailView
seealso: []
---
You can display a Detail View to the right or at the bottom of a List View. This Detail View displays the object selected in the List View. To enable this mode, set the [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode) property of the [Application Model](xref:112580)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node to `ListViewAndDetailView`. To display an alternate Detail View, you can use one of the following techniques:

* Specify the [IModelListView.MasterDetailView](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailView) property in the Model Editor. Note that when both `MasterDetailView` and `DetailView` properties are unspecified, XAF automatically determines the Detail View based on the type of the object created or edited in the List View (the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) value specified for a specific object type is used).
* Handle the `CreateCustomCurrentObjectDetailView` event and specify the handler's `DetailView` or `DetailViewId` parameter. Note that when you specify the `DetailViewId` parameter, XAF creates a Detail View with the passed identifier automatically.

When you use the second technique, you can implement custom logic to choose a Detail View and use the following handler's parameters to access and customize additional details:

@DevExpress.ExpressApp.CreateCustomCurrentObjectDetailViewEventArgs.ListViewCurrentObject 
:   Gets the currently selected object. 
@DevExpress.ExpressApp.CreateCustomCurrentObjectDetailViewEventArgs.ListViewObjectType 
:   Gets the type of the current List View's objects. 
@DevExpress.ExpressApp.CreateCustomCurrentObjectDetailViewEventArgs.CurrentDetailView
:   Gets the current Detail View.  
@DevExpress.ExpressApp.CreateCustomCurrentObjectDetailViewEventArgs.ListViewModel
:   Gets the Detail View currently set for the current List View in the Application Model (see the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node's [IModelListView.DetailView](xref:DevExpress.ExpressApp.Model.IModelListView.DetailView) property).

The following code snippet handles the `CreateCustomCurrentObjectDetailView` event for the following scenario:

Assume you created a custom Detail View node in the Application Model's _Views_ node ("MyCustomDetailView" in this example) and enabled **ListViewAndDetailView** mode for the **Person** List View. You want to display a Detail View near the `Employee` List View but do not want to use this Detail View to edit the List View's object in a separate window. You cannot set the `DetailViewID` property of the **Employee_ListView** node to your Detail View because, in this case, XAF uses this Detail View to edit an object in a separate window.

1. Create a custom Detail View node in the Application Model's _Views_ node ("MyCustomDetailView" in this example) and enable `ListViewAndDetailView` mode for the `Employee` List View.
3. Handle the `CreateCustomCurrentObjectDetailView` event and set the `DetailViewId` parameter to your Detail View in one of the following places:

* [Controller](xref:112621) 
* _MySolution.Win\WinApplication.cs_ file in WinForms applications
* _MySolution.Blazor.Server\BlazorApplication.cs_ file in ASP.NET Core Blazor applications

# [C# (WinForms)](#tab/tabid-win)
```csharp
public class MySolutionWinApplication : WinApplication {
    public MySolutionWinApplication() {
        ListViewCreated += MySolutionWinApplication_ListViewCreated;
    }
    private static void MySolutionWinApplication_ListViewCreated(object sender, ListViewCreatedEventArgs e) {
        if (e.ListView.Id == "Employee_ListView"){
            e.ListView.CreateCustomCurrentObjectDetailView += ListView_CreateCustomCurrentObjectDetailView;
        }
    }
    private static void ListView_CreateCustomCurrentObjectDetailView(object sender,
            CreateCustomCurrentObjectDetailViewEventArgs e) {
        e.DetailViewId = "MyCustomDetailView";
    }
}
```
# [C# (Blazor)](#tab/tabid-blazor)
```csharp
public class MySolutionBlazorApplication : BlazorApplication {
    public MySolutionBlazorApplication() {
        ListViewCreated += MySolutionBlazorApplication_ListViewCreated;
    }
    private static void MySolutionBlazorApplication_ListViewCreated(object sender, ListViewCreatedEventArgs e) {
        if (e.ListView.Id == "Employee_ListView"){
            e.ListView.CreateCustomCurrentObjectDetailView += ListView_CreateCustomCurrentObjectDetailView;
        }
    }
    private static void ListView_CreateCustomCurrentObjectDetailView(object sender,
            CreateCustomCurrentObjectDetailViewEventArgs e) {
        e.DetailViewId = "MyCustomDetailView";
    }
}
```
***
