---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.ShowColumnHeaders
name: ShowColumnHeaders
type: Property
summary: Specifies whether or not column headers are visible.
syntax:
  content: |-
    [DefaultValue(true)]
    [ModelBrowsable(typeof(ModelBandsLayoutPropertyVisibilityCalculator))]
    bool ShowColumnHeaders { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if band headers are visible, otherwise, **false**.'
seealso:
- linkId: "113694"
---
> [!IMPORTANT]
> The **ShowColumnHeaders** property is invisible in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.