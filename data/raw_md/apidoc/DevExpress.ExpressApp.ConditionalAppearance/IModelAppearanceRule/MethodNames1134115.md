---
uid: DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRule.MethodNames
name: MethodNames
type: Property
summary: Specifies the possible method names to which the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) can be applied.
syntax:
  content: |-
    [Browsable(false)]
    IEnumerable<string> MethodNames { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IEnumerable{System.String}
    description: An **IEnumerable\<String>** collection that are the possible method names to which the **Appearance** can be applied.
seealso: []
---
This property is used internally as a source for the AppearanceRule's [IAppearanceRuleProperties.Method](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Method) property drop-down list.