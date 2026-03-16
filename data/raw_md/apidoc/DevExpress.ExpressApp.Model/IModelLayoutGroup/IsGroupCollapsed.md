---
uid: DevExpress.ExpressApp.Model.IModelLayoutGroup.IsGroupCollapsed
name: IsGroupCollapsed
type: Property
summary: Specifies the expanded state of a [collapsible layout group](xref:DevExpress.ExpressApp.Model.IModelLayoutGroup.IsCollapsibleGroup).
syntax:
  content: |-
    [DefaultValue(false)]
    [ModelBrowsable(typeof(ModelLayoutCollapsibleGroupVisibilityCalculator))]
    bool IsGroupCollapsed { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if a layout card group is collapsed; otherwise, `false`.'
seealso: []
---
The `IsGroupCollapsed` property saves and manages the state of a [collapsible layout group](xref:DevExpress.ExpressApp.Model.IModelLayoutGroup.IsCollapsibleGroup). This option defines whether a layout group is collapsed or expanded.

WinForms
:   ![IsCollapsibleGroup Win Closed](~/images/Collapsible-WinDemonstrationClosed.png)
ASP.NET Core Blazor
:   ![IsCollapsibleGroup Blazor Closed](~/images/Collapsible-BlazorClosed.png)

The `IsGroupCollapsed` property is available in the [Model Editor](xref:112582) if the [](xref:DevExpress.ExpressApp.Model.IModelLayoutGroup.IsCollapsibleGroup) property is `True`. 
You can change the `IsGroupCollapsed` value in two ways:
* Collapse or expand a collapsible layout group in the UI.
* Access the property in the Model Editor. To do this, double-click the _MySolution\Module\Model.xamfl_ file to invoke [Model Editor](xref:112582) and navigate to the [!include[Node_Views_DetailView_Layout](~/templates/node_views_detailview_layout111385.md)] node. After that, expand the layout group node, focus the group item node, and change the `IsGroupCollapsed` property value.

   ![IsGroupCollapsed_ModelEditor](~/images/Collapsed-ModelEditorTrue.png)

   Alternatively, you can access this property in a platform-specific module (_MySolution\Blazor.Server\Model.xamfl_ or _MySolution\Win\Model.xamfl_ file) and change the setting for the ASP.NET Core Blazor or Windows Forms project respectively.
