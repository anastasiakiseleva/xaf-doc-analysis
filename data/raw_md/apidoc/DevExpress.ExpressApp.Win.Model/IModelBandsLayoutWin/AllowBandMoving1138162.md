---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowBandMoving
name: AllowBandMoving
type: Property
summary: Specifies if a user can reorder [bands](xref:113695).
syntax:
  content: |-
    [DefaultValue(true)]
    [ModelBrowsable(typeof(ModelBandsLayoutPropertyVisibilityCalculator))]
    bool AllowBandMoving { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a user can reorder bands; otherwise, **false**.'
seealso:
- linkId: "113694"
---
> [!IMPORTANT]
> The **AllowBandMoving** property is invisible in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.