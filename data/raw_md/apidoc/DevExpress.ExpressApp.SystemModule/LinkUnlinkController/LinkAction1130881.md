---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction
name: LinkAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController)'s **Link** Action.
syntax:
  content: public PopupWindowShowAction LinkAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.PopupWindowShowAction
    description: A [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) object representing the **Link** Action.
seealso:
- linkId: "112924"
---
The **Link** Action adds the specified existing objects to a collection property displayed by a nested List View:

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor Link Action, DevExpress](~/images/xaf-link-action-blazor-devexpress.gif)
Windows Forms
:   ![XAF Windows Forms Link Action, DevExpress](~/images/linkunlink_win_1115947.png)

To show all existing objects of the current collection property's object type, a List View is created and shown in a pop-up Window. This List View is generated using information from the [Application Model](xref:112580). The node which is used as the information source is determined by the `LinkView` property of the [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node defining the current collection property:

By default, the `LinkView` property is set to the value of the `DefaultLookupListView` property of the **BOModel** | **_\<Class\>_** node, defining the collection property's object type. If the `LinkView` property is not specified, the **ListView** node used to display the collection property will be used.

To create a custom List View, handle the [LinkUnlinkController.CustomCreateLinkView](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.CustomCreateLinkView) event.

You can filter the created List View by setting a criteria for the objects to be displayed. For this purpose, use the [](xref:DevExpress.Persistent.Base.DataSourceCriteriaAttribute) for the collection property. In addition, you can provide a custom collection source for the created List View. For this purpose, use the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute). For details, refer to the [How to: Filter a Link Dialog's List View](xref:112924) topic.

The created List View appears in a pop-up [Window](xref:112608): the `LookupForm` [Template](xref:112609) in Windows Forms and `PopupWindowTemplate` in ASP.NET Core Blazor.

To customize the pop-up Window's Template, handle the [PopupWindowShowAction.CustomizeTemplate](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizeTemplate) event that occurs after assigning the Template to the Window. Use the handler's [CustomizeTemplateEventArgs.Template](xref:DevExpress.ExpressApp.CustomizeTemplateEventArgs.Template) parameter to access the Template. The `LinkUnlinkController` handles this event to add the Search functionality to the Template, if required. This functionality is activated by default in Blazor applications, or when a created List View's collection source contains more than 25 objects. This number is specified by the [IModelOptions.LookupSmallCollectionItemCount](xref:DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount) property of the [Application Model](xref:112580)'s **Options** node.

You can use other display modes for List View and the Search functionality in the Link Action's pop-up Window. To select the mode, use the `LookupEditorModeAttribute` for the collection property. Alternatively, you can use the [Model Editor](xref:112582). The value of the `LookupEditorMode` attribute's _mode_ parameter is set for the [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode) property of the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node, corresponding to the current collection property. For details, refer to [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925).

If you do not want to support the Search functionality, or need to modify it for a particular Link Action's pop-up Window, inherit from the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController) and override the `CustomizeLinkTemplate` method.

> [!NOTE]
> The `LookupEditorMode`, `DataSourceCriteria` and `DataSourceProperty` features are supported when the **Link** Action's List View is created using information from a **LookupListView** node. This node is specified by the `LinkView` property of the **DetailView** | **Items** | **PropertyEditor** node that corresponds to the current collection property.

To add an Action to the **Link** Action's pop-up Window, first determine what [Action Containers](xref:112610) can be included in the Window's Template. For information on this, refer  to the [Add Actions to a Popup Window](xref:112804) topic.

You can provide a custom list of the objects to be linked by the **Link** Action. For this purpose, handle the [LinkUnlinkController.QueryLinkObjects](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.QueryLinkObjects) event.

When implementing a custom Controller to modify the behavior of the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController) or its **Link** Action, you may have to determine whether the current List View is the one of the **Link** Action's pop-up Windows. For this purpose, use one of the following criteria:

* Use the List View's ID:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    //...
    if (View is ListView && View.Id == "MyBusinessClass_LookupListView") {
      //...
    }
    //...
    ```
    ***
* Check the context of the List View's Frame:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    //...
    if(View is ListView && Frame is Window && 
          Frame.Context == TemplateContext.LookupWindow) {
      //...
    }
    //...
    ```
    ***

The **Link** Action is active under the following conditions by default:

* If the current List View's collection source is of the `PropertyCollectionSource` type, which is satisfied for List Views that display collection properties.
* The current List View is not read-only.
* The applied [Security System](xref:113366) does not prohibit the current View's access.
* The collection property represents the Many-to-Many relationship's part; or it represents the One-to-Many relationship's Many part, being non-aggregated.

To determine why the **Link** Action is deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property.

Information on the **Link** Action is available in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelActionDesign) node. To access it, use the [Model Editor](xref:112582).
