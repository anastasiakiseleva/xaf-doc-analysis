---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.GetRulesFromModel(DevExpress.ExpressApp.Model.IModelClass)
name: GetRulesFromModel(IModelClass)
type: Method
summary: Returns the list of appearance rules declared in the specified [](xref:DevExpress.ExpressApp.Model.IModelClass) node.
syntax:
  content: |-
    [Browsable(false)]
    public static List<IAppearanceRuleProperties> GetRulesFromModel(IModelClass classModel)
  parameters:
  - id: classModel
    type: DevExpress.ExpressApp.Model.IModelClass
    description: An [](xref:DevExpress.ExpressApp.Model.IModelClass) object that specifies the **BOModel** | **_\<Class\>_** node.
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties}
    description: A list of [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties) properties that specifies the appearance rules.
seealso: []
---
