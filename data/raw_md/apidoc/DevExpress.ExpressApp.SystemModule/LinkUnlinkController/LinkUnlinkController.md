---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController
name: LinkUnlinkController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **Link** and **Unlink** [Actions](xref:112622).
syntax:
  content: 'public class LinkUnlinkController : ViewController, IModelExtender'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.LinkUnlinkController._members
  altText: LinkUnlinkController Members
---
The `LinkUnlinkController` displays the **Link** and **Unlink** Actions.

In a Windows Forms application:

![LinkUnlinkController_Actions_Win](~/images/linkunlinkcontroller_actions_win115944.png)

For details on the **Link** and **Unlink** Actions, refer to the description of the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) and [LinkUnlinkController.UnlinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.UnlinkAction) properties that provide access to these Actions.

To customize the default behavior of the **Link** and **Unlink** Actions, you can inherit from this Controller, or subscribe to its events. In addition, you can access the Actions to modify their behavior.

If you need to inherit from the **`LinkUnlinkController`**, the following protected virtual methods are available for overriding:

| Method | When is it called? | Description |
|---|---|---|
| `CreateLinkView` | Invoked as a result of executing the **Link** Action. | Represents the **Link** Action's [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event handler. Creates a List View for the **Link** Action's pop-up Window. This List View corresponds to the **Views** \| **View** node that is referenced by [IModelPropertyEditorLinkView.LinkView](xref:DevExpress.ExpressApp.SystemModule.IModelPropertyEditorLinkView.LinkView) property of the current List Property Editor's [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node. If this property is not specified, the current List View's node is used for creating the **Link** Action's pop-up Window. |
| `CustomizeLinkTemplate` | Invoked as a result of executing the **Link** Action. | Represents the **Link** Action's [PopupWindowShowAction.CustomizeTemplate](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizeTemplate) event handler. Adds the **Search** functionality according to the [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode) property of the current List Property Editor's [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node. |
| `Link` | Invoked as a result of executing the **Link** Action. | Represents the **Link** Action's [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) event handler. Adds the invoked List View's selected objects to the current List View. Saves changes if the [LinkUnlinkController.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.AutoCommit) property is set to `true`. |
| `Unlink` | Invoked as a result of executing the **Unlink** Action. | Represents the **Unlink** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Removes the current List View's selected objects. Saves changes if the [LinkUnlinkController.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.AutoCommit) property is set to `true`. |
| `UpdateActionsState` | Called when the `LinkUnlinkController` is activated. In addition, it is called when the current ListView's CollectionSource is changed, and when the current View's [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) and [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete) properties are changed. | Updates the **Link** and **Unlink** Actions' active state (see [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active)). |

Public members are described individually in the documentation.

This Controller is activated for the nested [List Views](xref:112611) that are displayed via the **ListPropertyEditor**. To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information on the `LinkUnlinkController` and its **Link** and **Unlink** Actions is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).