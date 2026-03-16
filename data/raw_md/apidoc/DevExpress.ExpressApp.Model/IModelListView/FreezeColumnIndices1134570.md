---
uid: DevExpress.ExpressApp.Model.IModelListView.FreezeColumnIndices
name: FreezeColumnIndices
type: Property
summary: Specifies whether automatic update of the [List Views](xref:112611)'s column indices is disabled.
syntax:
  content: |-
    [ModelBrowsable(typeof(NotNewNodeVisibleCalculator))]
    bool FreezeColumnIndices { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the automatic update of indices is disabled; otherwise, `false`. The default is `false`.'
seealso: []
---
By default, the column indices are updated automatically in the following cases:

* when you make changes in the business model (e.g., add a new property to the business class);
* when you modify column indices at a lower [Application Model](xref:112580) layer (for example, you modify indices in the _MySolution\Module_ project and the layout is automatically updated in the _MySolution\Blazor.Server_, _MySolution\Win_, and _MySolution\Web_ projects).

Set the `FreezeColumnIndices` property to `true` to prohibit automatic updates of column indices. In this instance, only manual modifications will be allowed.

> [!NOTE]
> The `FreezeColumnIndices` property is not available for List View nodes that you have added or cloned at the current Application Model layer. Column indices in these nodes are never updated automatically.

When you set the `FreezeColumnIndices` property to `true`, [Model Editor](xref:112582) copies the current values of column indices to the model differences. As a result, any changes from lower layers are overridden. When you revert the `FreezeColumnIndices` back to `false` the Model Editor resets differences - all current indices customizations are removed.