---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowColumnMoving
name: AllowColumnMoving
type: Property
summary: Specifies if a user can move columns within a [band](xref:113695).
syntax:
  content: |-
    [DefaultValue(true)]
    [ModelBrowsable(typeof(ModelBandsLayoutPropertyVisibilityCalculator))]
    bool AllowColumnMoving { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a user can reorder columns within a band; otherwise, **false**.'
seealso:
- linkId: "113694"
---
> [!IMPORTANT]
> The **AllowColumnMoving** property is invisible in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.