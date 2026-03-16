---
uid: DevExpress.ExpressApp.Editors.IAppearanceVisibility.Visibility
name: Visibility
type: Property
summary: Specifies the user interface element visibility.
syntax:
  content: ViewItemVisibility Visibility { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Editors.ViewItemVisibility
    description: A [](xref:DevExpress.ExpressApp.Editors.ViewItemVisibility) enumeration value specifying the user interface element visibility.
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Visibility
---
The UI elements that implement the **IAppearanceVisibility** interface can be made invisible/visible by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. The visibility state is changed via the **Visibility** property.