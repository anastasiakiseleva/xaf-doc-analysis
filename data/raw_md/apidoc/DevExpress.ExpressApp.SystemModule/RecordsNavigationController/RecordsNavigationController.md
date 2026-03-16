---
uid: DevExpress.ExpressApp.SystemModule.RecordsNavigationController
name: RecordsNavigationController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **Previous Object** and **Next Object** [Actions](xref:112622).
syntax:
  content: 'public class RecordsNavigationController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.RecordsNavigationController._members
  altText: RecordsNavigationController Members
---
The `RecordsNavigationController` displays the **Previous Object** and **Next Object** Actions.

ASP.NET Core Blazor

:   ![|ASP.NET Core Blazor RecordsNavigationController Actions, DevExpress|](~/images/blazorrecordsnavigationcontroller.png)

Windows Forms

:   ![|Windows Forms RecordsNavigationController Actions, DevExpress|](~/images/recordsnavigationcontroller_actions_win115934.png)

To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information about the `RecordsNavigationController` and its **Previous Object** and **Next Object** Actions is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access the node, use the [Model Editor](xref:112582).


### Order Providers

XAF activates `RecordsNavigationController` for all Views. This controller uses an `OrderProviderSource` to obtain an `OrderProvider`. These objects determine which collection to use and how to fetch the required objects from the collection when a user executes **Next Object** or **Previous Object** Actions.

Order Providers implement the following members of the `IOrderProvider` interface: `GetObjectByIndex` and `GetOrderedObjects`. XAF supports several Order Providers that implement either the `IObjectOrderProvider` or `IKeyOrderProvider` interface. Both interfaces are `IOrderProvider` interface descendants. The `IObjectOrderProvider` interface includes the `GetIndexByObject` method, while the `IKeyOrderProvider` includes the `GetIndexByObjectKey` method.

#### ListEditorOrderProvider

Implements `IObjectOrderProvider`.

Works with a List View that you pass to it in its constructor. Uses the corresponding methods of its `ControlOrderProvider` - the List View's Editor that implements the `IControlOrderProvider` interface. The built-in [List Editors](xref:113189) implement this interface ([](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor), [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor), [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase), and [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)). If the current editor does not implement these the required interface methods, XAF uses `DefaultOrderProvider`. This Order Provider is passed to the `ListEditorOrderProvider` in its constructor.

Used when XAF activates the `RecordsNavigationController` for a List View.

#### DefaultOrderProvider

Implements `IObjectOrderProvider`.

Works with any View that you pass to it in its constructor. In case of a List View, this Order Provider uses the `DataSource` of the `ListEditor`. In case of a Detail View, the `GetObjectByIndex` and `GetOrderedObjects` methods return `null`, and the `GetIndexByObject` method returns `-1`.

Used when XAF activates the `RecordsNavigationController` for a List View, but the View's Editor does not implement the `IControlOrderProvider` interface or when XAF activates the `RecordsNavigationController` for a Detail View.

#### NullOrderProvider

Implements `IObjectOrderProvider`.

The `GetObjectByIndex` and `GetOrderedObjects` methods return `null`, and the `GetIndexByObject` method returns `-1`.

Used by the `ListEditorOrderProvider` when the specified `DefaultOrderProvider` is `null`.

#### StandaloneOrderProvider

Implements `IKeyOrderProvider`.

Works with the ordered list of objects that you pass to it in its constructor.

Used when the current `RecordsNavigationController` is deactivated. The previously used Order Provider passes the objects it worked with to this Order Provider. This is required to support a Detail View's `RecordsNavigationController` that uses the Order Provider of a List View's `RecordsNavigationController`.

By default, when XAF activates the `RecordsNavigationController` for a List View, it passes this View to the Order Provider. The **Next Object** and **Previous Object** Actions can then navigate through the List View's objects. When the `RecordsNavigationController` is activated for a standalone Detail View, there is no collection to navigate through, so the **Next Object** and **Previous Object** Actions are disabled. However, you can also invoke a Detail View in a separate [Window](xref:112608) to display objects selected in a List View. `RecordsNavigationController` handles this scenario in a special manner. The `OrderProviderSource` used by the List View's `RecordsNavigationController` is assigned to the [RecordsNavigationController.OrderProviderSource](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.OrderProviderSource) property of the Detail View's `RecordsNavigationController`. Therefore, XAF uses the List View's collection for navigation in the Detail View, since the Order Provider works with the List View.

You can inherit from this Controller or subscribe to its events to modify its behavior. In addition, you can use the [RecordsNavigationController.NextObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.NextObjectAction) and [RecordsNavigationController.PreviousObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.PreviousObjectAction) properties to access the Controller's **Next Object** and **Previous Object** Actions and modify their behavior.

### RecordsNavigationController Behavior Customization

If you need to override the behavior of `RecordsNavigationController`, inherit from one of the following classes:

ASP.NET Core Blazor

:   `DevExpress.ExpressApp.Blazor.SystemModule.BlazorRecordsNavigationController`

Windows Forms

:   `DevExpress.ExpressApp.SystemModule.RecordsNavigationController`

You can override the following methods:

{|
|-

! Method
! What triggers this method?
! Description
|-

| `MoveToNext`
| The **Next Object** Action.
| The **Next Object** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. It obtains the current object's index in the collection, finds the following object, and sets it as the current object for the Controller's current View.
|-

| `MoveToPrevious`
| The **Previous Object** Action.
| The Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. It obtains the current object's index in the collection, finds the previous object, and sets it as the current object for the Controller's current View.
|-

| `OnViewShowing`
| The [XafApplication.ViewShowing](xref:DevExpress.ExpressApp.XafApplication.ViewShowing) event.
| If the target View is a Detail View displayed in a separate Window, this method creates an `OrderProviderInitializer` and passes the [RecordsNavigationController.OrderProviderSource](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.OrderProviderSource) to it. After XAF displays the Detail View, this `OrderProviderInitializer` sets the `OrderProviderSource` for the View's `RecordsNavigationController`. This is a requirement for the scenario described in the [StandaloneOrderProvider](#standaloneorderprovider) section above.
|-

| `CreateDefaultOrderProvider`
| `RecordsNavigationController` activation.
| Returns a newly created `DefaultOrderProvider`.
|-

| `UpdateActionsState`
| * `RecordsNavigationController` activation
* [RecordsNavigationController.OrderProviderSource](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.OrderProviderSource) property change

* [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged) event
* [View.SelectionChanged](xref:DevExpress.ExpressApp.View.SelectionChanged) event
* [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed) event
| Updates the **Next Object** and **Previous Object** Action's `Active` and `Enabled` state.
|}

### Support in List Editors

`RecordsNavigationController` works seamlessly with all the built-in list editors in all [List View data access modes](xref:113683). For custom List Editors in non-client modes, you should implement the `IControlOrderProvider` interface. Refer to the following topics for implementation examples:

* [How to: Use a Custom Component to Implement List Editor (Blazor)](xref:403258#full-list-editor-code)
* [How to: Implement a Custom List Editor (WinForms)](xref:112659)