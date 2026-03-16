---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowChangeBandParent
name: AllowChangeBandParent
type: Property
summary: Specifies if a user can move [bands](xref:113695) from one parent band to another.
syntax:
  content: |-
    [DefaultValue(false)]
    [ModelBrowsable(typeof(ModelBandsLayoutPropertyVisibilityCalculator))]
    bool AllowChangeBandParent { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a user can move bands from one parent band to another; otherwise, **false**.'
seealso:
- linkId: "113694"
---
> [!IMPORTANT]
> The **AllowChangeBandParent** property is invisible in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.