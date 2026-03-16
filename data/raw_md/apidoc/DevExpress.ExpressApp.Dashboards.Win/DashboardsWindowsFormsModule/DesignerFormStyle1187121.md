---
uid: DevExpress.ExpressApp.Dashboards.Win.DashboardsWindowsFormsModule.DesignerFormStyle
name: DesignerFormStyle
type: Property
summary: Specifies the dashboard designer form style.
syntax:
  content: public RibbonFormStyle? DesignerFormStyle { get; set; }
  parameters: []
  return:
    type: System.Nullable{DevExpress.XtraBars.Ribbon.RibbonFormStyle}
    description: '`RibbonFormStyle.Standard`, when the Standard UI is used; `RibbonFormStyle.Ribbon` - if the Ribbon UI is used.'
seealso: []
---
If the `DesignerFormStyle` value is `null`, the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) value is considered instead.