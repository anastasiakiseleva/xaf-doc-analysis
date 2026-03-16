---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowChangeColumnParent
name: AllowChangeColumnParent
type: Property
summary: Specifies if a user can move columns from one [band](xref:113695) to another.
syntax:
  content: |-
    [DefaultValue(false)]
    [ModelBrowsable(typeof(ModelBandsLayoutPropertyVisibilityCalculator))]
    bool AllowChangeColumnParent { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a user can move columns from one band to another; otherwise, **false**.'
seealso:
- linkId: "113694"
---
> [!IMPORTANT]
> The **AllowChangeColumnParent** property is invisible in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.