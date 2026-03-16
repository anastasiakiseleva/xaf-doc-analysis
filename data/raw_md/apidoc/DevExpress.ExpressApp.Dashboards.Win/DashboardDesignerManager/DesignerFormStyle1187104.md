---
uid: DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.DesignerFormStyle
name: DesignerFormStyle
type: Property
summary: Specifies whether the Standard UI or Ribbon UI is used in the Dashboard Designer.
syntax:
  content: public RibbonFormStyle DesignerFormStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraBars.Ribbon.RibbonFormStyle
    description: '**RibbonFormStyle.Standard** when the Standard UI is used; **RibbonFormStyle.Ribbon** - if the Ribbon UI is used.'
seealso: []
---
If the [DashboardsWindowsFormsModule.DesignerFormStyle](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardsWindowsFormsModule.DesignerFormStyle) property value is **not null**, it is used as the default value.

If the [DashboardsWindowsFormsModule.DesignerFormStyle](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardsWindowsFormsModule.DesignerFormStyle) property value is **null**, the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property value is used as the default value.