---
uid: DevExpress.ExpressApp.Editors.ListEditor
name: ListEditor
type: Class
summary: The base class for [List Editors](xref:113189).
syntax:
  content: 'public abstract class ListEditor : IDisposable, IProtectedContentEditor, IServiceProviderClient'
seealso:
- linkId: DevExpress.ExpressApp.Editors.ListEditor._members
  altText: ListEditor Members
- linkId: "113189"
- linkId: DevExpress.ExpressApp.Editors.ListEditorAttribute
- linkId: DevExpress.ExpressApp.Editors.IComplexListEditor
---
List Views are visualized by means of List Editors. A List Editor has a control that is used to display an object collection supplied by a List View. The List Editor handles binding of its control and supports interaction between the List View and the control.

The List Editor that represents a specific List View can be accessed using the [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) property. The following code snippet demonstrates how to do this by handling the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) and [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) events:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.XtraGrid;
//...
public partial class MyController : ViewController {
    public MyController() {
        TargetViewType = ViewType.ListView;
        Activated += MyController_Activated;
        ViewControlsCreated += MyController_ViewControlsCreated;
    }
    private void MyController_Activated(object sender, EventArgs e) {
        ListEditor listEditor = ((ListView)View).Editor;
        //Do what is required with the List Editor            
    }
    void MyController_ViewControlsCreated(object sender, EventArgs e) {
        ListEditor listEditor = ((ListView)View).Editor;
        GridControl gridControl = (GridControl)listEditor.Control;
        //Do what is required with the List Editor's control
    }
}
```
***

To display List Views XAF uses @DevExpress.ExpressApp.Win.Editors.GridListEditor in WinForms applications and @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor in Blazor applications.

You can use the `ListEditor` class and its descendant to implement custom List Editors. When deriving from the `ListEditor` class, you can override the following protected members that are not described in the documentation:

| Member |  Description |
|---|---|
| `AssignDataSourceToControl` | Called in the @DevExpress.ExpressApp.Editors.ListEditor.CreateControls method and the @DevExpress.ExpressApp.Editors.ListEditor.DataSource property setter. <br/> This method is abstract. Override it to assign the current List Editor's data source to the control. |
| `CreateControlsCore` | Called in the @DevExpress.ExpressApp.Editors.ListEditor.CreateControls method. <br/> This method is abstract. Override it to instantiate the List Editor's control. |
| `OnAllowEditChanged` | Called in the @DevExpress.ExpressApp.Editors.ListEditor.AllowEdit property setter. <br/> Raises the @DevExpress.ExpressApp.Editors.ListEditor.AllowEditChanged event. Call this method after the List Editor's edit mode has changed. |
| `OnFocusedObjectChanging` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.FocusedObjectChanging event. Call this method before the focused object is changed in the List Editor's control. |
| `OnFocusedObjectChanged` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.FocusedObjectChanged event. Call this method after the focused object is changed in the List Editor's control. |
| `OnNewObjectAdding` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.NewObjectAdding event. Call this method before a new object is created in the List Editor's control. |
| `OnNewObjectCanceled` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.NewObjectCanceled event. Call this method after creation of a new object is canceled in the List Editor's control. |
| `OnNewObjectCreated` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.NewObjectCreated event. Call this method after a new object is created in the List Editor's control. |
| `OnProcessSelectedItem` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.ProcessSelectedItem event. Call this method when an object is selected in the List Editor's control and an end-user presses Enter or double-clicks the object. |
| `OnSelectionChanged` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.SelectionChanged event. Call this method after the selection is changed in the List Editor's control. |
| `OnSelectionTypeChanged` | Raises the @DevExpress.ExpressApp.Editors.ListEditor.SelectionTypeChanged event. Call this method after the List Editor's supported selection type is changed. |

Typical implementation of the `ListEditor` class' descendants comprises the following steps:

1. Override the `CreateControlsCore` method. Create and configure an instance of the control that will represent a List View in a UI. Handle the control's events to call the following methods:
    - `OnProcessSelectedItem`
    - `OnSelectionChanged`
    - `OnFocusedObjectChanging`
    - `OnFocusedObjectChanged`
    - `OnNewObjectAdding`
    - `OnNewObjectCanceled`
    - `OnNewObjectCreated`
2. Override the `AssignDataSourceToControl` method. Assign the List Editor's data source to its control.
3. Override the @DevExpress.ExpressApp.Editors.ListEditor.Refresh method. Refresh data in the List Editor's control.
4. Override the @DevExpress.ExpressApp.Editors.ListEditor.RequiredProperties property. Return  business class' property names that are used by the List Editor when displaying objects. These properties are treated as displayable if a List View's data source is derived from the [](xref:DevExpress.Xpo.XPBaseCollection).
5. Override the @DevExpress.ExpressApp.Editors.ListEditor.SelectionType property. Return the selection type supported by the List Editor's control.
6. Override the @DevExpress.ExpressApp.Editors.ListEditor.GetSelectedObjects method. Return a list of the selected objects.
7. Override the @DevExpress.ExpressApp.Editors.ListEditor.FocusedObject method.  Get and set the control's focused object.
8. If the custom List Editor does not support [List View data access mode](xref:113683), override the @DevExpress.ExpressApp.Editors.ListEditor.SupportsDataAccessMode(DevExpress.ExpressApp.CollectionSourceDataAccessMode) property. It is also recommended that you implement a custom generator updater to disable unsupported modes for List Views visualized by the custom List Editor.
9. Modify the constructor to instantiate the control that will represent the List Editor's pop-up menu. This control must implement the `IDXPopupMenuHolder` interface to support XAF architecture. Override the @DevExpress.ExpressApp.Editors.ListEditor.ContextMenuTemplate property to return the created instance of the control.
10. Mark the custom List Editor with the [](xref:DevExpress.ExpressApp.Editors.ListEditorAttribute).

> [!NOTE]
> * To support the export functionality of the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) Controller, implement the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface in your custom List Editor.
> * To support the [RecordsNavigationController.PreviousObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.PreviousObjectAction) and [RecordsNavigationController.NextObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.NextObjectAction) Actions, implement the `IControlOrderProvider` interface in your custom List Editor.

For an example of a List Editor derived from the `ListEditor` class, refer to the following topics:

* [How to: Implement a Custom WinForms List Editor](xref:112659)
* [How to: Support a Context Menu for a Custom WinForms List Editor](xref:112660)
