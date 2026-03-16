---
uid: DevExpress.ExpressApp.Model.IModelDetailView.FreezeLayout
name: FreezeLayout
type: Property
summary: Specifies whether the automatic update of the [Detail View layout](xref:112817) is disabled.
syntax:
  content: |-
    [ModelBrowsable(typeof(NotNewNodeVisibleCalculator))]
    bool FreezeLayout { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the automatic update of layout is disabled; otherwise, `false`. The default is `false`.'
seealso:
- linkId: "112817"
---
By default, the Detail View layout is updated automatically in the following cases:

* when you make changes in the business model (for example, add a new property to the business class);
* when you modify the same Detail View layout at a lower [Application Model](xref:112580) layer (for example, you modify layout in the _MySolution\Module_ project and the layout is automatically updated in the _MySolution\Blazor.Server_, _MySolution\Win_, and _MySolution\Web_ projects).

Set the `FreezeLayout` property to `true` to prohibit automatic updates of the layout. In this instance, only manual modifications will be allowed.

![Layout_FreezeLayout](~/images/layout_freezelayout116768.png)

> [!NOTE]
> The `FreezeLayout` property is not available for nodes that you have added or cloned at the current Application Model layer. Layout of these nodes is never updated automatically.

When you set the `FreezeLayout` property to `true`, the [Model Editor](xref:112582) copies the current state of the layout to the model differences. As a result, any changes from lower layers (e.g., default layout generation) are overridden. When you revert the `FreezeLayout` back to `false`, Model Editor resets differences - all current layout customizations are removed.

[!include[FreezeLayoutWarning](~/templates/freezelayoutwarning11127.md)]