---
uid: DevExpress.ExpressApp.Model.IModelLayoutGroup.IsCollapsibleGroup
name: IsCollapsibleGroup
type: Property
summary: Specifies whether a layout group can be collapsed.
syntax:
  content: |-
    [DefaultValue(false)]
    [ModelBrowsable(typeof(ModelLayoutCollapsibleGroupVisibilityCalculator))]
    bool IsCollapsibleGroup { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if a layout card group can be collapsed; otherwise, `false`.'
seealso: []
---
The `IsCollapsibleGroup` property enables the expand/collapse button in a group of [View Items](xref:112612). This feature helps users to organize complex [Detail Views](xref:112611#detail-view) in WinForms and ASP.NET Core Blazor applications.

WinForms
:   ![IsCollapsibleGroup WinOpen](~/images/Collapsible-WinDemonstrationOpen.png)
ASP.NET Core Blazor
:   ![IsCollapsibleGroup Blazor](~/images/Collapsible-Blazor.png)

To make a selected group collapsible in WinForms and ASP.NET Core Blazor projects, double-click the _MySolution\Module\Model.xamfl_ file to invoke [Model Editor](xref:112582). Navigate to the [!include[Node_Views_DetailView_Layout](~/templates/node_views_detailview_layout111385.md)] node, expand the layout group node, focus the group item node, and set the `IsCollapsibleGroup` property value to `True`.

![IsCollapsibleGroup_ModelEditor](~/images/Collapsible-ModelEditorTrue.png)

Alternatively, you can access this property in a platform-specific module (_MySolution\Blazor.Server\Model.xamfl_ or _MySolution\Win\Model.xamfl_ file) and change the setting for the ASP.NET Core Blazor or Windows Forms project respectively.
