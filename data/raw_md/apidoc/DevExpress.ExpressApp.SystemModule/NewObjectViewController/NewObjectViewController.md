---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController
name: NewObjectViewController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **New** [Action](xref:112622).
syntax:
  content: 'public class NewObjectViewController : ViewController, IComparer<ChoiceActionItem>, IModelExtender, ICreateObjectActionProvider'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.NewObjectViewController._members
  altText: NewObjectViewController Members
- linkId: DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectActionItemListMode
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t326296/how-to-remove-or-hide-the-base-class-from-the-new-action-s-items-list
  altText: How to remove or hide the base class from the New Action's items list
---
`NewObjectViewController` displays the **New** Action.

ASP.NET Core Blazor
:   ![|NewObjectViewController New Action in ASP.NET Core Blazor, DevExpress|](~/images/blazor-newobjectviewcontroller-devexpress.png)

Windows Forms
:   ![|NewObjectViewController New Action in Windows Forms, DevExpress|](~/images/winnewobjectviewcontroller_new115926.png)

>[!NOTE]
> In ASP.NET Core Blazor, the **New** Action is not available in Detail Views.

[!include[new-action-hidden-in-many-to-many-collection](~/templates/new-action-hidden-in-many-to-many-collection.md)]

For more information about the **New** Action, refer to the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) property description.

To customize the default behavior of the **New** Action, you can inherit from this Controller or subscribe to its events. In addition, you can access the Action to modify its behavior.

| Platform | Descendant |
| -------- | ---------- |
| ASP.NET Core Blazor | [](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorModificationsController) |
| Windows Forms | [](xref:DevExpress.ExpressApp.Win.SystemModule.WinModificationsController) |

If you need to inherit from the **NewObjectViewController**, the following protected virtual methods are available:

{|
|-

! Method
! Trigger Action
! Description
|-

| `OnObjectCreating`
| After the `New` method call, but before the object is created.
| Raises the [NewObjectViewController.ObjectCreating](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreating) event.
|-

| `OnCustomAddObjectToCollection`
| After the object has been created, but before it is added to the object collection.
| Raises the [NewObjectViewController.CustomAddObjectToCollection](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CustomAddObjectToCollection) event.
|-

| `OnObjectCreated`
| After the new object has been created and added to the object collection. If the `ObjectCreatedEventArgs.ShowDetailView` property is set to `true`, a Detail View with the new object is invoked after calling this method.
| Raises the [NewObjectViewController.ObjectCreated](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreated) event.
|-

| `New`
| The **New** Action's [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event.
| * Creates a new object using the handler's `ObjectCreatedEventArgs` properties.
* Adds the new object to the collection source of the Controller's current List View. If the current View represents a Detail View, the object is added to the List View from which the Detail View was added. If you need to add the new object in a custom way, handle the [NewObjectViewController.CustomAddObjectToCollection](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CustomAddObjectToCollection) event and set the handler's `ProcessNewObjectEventArgs.Handled` parameter to `false`.
* Shows a Detail View with the new object, if the [NewObjectViewController.ObjectCreating](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreating) event handler's `ObjectCreatingArgs.ShowDetailView` parameter is set to `true`.
|-

| `UpdateActionState`
| `NewObjectViewController` activation, changes in the current ListView's CollectionSource, and changes in the current View's [AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) property. In platform-specific Controllers, this method populates the New Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection.
| &nbsp;
|}

To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property (see [How to: Detect a Lookup List View in Code](xref:112908)). If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information about the `NewObjectViewController` and its `New` Action is available in the [Application Model](xref:112580). To access it, use the [Model Editor](xref:112582).
