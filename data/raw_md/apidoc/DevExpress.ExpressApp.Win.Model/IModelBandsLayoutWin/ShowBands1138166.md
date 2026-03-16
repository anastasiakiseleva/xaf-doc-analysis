---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.ShowBands
name: ShowBands
type: Property
summary: Specifies whether or not [band](xref:113695) headers are visible.
syntax:
  content: |-
    [DefaultValue(true)]
    [ModelBrowsable(typeof(ModelBandsLayoutPropertyVisibilityCalculator))]
    bool ShowBands { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if band headers are visible, otherwise, **false**.'
seealso:
- linkId: "113694"
---
> [!IMPORTANT]
> The **ShowBands** property is invisible in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.