---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.UnlinkAction
name: UnlinkAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController)'s **Unlink** Action.
syntax:
  content: public SimpleAction UnlinkAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Unlink** Action.
seealso: []
---
The **Unlink** Action is intended to remove required objects from a collection property displayed by a nested List View:

In a Windows Forms application:

![LinkUnlink_Win_3](~/images/linkunlink_win_3115950.png)

This Action's `Execute` event is handled by the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController)'s `Unlink` protected method. If you need to modify the way this Action is executed, inherit from this Controller and override the `Unlink` method. Alternatively, handle the Action's `Execute` event in a custom Controller.

When implementing a custom Controller to modify the behavior of the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController) or its **Unlink** Action, you may have to determine whether the current List View displays a collection property in a Detail View. To accomplish this, use one of the following criteria:

* Use the List View's ID:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    //...
    if (View is ListView && View.Id == "MyBusinessClass1_MyBusinessClass2_ListView") {
      //...
    }
    //...
    ```
    ***
* Use the List View's CollectionSource type:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    //...
    if(View is ListView && !View.IsRoot && 
          ((ListView)View).CollectionSource is PropertyCollectionSource) {
       //...
    }
    //...
    ```
    ***

By default, the **Unlink** Action is active under the following conditions:

* If the current List View's collection source is of the `PropertyCollectionSource` type for List Views displaying collection properties.
* The current List View is not read-only.
* The applied [Security System](xref:113366) does not prohibit the current View's access.
* The collection property represents the Many-to-Many relationship's part or it represents the One-to-Many relationship's Many part, being non-aggregated.

The **Unlink** Action is enabled when changes have been made to the current object. However, it can be disabled, because the current user does not have permission to change the current object.

To ascertain why the **Unlink** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **Unlink** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).