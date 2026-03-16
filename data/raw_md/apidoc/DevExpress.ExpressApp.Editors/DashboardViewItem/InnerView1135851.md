---
uid: DevExpress.ExpressApp.Editors.DashboardViewItem.InnerView
name: InnerView
type: Property
summary: Provides access to the [View](xref:112611) displayed by the [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem)'s [DashboardViewItem.Frame](xref:DevExpress.ExpressApp.Editors.DashboardViewItem.Frame).
syntax:
  content: public View InnerView { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) displayed by the DashboardViewItem's Frame.
seealso:
- linkId: DevExpress.ExpressApp.Editors.DashboardViewItem.Frame
---
To display a [View](xref:112611), a DashboardViewItem creates a nested Frame using the [TemplateContext.NestedFrame](xref:DevExpress.ExpressApp.TemplateContext.NestedFrame) template context. Use the [DashboardViewItem.Frame](xref:DevExpress.ExpressApp.Editors.DashboardViewItem.Frame) property to access this Frame.